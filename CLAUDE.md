# CLAUDE.md — Physical Therapy / Rehab Plan Support (idea 122)

## Skill Identity
- **Name / slug:** `physical-therapy-rehab-plan`
- **Tagline:** Physical Therapy / Rehab Plan Support
- **Source idea:** #122 (`ideas.md`)
- **Cluster:** Health, Wellness & Psychology (`health-wellness`)
- **Current phase:** Phase 4 — Testing & Validation (initial build complete)

## Problem This Skill Solves
People recovering from injury need safe, progressive rehab guidance but lack access to consistent professional input and risk re-injury from generic internet programs.

This skill becomes **an evidence-based rehabilitation advisor who reasons like a physiotherapist using clinical practice guidelines (educational, not a substitute for in-person PT)**. It is research-first, grounds every score in named world-renowned frameworks, challenges its own assumptions before concluding, and produces a professional artifact: a multi-dimensional score plus a prioritized improvement roadmap.

## Harness Flow Summary
1. **Intake** → `sub-profile-intake` gathers structured inputs.
2. **Gate / framework** → safety/risk/compliance gate runs, then the correct evaluation framework is selected.
3. **Research** → WebSearch/WebFetch enrich evidence from authoritative sources (graceful degradation to SECOND-KNOWLEDGE-BRAIN.md if unavailable).
4. **Scoring** → `sub-scoring-engine` produces a 0–100 multi-dimensional score.
5. **Roadmap** → prioritized improvement plan (effort × impact).
6. **Quality gate** → devil's-advocate review before final output.

**SAFETY GATE:** `sub-safety-screener` MUST pass before any guidance is emitted.

## Sub-skills
- `skills/sub-profile-intake.md` — Capture injury type, stage, diagnosis (if any), pain, function goals, and medical context.
- `skills/sub-safety-screener.md` — Screen for red flags (fracture, infection, DVT, neuro deficits) and gate referral before any exercise guidance.
- `skills/sub-scoring-engine.md` — Score recovery stage, safety, and progression readiness against healing-phase and CPG criteria.
- `skills/sub-improvement-roadmap.md` — Build a phased, progressive rehab roadmap with pain-monitoring rules and clear stop/seek-care triggers.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence gathering
- `Read`, `Write` — artifact production
- `Bash`/`python` — run `tools/knowledge_updater.py`

## Knowledge Sources (crawl targets)
- PubMed (rehabilitation, physiotherapy)
- JOSPT clinical practice guidelines
- Cochrane musculoskeletal reviews
- British Journal of Sports Medicine

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (weekly cron recommended).

## Active Development Tasks
- [x] Scaffold all required deliverables
- [x] Author main harness + 4 sub-skills
- [x] Define scoring dimensions: Recovery stage, Safety, Progression readiness, Pain control, Functional goal fit
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl
- [ ] Add 5+ more regression scenarios

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — living knowledge base
