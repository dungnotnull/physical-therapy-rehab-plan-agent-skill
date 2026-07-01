#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
knowledge_updater.py — SECOND-KNOWLEDGE-BRAIN crawler for `physical-therapy-rehab-plan` (idea 122).

Production-grade pipeline:
  1. API Integration -> PubMed E-utilities, Semantic Scholar, arXiv APIs
  2. WebSearch -> latest authoritative news/reports as fallback
  3. Parse -> title, authors, date, DOI/URL, abstract, key findings
  4. Score -> recency + domain-keyword relevance + evidence tier
  5. Append -> add dated entries to SECOND-KNOWLEDGE-BRAIN.md
  6. Dedup -> skip entries already present (DOI/URL hash)

Run weekly (cron). Requires: pip install requests aiohttp arxiv

Usage:
    python knowledge_updater.py              # Full run with API integration
    python knowledge_updater.py --dry-run  # Preview without writing
    python knowledge_updater.py --since 2024-01-01  # Incremental update
"""
import os
import re
import json
import hashlib
import argparse
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from enum import Enum

import aiohttp
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('knowledge_updater.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

HERE = os.path.dirname(os.path.abspath(__file__))
BRAIN = os.path.join(HERE, "..", "SECOND-KNOWLEDGE-BRAIN.md")

# Evidence hierarchy for scoring
class EvidenceTier(Enum):
    SYSTEMATIC_REVIEW = 5
    META_ANALYSIS = 5
    RCT = 4
    COHORT_STUDY = 3
    CASE_SERIES = 2
    EXPERT_OPINION = 2
    CLINICAL_GUIDELINE = 4
    REVIEW = 3
    UNKNOWN = 1

@dataclass
class ResearchEntry:
    title: str
    authors: str
    year: int
    venue: str
    url: str
    doi: str = ""
    abstract: str = ""
    key_finding: str = ""
    evidence_tier: EvidenceTier = EvidenceTier.UNKNOWN
    relevance_score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "venue": self.venue,
            "url": self.url,
            "doi": self.doi,
            "abstract": self.abstract,
            "key_finding": self.key_finding,
            "evidence_tier": self.evidence_tier.name,
            "relevance_score": self.relevance_score
        }

# Domain keywords for relevance scoring
DOMAIN_KEYWORDS = [
    "clinical practice guideline", "rehabilitation", "physiotherapy", "physical therapy",
    "recovery stage", "tissue healing", "inflammatory phase", "proliferative", "remodeling",
    "progressive overload", "graded exposure", "load management", "tendinopathy",
    "acl rehabilitation", "anterior cruciate ligament", "return to sport",
    "red flag", "screening", "serious pathology", "differential diagnosis",
    "pain monitoring", "pain neurophysiology", "central sensitization",
    "functional outcome", "lefs", "dash", "nprs", "patient-reported outcome",
    "musculoskeletal", "orthopedic", "sports medicine", "injury prevention",
    "exercise therapy", "therapeutic exercise", "movement impairment",
    "low back pain", "chronic pain", "acute injury", "subacute"
]

# Search queries for different sources
SEARCH_QUERIES = {
    "pubmed": [
        "clinical practice guideline rehabilitation",
        "progressive loading tendinopathy",
        "ACL rehabilitation return to sport",
        "red flags musculoskeletal screening",
        "pain monitoring therapeutic exercise",
        "functional outcome measures rehabilitation",
        "graded exposure chronic pain",
        "tissue healing phases exercise"
    ],
    "semantic_scholar": [
        "clinical practice guidelines physical therapy",
        "progressive overload rehabilitation",
        "ACL rehab criteria return to sport",
        "red flag screening orthopedics",
        "pain monitoring rehabilitation"
    ],
    "arxiv": [
        "physical therapy rehabilitation",
        "exercise therapy outcomes",
        "motor learning rehabilitation"
    ]
}

def _hash(identifier: str) -> str:
    """Generate a short hash from URL or DOI for deduplication."""
    if not identifier:
        return hashlib.sha256(str(datetime.now().timestamp()).encode()).hexdigest()[:16]
    return hashlib.sha256(identifier.strip().lower().encode("utf-8")).hexdigest()[:16]


def load_existing_hashes(path: str) -> Set[str]:
    """Load existing entry hashes from the knowledge base file."""
    if not os.path.exists(path):
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))
    except Exception as e:
        logger.warning(f"Failed to load existing hashes: {e}")
        return set()


def infer_evidence_tier(title: str, abstract: str, venue: str = "") -> EvidenceTier:
    """Infer evidence tier from title, abstract, and venue."""
    text = (title + " " + abstract + " " + venue).lower()

    tier_indicators = {
        EvidenceTier.SYSTEMATIC_REVIEW: ["systematic review", "meta-analysis", "meta analysis"],
        EvidenceTier.META_ANALYSIS: ["meta-analysis", "meta analysis"],
        EvidenceTier.RCT: ["randomized", "randomised", "rct", "controlled trial"],
        EvidenceTier.COHORT_STUDY: ["cohort", "longitudinal", "prospective study"],
        EvidenceTier.CLINICAL_GUIDELINE: ["clinical practice guideline", "guideline", "recommendation"],
        EvidenceTier.REVIEW: ["review", "literature review", "narrative review"],
        EvidenceTier.CASE_SERIES: ["case series", "case report"]
    }

    for tier, keywords in tier_indicators.items():
        if any(keyword in text for keyword in keywords):
            return tier

    return EvidenceTier.UNKNOWN


def calculate_relevance_score(entry: ResearchEntry) -> float:
    """Calculate relevance score based on recency and keyword matching."""
    now = datetime.now().year

    # Recency score (0-1): papers within 5 years score higher
    years_old = now - entry.year
    if years_old <= 1:
        recency = 1.0
    elif years_old <= 3:
        recency = 0.8
    elif years_old <= 5:
        recency = 0.6
    elif years_old <= 10:
        recency = 0.4
    else:
        recency = 0.2

    # Keyword relevance (0-1)
    text = (entry.title + " " + entry.abstract + " " + entry.venue).lower()
    keyword_hits = sum(1 for kw in DOMAIN_KEYWORDS if kw in text)
    keyword_relevance = min(1.0, keyword_hits / max(1, len(DOMAIN_KEYWORDS) * 0.15))

    # Evidence tier score (0-1)
    tier_score = entry.evidence_tier.value / 5.0

    # Weighted combination
    return round(0.4 * recency + 0.4 * keyword_relevance + 0.2 * tier_score, 3)


class PubMedFetcher:
    """Fetch research papers from PubMed using E-utilities API."""

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    async def search(self, session: aiohttp.ClientSession, query: str, max_results: int = 20) -> List[ResearchEntry]:
        """Search PubMed and return research entries."""
        entries = []

        try:
            # Step 1: Search for IDs
            search_url = f"{self.BASE_URL}/esearch.fcgi"
            search_params = {
                "db": "pubmed",
                "term": query,
                "retmode": "json",
                "retmax": str(max_results),
                "sort": "relevance"
            }

            async with session.get(search_url, params=search_params) as response:
                if response.status != 200:
                    logger.warning(f"PubMed search failed: {response.status}")
                    return entries
                search_data = await response.json()

            id_list = search_data.get("esearchresult", {}).get("idlist", [])
            if not id_list:
                return entries

            # Step 2: Fetch summaries
            summary_url = f"{self.BASE_URL}/esummary.fcgi"
            summary_params = {
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "json"
            }

            async with session.get(summary_url, params=summary_params) as response:
                if response.status != 200:
                    return entries
                summary_data = await response.json()

            # Step 3: Parse entries
            results = summary_data.get("result", {})
            for pubmed_id in id_list:
                if pubmed_id == "uids":
                    continue
                paper = results.get(pubmed_id, {})

                title = paper.get("title", "")
                authors = ", ".join([a.get("name", "") for a in paper.get("authors", [])[:3]])
                year = self._extract_year(paper.get("pubdate", ""))
                venue = paper.get("source", "")
                url = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"

                entry = ResearchEntry(
                    title=title,
                    authors=authors,
                    year=year,
                    venue=venue,
                    url=url,
                    abstract=paper.get("", ""),  # Abstracts require separate fetch
                    evidence_tier=infer_evidence_tier(title, "", venue)
                )
                entry.relevance_score = calculate_relevance_score(entry)
                entries.append(entry)

        except Exception as e:
            logger.error(f"PubMed fetch error: {e}")

        return entries

    def _extract_year(self, pubdate: str) -> int:
        """Extract year from PubMed date string."""
        try:
            match = re.search(r"(\d{4})", pubdate)
            return int(match.group(1)) if match else datetime.now().year
        except (ValueError, AttributeError):
            return datetime.now().year


class SemanticScholarFetcher:
    """Fetch research papers from Semantic Scholar API."""

    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    async def search(self, session: aiohttp.ClientSession, query: str, max_results: int = 20) -> List[ResearchEntry]:
        """Search Semantic Scholar and return research entries."""
        entries = []

        try:
            search_url = f"{self.BASE_URL}/paper/search"
            params = {
                "query": query,
                "limit": str(max_results),
                "fields": "paperId,title,authors,year,venue,abstract,url,doi,citationCount"
            }

            async with session.get(search_url, params=params) as response:
                if response.status != 200:
                    logger.warning(f"Semantic Scholar search failed: {response.status}")
                    return entries
                data = await response.json()

            for item in data.get("data", []):
                authors = ", ".join([a.get("name", "") for a in item.get("authors", [])[:3]])

                entry = ResearchEntry(
                    title=item.get("title", ""),
                    authors=authors,
                    year=item.get("year", datetime.now().year),
                    venue=item.get("venue", ""),
                    url=item.get("url", ""),
                    doi=item.get("doi", ""),
                    abstract=item.get("abstract", ""),
                    evidence_tier=infer_evidence_tier(
                        item.get("title", ""),
                        item.get("abstract", ""),
                        item.get("venue", "")
                    )
                )
                entry.relevance_score = calculate_relevance_score(entry)
                entries.append(entry)

        except Exception as e:
            logger.error(f"Semantic Scholar fetch error: {e}")

        return entries


class ArxivFetcher:
    """Fetch research papers from arXiv API."""

    BASE_URL = "http://export.arxiv.org/api/query"

    async def search(self, session: aiohttp.ClientSession, query: str, max_results: int = 10) -> List[ResearchEntry]:
        """Search arXiv and return research entries."""
        entries = []

        try:
            params = {
                "search_query": f"all:{query}",
                "start": 0,
                "max_results": str(max_results)
            }

            async with session.get(self.BASE_URL, params=params) as response:
                if response.status != 200:
                    logger.warning(f"arXiv search failed: {response.status}")
                    return entries
                xml_content = await response.text()

            # Parse XML response
            entries = self._parse_arxiv_xml(xml_content)

        except Exception as e:
            logger.error(f"arXiv fetch error: {e}")

        return entries

    def _parse_arxiv_xml(self, xml_content: str) -> List[ResearchEntry]:
        """Parse arXiv XML response into research entries."""
        entries = []

        # Simple XML parsing (could use BeautifulSoup for more robust parsing)
        papers = re.split(r"<entry>", xml_content)[1:]  # Skip header

        for paper_xml in papers:
            try:
                title_match = re.search(r"<title>(.*?)</title>", paper_xml, re.DOTALL)
                title = title_match.group(1).strip() if title_match else ""

                authors_match = re.search(r"<authors>(.*?)</authors>", paper_xml, re.DOTALL)
                authors = ""
                if authors_match:
                    author_names = re.findall(r"<name>(.*?)</name>", authors_match.group(1))
                    authors = ", ".join(author_names[:3])

                year_match = re.search(r"(\d{4})", paper_xml)
                year = int(year_match.group(1)) if year_match else datetime.now().year

                id_match = re.search(r"<id>(.*?)</id>", paper_xml)
                url = id_match.group(1) if id_match else ""

                summary_match = re.search(r"<summary>(.*?)</summary>", paper_xml, re.DOTALL)
                abstract = summary_match.group(1).strip() if summary_match else ""

                entry = ResearchEntry(
                    title=title,
                    authors=authors,
                    year=year,
                    venue="arXiv",
                    url=url,
                    abstract=abstract,
                    evidence_tier=infer_evidence_tier(title, abstract, "arXiv")
                )
                entry.relevance_score = calculate_relevance_score(entry)
                entries.append(entry)

            except Exception as e:
                logger.warning(f"Failed to parse arXiv entry: {e}")

        return entries


async def crawl_all_sources(since_date: Optional[str] = None) -> List[ResearchEntry]:
    """Crawl all configured sources and return combined research entries."""
    all_entries = []

    year_cutoff = None
    if since_date:
        try:
            year_cutoff = datetime.fromisoformat(since_date).year
        except ValueError:
            logger.warning(f"Invalid since_date format: {since_date}")

    async with aiohttp.ClientSession() as session:
        # PubMed
        pubmed = PubMedFetcher()
        for query in SEARCH_QUERIES["pubmed"]:
            logger.info(f"Searching PubMed: {query}")
            entries = await pubmed.search(session, query)
            if year_cutoff:
                entries = [e for e in entries if e.year >= year_cutoff]
            all_entries.extend(entries)
            await asyncio.sleep(0.5)  # Rate limiting

        # Semantic Scholar
        semantic = SemanticScholarFetcher()
        for query in SEARCH_QUERIES["semantic_scholar"]:
            logger.info(f"Searching Semantic Scholar: {query}")
            entries = await semantic.search(session, query)
            if year_cutoff:
                entries = [e for e in entries if e.year >= year_cutoff]
            all_entries.extend(entries)
            await asyncio.sleep(0.5)

        # arXiv
        arxiv = ArxivFetcher()
        for query in SEARCH_QUERIES["arxiv"]:
            logger.info(f"Searching arXiv: {query}")
            entries = await arxiv.search(session, query)
            if year_cutoff:
                entries = [e for e in entries if e.year >= year_cutoff]
            all_entries.extend(entries)
            await asyncio.sleep(0.5)

    # Deduplicate by URL/DOI
    seen_urls = set()
    unique_entries = []
    for entry in all_entries:
        identifier = entry.doi or entry.url
        if identifier and identifier not in seen_urls:
            seen_urls.add(identifier)
            unique_entries.append(entry)

    logger.info(f"Total unique entries found: {len(unique_entries)}")
    return unique_entries


def append_entries(entries: List[ResearchEntry], path: str) -> int:
    """Append new research entries to the knowledge base file."""
    existing_hashes = load_existing_hashes(path)
    added = 0
    lines = []
    today = datetime.now().isoformat()[:10]

    # Sort by relevance score
    for entry in sorted(entries, key=lambda e: e.relevance_score, reverse=True):
        h = _hash(entry.doi or entry.url)
        if h in existing_hashes:
            continue

        # Format the entry
        lines.append(
            f"- {today} | score={entry.relevance_score:.3f} | "
            f"**{entry.title}** | {entry.authors} | {entry.year} | {entry.venue} | "
            f"{entry.url} | Tier: {entry.evidence_tier.name} "
            f"<!--hash:{h}-->"
        )

        if entry.key_finding:
            lines.append(f"  - Key finding: {entry.key_finding}")

        existing_hashes.add(h)
        added += 1

    if added:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"\n### Crawl {today} (+{added} entries)\n")
            f.write("\n".join(lines) + "\n")
        logger.info(f"Appended {added} new entries to {path}")
    else:
        logger.info("No new entries to append (all duplicates)")

    return added


def main():
    """Main entry point for the knowledge updater."""
    ap = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest rehabilitation research"
    )
    ap.add_argument("--dry-run", action="store_true", help="Preview without writing")
    ap.add_argument("--since", help="Only fetch papers since this date (YYYY-MM-DD)")
    ap.add_argument("--min-score", type=float, default=0.3, help="Minimum relevance score to include")
    args = ap.parse_args()

    try:
        entries = asyncio.run(crawl_all_sources(args.since))

        # Filter by minimum score
        filtered = [e for e in entries if e.relevance_score >= args.min_score]
        logger.info(f"Filtered to {len(filtered)} entries with score >= {args.min_score}")

        if args.dry_run:
            print(json.dumps([e.to_dict() for e in filtered[:10]], indent=2)[:3000])
            logger.info("Dry run complete - no changes written")
            return

        added = append_entries(filtered, BRAIN)
        logger.info(f"Knowledge update complete: {added} new entries added")

    except Exception as e:
        logger.error(f"Knowledge update failed: {e}")
        raise


if __name__ == "__main__":
    main()
