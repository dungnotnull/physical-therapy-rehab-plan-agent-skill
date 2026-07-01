# PROJECT-detail.md — Physical Therapy / Rehab Plan Support

## Executive Summary
`physical-therapy-rehab-plan` is a Claude Skill that turns Claude into **an evidence-based rehabilitation advisor who reasons like a physiotherapist using clinical practice guidelines (educational, not a substitute for in-person PT)**. It ingests domain inputs, screens for safety/compliance where required, selects a world-renowned evaluation framework, gathers fresh evidence, scores the subject across 5 dimensions, and outputs a prioritized improvement roadmap. It is part of the **Health, Wellness & Psychology** cluster.

## Problem Statement
People recovering from injury need safe, progressive rehab guidance but lack access to consistent professional input and risk re-injury from generic internet programs.

Domain context: practitioners need reproducible, evidence-graded evaluation rather than ad-hoc opinion. This skill enforces a research-first harness with explicit quality gates and a self-improving knowledge base.

## Target Users & Use Cases
- Primary: practitioners, learners, and decision-makers in this domain.
- Trigger examples:
1. **Ankle sprain week 2** — Grade II lateral sprain. Expect phase-appropriate loading plan and pain traffic-light rules.
2. **Possible DVT red flag** — Calf swelling, warmth, recent surgery. Expect safety gate and urgent-referral, no exercises.
3. **Post-op ACL milestone** — 12 weeks post-ACLR. Expect criterion-based progression and return-to-sport caveats with PT referral.
4. **Chronic low back pain** — Non-specific LBP. Expect graded-exposure roadmap and red-flag screening.
5. **Shoulder, no diagnosis** — Pain, no imaging. Expect graceful caution, referral note, and conservative general program.

## Harness Architecture
```
/physical-therapy-rehab-plan  (main.md)
   |
   v
[1] sub-profile-intake        -> structured intake
   |
   v
[2] GATE: sub-safety-screener  -> blocks unsafe/non-compliant requests
   |
   v
[3] research (WebSearch/WebFetch)        -> evidence (graceful deg: SECOND-KNOWLEDGE-BRAIN.md)
   |
   v
[4] scoring engine                       -> 0-100 multi-dimensional score
   |
   v
[5] improvement roadmap                  -> effort x impact prioritized actions
   |
   v
[6] quality-gate / devil's advocate      -> final professional artifact
```

## Full Sub-Skill Catalog
#### `sub-profile-intake`
- **Purpose:** Capture injury type, stage, diagnosis (if any), pain, function goals, and medical context.
- **Inputs:** structured outputs from prior stage + user-supplied data
- **Outputs:** validated, structured payload for the next stage
- **Tools:** Read, Write
- **Quality gate:** output schema validated before proceeding

#### `sub-safety-screener`
- **Purpose:** Screen for red flags (fracture, infection, DVT, neuro deficits) and gate referral before any exercise guidance.
- **Inputs:** structured outputs from prior stage + user-supplied data
- **Outputs:** validated, structured payload for the next stage
- **Tools:** Read, Write
- **Quality gate:** BLOCKS the harness until satisfied (hard gate)

#### `sub-scoring-engine`
- **Purpose:** Score recovery stage, safety, and progression readiness against healing-phase and CPG criteria.
- **Inputs:** structured outputs from prior stage + user-supplied data
- **Outputs:** validated, structured payload for the next stage
- **Tools:** Read, Write, WebSearch/WebFetch
- **Quality gate:** output schema validated before proceeding

#### `sub-improvement-roadmap`
- **Purpose:** Build a phased, progressive rehab roadmap with pain-monitoring rules and clear stop/seek-care triggers.
- **Inputs:** structured outputs from prior stage + user-supplied data
- **Outputs:** validated, structured payload for the next stage
- **Tools:** Read, Write
- **Quality gate:** output schema validated before proceeding


## Evaluation Frameworks (world-renowned, citable)
- Tissue-healing phases (inflammatory/proliferative/remodeling)
- Progressive overload & graded exposure
- Clinical practice guidelines (APTA, JOSPT)
- Red-flag screening (serious pathology)
- Pain-monitoring (traffic-light) models
- Outcome measures (e.g., LEFS, DASH, NPRS)

## Scoring Model
| Dimension | Range | Notes |
|-----------|-------|-------|
| Recovery stage | 0–100 | Weighted contribution to the composite index |
| Safety | 0–100 | Weighted contribution to the composite index |
| Progression readiness | 0–100 | Weighted contribution to the composite index |
| Pain control | 0–100 | Weighted contribution to the composite index |
| Functional goal fit | 0–100 | Weighted contribution to the composite index |

Composite = weighted mean of dimensions (weights justified per case, surfaced to the user). Every dimension score must cite at least one framework criterion or evidence source.

## Skill File Format Specification
Frontmatter: `name`, `description`. Required sections in `main.md`: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse user request; if inputs missing, run intake questions.
2. Run hard gate; if it fails, STOP and emit referral/disclaimer.
3. Gather evidence (prefer Systematic Review > Meta-analysis > RCT/empirical > expert opinion).
4. Score each dimension with cited justification.
5. Build prioritized roadmap.
6. Run devil's-advocate quality gate; revise; present artifact.
- Error handling: missing data → state assumptions + confidence; tool failure → degrade to knowledge base and signal limitation.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: PubMed (rehabilitation, physiotherapy), JOSPT clinical practice guidelines, Cochrane musculoskeletal reviews, British Journal of Sports Medicine.
- Crawl queries: clinical practice guideline rehabilitation, progressive loading tendinopathy evidence, ACL rehab criteria return to sport, red flags musculoskeletal screening.
- Append format: dated entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance.

## Supporting Tools Spec — `knowledge_updater.py`
- Inputs: source list + query list (above), `--since` date.
- Outputs: appended, de-duplicated entries in `SECOND-KNOWLEDGE-BRAIN.md`.
- Schedule: weekly cron.

## Quality Gates (must be true before final output)
- [ ] Hard safety/risk/compliance gate passed or referral issued
- [ ] Every score cites a framework criterion or evidence source
- [ ] Roadmap items have effort + impact + owner
- [ ] Assumptions and confidence stated; limitations disclosed
- [ ] Devil's-advocate pass completed

## Test Scenarios (≥5)
1. **Ankle sprain week 2** — Grade II lateral sprain. Expect phase-appropriate loading plan and pain traffic-light rules.
2. **Possible DVT red flag** — Calf swelling, warmth, recent surgery. Expect safety gate and urgent-referral, no exercises.
3. **Post-op ACL milestone** — 12 weeks post-ACLR. Expect criterion-based progression and return-to-sport caveats with PT referral.
4. **Chronic low back pain** — Non-specific LBP. Expect graded-exposure roadmap and red-flag screening.
5. **Shoulder, no diagnosis** — Pain, no imaging. Expect graceful caution, referral note, and conservative general program.

## Key Design Decisions
1. Research-first; no memory-only claims when search is possible.
2. Named frameworks only — never ad hoc criteria.
3. Hard gate precedes all guidance for this safety/compliance-sensitive domain.
4. Multi-dimensional score + prioritized roadmap are mandatory outputs.
5. Self-improving knowledge base via weekly crawl.
