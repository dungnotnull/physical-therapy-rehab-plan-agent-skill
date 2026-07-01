# Physical Therapy / Rehab Plan Support

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](https://github.com/dungnotnull/physical-therapy-rehab-plan-agent-skill)
[![Phase: 100% Complete](https://img.shields.io/badge/Phase-100%25%20Complete-brightgreen.svg)](https://github.com/dungnotnull/physical-therapy-rehab-plan-agent-skill)

An evidence-based rehabilitation advisor that reasons like a physiotherapist using clinical practice guidelines. Built for Claude AI, this skill provides safe, progressive rehab guidance based on world-renowned frameworks and peer-reviewed research.

## Overview

This skill transforms Claude into an **evidence-based rehabilitation advisor** that:

- Screens for red flags before any exercise guidance
- Scores recovery across 5 validated dimensions
- Generates prioritized improvement roadmaps
- Cites world-renowned frameworks and research papers
- Maintains a self-improving knowledge base

> **Educational Purpose:** This skill is for educational purposes only and is not a substitute for in-person physical therapy or medical care.

## Key Features

- Safety-first architecture with hard gate blocking
- Multi-dimensional scoring (0-100) across recovery domains
- Evidence-based recommendations from peer-reviewed research
- Progressive, graded exposure protocols
- Pain monitoring with traffic-light system
- Real-time knowledge updates via API integrations
- Comprehensive test coverage

## How It Works

The harness follows a systematic workflow:

```
User Input → Intake → HARD GATE → Research → Scoring → Roadmap → Quality Gate → Output
```

1. **Intake:** Captures injury type, stage, diagnosis, pain, goals, and medical context
2. **Safety Gate:** Screens for red flags (fracture, infection, DVT, neuro deficits) — BLOCKS if present
3. **Research:** Gathers evidence from PubMed, JOSPT, Cochrane, and other authoritative sources
4. **Scoring:** Scores 5 dimensions (0-100) with cited frameworks
5. **Roadmap:** Generates prioritized improvement plan (effort × impact)
6. **Quality Gate:** Devil's advocate review before final output

## Scoring Dimensions

| Dimension | Range | Framework |
|-----------|-------|-----------|
| Recovery Stage | 0-100 | Tissue-healing phases |
| Safety | 0-100 | Red-flag screening protocols |
| Progression Readiness | 0-100 | Progressive overload principles |
| Pain Control | 0-100 | Pain monitoring systems |
| Functional Goal Fit | 0-100 | Clinical practice guidelines |

## Installation

### Prerequisites

- Python 3.8 or higher
- Claude AI or compatible Claude Code environment

### Install Dependencies

```bash
cd tools
pip install -r requirements.txt
```

Required packages:
- aiohttp >= 3.9.0
- requests >= 2.31.0
- arxiv >= 2.1.0

### Install the Skill

Place the skill files in your Claude skills directory or load them according to your Claude environment's instructions.

## Usage

### Basic Usage

Invoke the skill with a rehabilitation scenario:

```
I have a grade II ankle sprain, week 2. What's my recovery plan?
```

The skill will:
1. Ask targeted intake questions if information is missing
2. Screen for red flags
3. Score your recovery across 5 dimensions
4. Generate a prioritized improvement roadmap

### Example Scenarios

**Scenario 1: Ankle Sprain**
```
Input: Grade II lateral ankle sprain, week 2, pain 3/10 at rest
Output: 
- Recovery Stage: 65/100 (proliferative phase)
- Safety: 90/100 (no red flags)
- Progression Readiness: 60/100 (pain needs addressing)
- Roadmap: Pain monitoring, ROM exercises, progressive WB, balance training
```

**Scenario 2: DVT Red Flag**
```
Input: Calf swelling, warmth, recent surgery
Output: URGENT REFERRAL - Possible DVT, seek immediate care
(Note: Harness blocks, no rehab guidance provided)
```

**Scenario 3: ACL Return to Sport**
```
Input: 12 weeks post-ACL reconstruction, want to return to soccer
Output:
- Recovery Stage: 75/100 (remodeling phase)
- Safety: 88/100 (stable graft)
- Progression Readiness: 65/100 (needs objective criteria)
- Roadmap: LSI testing, ACL-RSI assessment, sport-specific progression
```

## Knowledge Base

The skill maintains a living knowledge base in `SECOND-KNOWLEDGE-BRAIN.md` containing:

- 50+ foundational research papers
- Clinical practice guidelines
- Evidence-based frameworks
- Clinical reasoning rules

### Updating Knowledge

Run the knowledge updater to fetch new research:

```bash
cd tools
python knowledge_updater.py                    # Full update
python knowledge_updater.py --dry-run        # Preview changes
python knowledge_updater.py --since 2024-01-01  # Incremental update
```

The updater integrates with:
- PubMed E-utilities API
- Semantic Scholar API
- arXiv API

## Testing

### Run Test Scenarios

The skill includes 5 comprehensive test scenarios in `tests/test-scenarios.md`:

1. Ankle sprain week 2
2. Possible DVT red flag
3. Post-op ACL milestone
4. Chronic low back pain
5. Shoulder, no diagnosis

### Run Regression Tests

Execute the 20 regression tests in `tests/regression-tests.md` to verify:
- Hard gate blocking behavior
- Scorecard completeness
- Roadmap structure
- Tool failure graceful degradation
- Edge case handling

## Architecture

### Skill Components

```
skills/
├── main.md                    # Main harness
├── sub-profile-intake.md     # Intake sub-skill
├── sub-safety-screener.md    # Safety gate (HARD GATE)
├── sub-scoring-engine.md     # Scoring engine
└── sub-improvement-roadmap.md # Roadmap generator
```

### Knowledge Pipeline

```
tools/
├── knowledge_updater.py       # API integrations + crawler
└── requirements.txt           # Dependencies
```

### Documentation

```
PROJECT-detail.md                      # Technical specification
PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase tracking
PROJECT-COMPLETION-SUMMARY.md          # Completion summary
CLUSTER-INTEGRATION.md                 # Cluster integration
CLUSTER-SHARING-PROTOCOL.md            # Sharing protocol
CLAUDE.md                              # Project instructions
SECOND-KNOWLEDGE-BRAIN.md              # Knowledge base
```

## Clinical Frameworks

The skill grounds all recommendations in these world-renowned frameworks:

- Tissue-healing phases (inflammatory/proliferative/remodeling)
- Progressive overload & graded exposure
- Clinical practice guidelines (APTA, JOSPT)
- Red-flag screening (serious pathology)
- Pain-monitoring (traffic-light) models
- Outcome measures (LEFS, DASH, NPRS)

## Safety Features

### Hard Gate Blocking

The safety gate **BLOCKS** the harness when red flags are present:

- Suspected fracture (deformity, inability to bear weight)
- Infection signs (fever, warmth, erythema)
- Deep vein thrombosis (unilateral swelling, warmth)
- Neurological deficits (sensation loss, motor weakness)
- Systemic signs of serious pathology

When blocked, the skill:
1. STOPS immediately
2. Emits urgent referral instructions
3. Provides emergency warning signs
4. Does NOT produce exercise guidance

### Pain Monitoring

Traffic-light system for activity-based pain monitoring:

**Green (Continue):**
- Pain ≤ 3/10 during activity
- No increase 24 hours post-activity
- Full next-day recovery

**Yellow (Modify):**
- Pain 4-6/10 during activity
- Temporary flare overnight
- Reduce volume by 25%

**Red (Stop + Seek Care):**
- Pain ≥ 7/10
- Loss of function
- New or worsening symptoms

## Cluster Integration

This skill is part of the **Health, Wellness & Psychology** cluster, which includes:

- Physical Therapy / Rehab Plan Support (this skill)
- Mental Health & Wellness Support (planned)
- Sleep & Recovery Optimization (planned)
- Nutrition & Performance Fueling (planned)
- Stress & Resilience Management (planned)

Shared sub-skills enable consistent quality across cluster skills.

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear documentation
4. Ensure all tests pass
5. Submit a pull request

### Contribution Areas

- Add research papers to knowledge base
- Improve framework coverage
- Add test scenarios
- Enhance documentation
- Fix bugs or issues

## Documentation

- [Technical Specification](PROJECT-detail.md) - Full technical details
- [Development Tracking](PROJECT-DEVELOPMENT-PHASE-TRACKING.md) - Phase completion status
- [Cluster Integration](CLUSTER-INTEGRATION.md) - Cross-skill integration
- [Sharing Protocol](CLUSTER-SHARING-PROTOCOL.md) - Sub-skill sharing
- [Test Scenarios](tests/test-scenarios.md) - Comprehensive test cases
- [Regression Tests](tests/regression-tests.md) - Regression test suite

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this skill in your work, please cite:

```
Physical Therapy / Rehab Plan Support Skill
https://github.com/dungnotnull/physical-therapy-rehab-plan-agent-skill
```

## Acknowledgments

Built upon frameworks and research from:
- American Physical Therapy Association (APTA)
- Journal of Orthopaedic & Sports Physical Therapy (JOSPT)
- British Journal of Sports Medicine
- Cochrane Musculoskeletal Reviews
- PubMed Central

## Disclaimer

This skill is for **educational purposes only** and is not a substitute for:

- In-person physical therapy
- Medical diagnosis or treatment
- Professional healthcare advice

Always consult with qualified healthcare professionals for:
- Medical emergencies
- Injury diagnosis
- Treatment decisions
- Return-to-sport clearance

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the documentation
- Check existing test scenarios

---

**Status:** Production Ready | **Phase:** 100% Complete | **License:** MIT

Made with evidence-based care for the rehabilitation community.
