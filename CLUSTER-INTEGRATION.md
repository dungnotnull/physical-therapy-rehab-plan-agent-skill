# CLUSTER-INTEGRATION.md — Health, Wellness & Psychology Cluster

Cross-skill integration documentation for `physical-therapy-rehab-plan` and sibling skills in the Health, Wellness & Psychology cluster.

---

## Cluster Overview

**Cluster:** Health, Wellness & Psychology (`health-wellness`)

**Purpose:** Evidence-based guidance for physical and mental health, recovery, and performance optimization using authoritative frameworks and clinical best practices.

**Skills in Cluster:**

| Skill | Slug | Focus Area | Status |
|-------|------|------------|--------|
| Physical Therapy / Rehab Plan Support | `physical-therapy-rehab-plan` | Musculoskeletal injury rehab, exercise progression, clinical reasoning | **Active (this skill)** |
| Mental Health & Wellness Support | `mental-health-wellness-support` | Psychological well-being, coping strategies, mental health resources | Planned |
| Sleep & Recovery Optimization | `sleep-recovery-optimization` | Sleep hygiene, recovery protocols, circadian rhythm | Planned |
| Nutrition & Performance Fueling | `nutrition-performance-fueling` | Evidence-based nutrition, supplementation, fueling strategies | Planned |
| Stress & Resilience Management | `stress-resilience-management` | Stress physiology, resilience building, adaptation strategies | Planned |

---

## Shared Sub-Skills

### Sub-Skill Sharing Protocol

When multiple skills in the cluster require similar functionality, shared sub-skills are defined once and reused to ensure consistency and reduce duplication.

#### Current Shared Sub-Skills

| Sub-Skill | Shared By | Purpose | Location |
|-----------|-----------|---------|----------|
| `sub-profile-intake` | All cluster skills | Standardized intake pattern (condition, stage, goals, context) | `skills/sub-profile-intake.md` |
| `sub-safety-screener` | Physical Therapy, Mental Health, Sleep | Safety/risk/compliance gate before any guidance | `skills/sub-safety-screener.md` |
| `sub-scoring-engine` | All cluster skills | Multi-dimensional scoring against frameworks | `skills/sub-scoring-engine.md` |
| `sub-improvement-roadmap` | All cluster skills | Prioritized improvement roadmap (effort × impact) | `skills/sub-improvement-roadmap.md` |

#### Sharing Implementation

**File Structure:**
```
skills/
├── shared/                                    # Shared sub-skills
│   ├── sub-profile-intake.md
│   ├── sub-safety-screener.md
│   ├── sub-scoring-engine.md
│   └── sub-improvement-roadmap.md
├── physical-therapy-rehab-plan/
│   └── main.md                                # References shared sub-skills
├── mental-health-wellness-support/
│   └── main.md                                # References shared sub-skills
└── ...
```

**In Main Skill Files:**
```markdown
## Sub-skills Available
- `shared/sub-profile-intake` — Capture condition, stage, goals, context
- `shared/sub-safety-screener` — Safety/risk/compliance gate
- `shared/sub-scoring-engine` — Multi-dimensional scoring
- `shared/sub-improvement-roadmap` — Prioritized improvement roadmap
```

---

## Aligned Scoring Scales

### Cluster-Wide Scoring Principles

All cluster skills use a 0-100 scoring scale with consistent dimensions where applicable:

**Common Dimensions:**
- **Safety / Risk** — 0 (high risk) to 100 (minimal risk)
- **Progression Readiness** — 0 (not ready) to 100 (ready to progress)
- **Goal Alignment** — 0 (poor fit) to 100 (excellent fit)

**Skill-Specific Dimensions:**
- Physical Therapy: Recovery Stage, Pain Control
- Mental Health: Symptom Severity, Functional Impairment
- Sleep: Sleep Quality, Recovery Adequacy
- Nutrition: Nutritional Adequacy, Fueling Optimization
- Stress: Stress Level, Resilience Capacity

### Scoring Alignment

| Dimension | Physical Therapy | Mental Health | Sleep | Notes |
|-----------|-----------------|--------------|-------|-------|
| Safety | Red flag screening | Crisis risk screening | Sleep disorder screening | All use 0-100, 100 = safest |
| Progression | Tissue healing readiness | Stability for therapy work | Sleep consistency for changes | All use 0-100 |
| Goal Fit | Functional goals | Therapeutic goals | Sleep/recovery goals | All use 0-100 |

---

## Cross-Referral Protocol

### When to Refer Between Skills

**Physical Therapy → Mental Health:**
- Chronic pain with significant catastrophizing
- Fear-avoidance patterns limiting rehabilitation
- Depression/anxiety impacting recovery motivation
- Body image concerns post-injury/surgery

**Physical Therapy → Sleep:**
- Pain disrupting sleep quality
- Night pain affecting recovery
- Post-surgical sleep positioning difficulties

**Physical Therapy → Nutrition:**
- Optimizing tissue healing through nutrition
- Weight management considerations for load management
- Supplementation for bone/tissue health

**Mental Health → Physical Therapy:**
- Somatic symptoms of anxiety/depression
- Exercise as adjunct to mental health treatment
- Mind-body integration approaches

**Sleep → Physical Therapy:**
- Inadequate recovery affecting rehabilitation
- Sleep quality impacting pain perception

**Nutrition → Physical Therapy:**
- Nutritional support for injury recovery
- Fueling strategies for return to performance

### Cross-Referral Triggers

| From Skill | To Skill | Trigger |
|------------|-----------|---------|
| Physical Therapy | Mental Health | Pain catastrophizing score >7/10 |
| Physical Therapy | Sleep | Night pain >4/10 consistently |
| Physical Therapy | Nutrition | Healing delayed beyond expected timeline |
| Mental Health | Physical Therapy | Physical symptoms without medical cause |
| Sleep | Physical Therapy | Daytime fatigue affecting rehab participation |
| Nutrition | Physical Therapy | Underfueling identified affecting recovery |

---

## Shared Knowledge Base

### SECOND-KNOWLEDGE-BRAIN Structure

Each skill maintains its own knowledge base but references cluster-level foundations:

**Cluster-Level (Shared):**
- Evidence hierarchy principles
- Quality assessment frameworks
- Common outcome measures

**Skill-Level (Specific):**
- Physical Therapy: Tissue healing, load management, clinical guidelines
- Mental Health: CBT frameworks, trauma-informed care, crisis protocols
- Sleep: Sleep physiology, circadian biology, sleep disorders
- Nutrition: Macro/micronutrient needs, supplementation, timing strategies
- Stress: HPA axis, allostatic load, resilience frameworks

### Knowledge Sharing Mechanisms

**Citation Format:**
```markdown
[Physical Therapy] Khan KM, 2009 - Mechanotherapy framework
[Mental Health] CBT protocols for chronic pain management
[Shared] Evidence hierarchy: Systematic Review > Meta-Analysis > RCT
```

---

## Integrated Workflow Examples

### Example 1: Chronic Low Back Pain with Comorbidities

**User Request:** "I have chronic back pain and I'm always tired and stressed."

**Integrated Workflow:**
1. **Physical Therapy skill runs:**
   - Safety gate (red flag screening)
   - Intake (pain patterns, functional limitations)
   - Scoring (chronic pain, central sensitization)
   - Roadmap (graded exposure, movement re-education)
   - **Referral triggers:** Sleep issues → Sleep skill; Stress → Stress skill

2. **Sleep skill runs:**
   - Sleep quality assessment
   - Pain-sleep interaction analysis
   - Sleep hygiene recommendations
   - Cross-reference to Physical Therapy for positioning

3. **Stress skill runs:**
   - Stress level assessment
   - Stress-pain interaction analysis
   - Resilience building recommendations
   - Cross-reference to Physical Therapy for stress-reducing movement

**Integrated Output:**
- Coordinated roadmap with priorities across domains
- Cross-referenced goals (pain reduction → better sleep → better recovery)
- Aligned timelines (graded exposure paced with stress management)

### Example 2: Post-ACL Surgery Return to Sport

**User Request:** "I'm 6 months post-ACL surgery and want to return to soccer."

**Integrated Workflow:**
1. **Physical Therapy skill runs:**
   - Safety gate (surgical complications)
   - Intake (graft type, current function, goals)
   - Scoring (recovery stage, progression readiness, psychological readiness)
   - Roadmap (objective testing, sport-specific progression)
   - **Referral triggers:** Mental Health (psychological readiness); Nutrition (fueling for return)

2. **Mental Health skill runs:**
   - ACL-RSI assessment
   - Fear of re-injury analysis
   - Psychological readiness strategies
   - Cross-reference to Physical Therapy for exposure integration

3. **Nutrition skill runs:**
   - Fueling for high-intensity training
   - Nutritional support for tissue loading
   - Recovery nutrition strategies
   - Cross-reference to Physical Therapy for training periods

**Integrated Output:**
- Coordinated return-to-sport protocol
- Mental skills integrated with physical progression
- Nutrition timing aligned with training loads

---

## Development Coordination

### Cluster Development Phases

**Phase 1 (Current):** Physical Therapy / Rehab Plan Support (active)

**Phase 2 (Next):** Mental Health & Wellness Support
- Reuse shared sub-skills
- Adapt safety screener for crisis risk
- Define mental health-specific scoring dimensions
- Create mental health knowledge base

**Phase 3:** Sleep & Recovery Optimization
- Reuse shared sub-skills
- Adapt for sleep disorder screening
- Define sleep-specific dimensions
- Create sleep knowledge base

**Phase 4:** Nutrition & Performance Fueling
- Reuse shared sub-skills
- Adapt for nutritional risk screening
- Define nutrition-specific dimensions
- Create nutrition knowledge base

**Phase 5:** Stress & Resilience Management
- Reuse shared sub-skills
- Adapt for stress crisis screening
- Define stress-specific dimensions
- Create stress knowledge base

### Coordination Mechanisms

**Shared Decision Log:** `CLUSTER-DECISIONS.md`
- Cluster-wide architectural decisions
- Shared sub-skill modifications
- Scoring scale alignment decisions
- Cross-referral protocol updates

**Integration Testing:** `tests/cluster-integration-tests.md`
- Cross-referral trigger tests
- Shared sub-skill functionality tests
- Multi-skill workflow tests
- Scoring alignment tests

---

## Cross-Skill Quality Standards

All cluster skills must meet these standards:

1. **Safety First:** Every skill has a hard gate that blocks unsafe guidance
2. **Evidence-Based:** All claims cite authoritative sources
3. **Transparent Limitations:** Scope and assumptions explicitly stated
4. **Refer Appropriately:** Cross-referral when beyond skill scope
5. **Consistent Scoring:** 0-100 scale with clear dimension definitions
6. **Prioritized Roadmaps:** Effort × impact prioritization
7. **Graceful Degradation:** Functions when external tools unavailable
8. **Devil's Advocate:** Challenges own conclusions before output

---

## Future Cluster Enhancements

**Planned Integrations:**
- Bi-directional cross-referral (automatic triggers)
- Shared patient profile (single intake for multiple needs)
- Cluster-wide outcome tracking
- Integrated dashboards (multi-domain progress visualization)

**Potential New Skills:**
- Injury Prevention & Performance
- Mindfulness & Meditation
- Chronic Disease Management
- Women's Health (pregnancy, postpartum, menopause)
- Geriatric Health & Aging

---

## Maintenance Protocol

**Weekly:**
- Run regression tests on all active skills
- Check for new evidence in shared domains
- Update knowledge bases as needed

**Monthly:**
- Review cross-referral triggers
- Evaluate shared sub-skill performance
- Coordinate development roadmap

**Quarterly:**
- Cluster-wide quality review
- Update cluster-level frameworks
- Plan next skill development phase
