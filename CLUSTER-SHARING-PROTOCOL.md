# CLUSTER-SHARING-PROTOCOL.md — Health, Wellness & Psychology Cluster

Protocol for sharing sub-skills, frameworks, and resources across the Health, Wellness & Psychology cluster.

---

## Purpose

This document defines the protocol for sharing common functionality (sub-skills, scoring frameworks, knowledge bases) across sibling skills in the Health, Wellness & Psychology cluster to ensure:
- Consistency in user experience
- Reduced duplication and maintenance burden
- Aligned quality standards
- Cross-skill interoperability

---

## Shared Resources Inventory

### Sub-Skills Available for Sharing

| Sub-Skill | Purpose | Input Schema | Output Schema | Quality Gates | Status |
|-----------|---------|--------------|----------------|---------------|--------|
| `sub-profile-intake` | Capture condition, stage, diagnosis, goals, context | User request + any artifacts | Structured intake payload | Input validation, schema compliance | **Available for sharing** |
| `sub-safety-screener` | Screen for red flags, risk factors, contraindications | Intake payload | Pass/refer verdict | Blocking conditions checked | **Available for sharing** |
| `sub-scoring-engine` | Multi-dimensional scoring against frameworks | Gate-passed payload | Scorecard (0-100 per dimension) | All dimensions scored, cited | **Available for sharing** |
| `sub-improvement-roadmap` | Prioritized improvement plan | Scorecard + context | Roadmap (effort × impact) | All items have effort/impact/owner | **Available for sharing** |

### Shared Frameworks

| Framework | Domain | Applicable Skills | Reference Location |
|-----------|--------|-------------------|-------------------|
| Evidence hierarchy | All skills | All cluster skills | `SECOND-KNOWLEDGE-BRAIN.md` (shared section) |
| Red flag screening principles | Safety-critical | Physical Therapy, Mental Health, Sleep | `SECOND-KNOWLEDGE-BRAIN.md` |
| 0-100 scoring model | All skills | All cluster skills | `CLUSTER-INTEGRATION.md` |
| Effort × impact prioritization | Planning | All cluster skills | `CLUSTER-INTEGRATION.md` |
| Pain monitoring (traffic-light) | Physical, Mental Health | Physical Therapy, Mental Health | `SECOND-KNOWLEDGE-BRAIN.md` |

---

## Sharing Protocol Steps

### For a Skill Wishing to Use Shared Sub-Skills

**Step 1: Verify Compatibility**
- Confirm the sub-skills meet your domain requirements
- Identify any domain-specific extensions needed
- Document custom dimensions or criteria

**Step 2: Reference in Main Skill File**
Add to your skill's `main.md`:
```markdown
## Sub-skills Available
- `shared/sub-profile-intake` — Capture [domain-specific] condition, stage, goals, context
- `shared/sub-safety-screener` — Screen for [domain-specific] red flags and risks
- `shared/sub-scoring-engine` — Score against [domain-specific] frameworks
- `shared/sub-improvement-roadmap` — Build prioritized [domain-specific] roadmap
```

**Step 3: Extend for Domain Specificity**
Create domain-specific extensions in your skill directory:
```
your-skill/
├── main.md
├── extensions/
│   ├── intake-extension.md      # Domain-specific intake fields
│   ├── safety-extension.md      # Domain-specific red flags
│   ├── scoring-extension.md     # Domain-specific dimensions
│   └── roadmap-extension.md     # Domain-specific roadmap items
```

**Step 4: Implement Main Harness**
Wire the shared sub-skills together with your extensions:
```markdown
## Workflow
1. Intake (shared + extensions)
2. Safety Gate (shared + extensions)
3. Evidence gathering (domain-specific)
4. Scoring (shared framework + domain criteria)
5. Roadmap (shared + extensions)
6. Quality gate (shared devil's advocate)
```

**Step 5: Document Deviations**
In your skill's `CLAUDE.md` or main file:
```markdown
## Cluster Shared Components
This skill uses shared sub-skills from the Health, Wellness & Psychology cluster:
- Intake: Uses shared pattern with [X] domain-specific extensions
- Safety: Uses shared gate with [Y] domain-specific blocking conditions
- Scoring: Uses shared 0-100 scale with [Z] domain-specific dimensions
- Roadmap: Uses shared prioritization with [W] domain-specific items
```

---

## Extension Guidelines

### Intake Extensions

**When to extend:**
- Domain-specific fields required (e.g., psychological history for mental health)
- Specialized assessment tools needed (e.g., ACL-RSI for ACL rehab)

**How to extend:**
- Keep shared intake fields (condition, stage, goals, context)
- Add domain-specific fields in extension
- Document validation requirements

### Safety Gate Extensions

**When to extend:**
- Domain-specific red flags (e.g., suicidal ideation for mental health)
- Specialized contraindications (e.g., sleep disorders affecting rehab)

**How to extend:**
- Keep shared safety principles (screen for serious pathology)
- Add domain-specific blocking conditions in extension
- Maintain HARD GATE behavior

### Scoring Extensions

**When to extend:**
- Domain-specific dimensions required (e.g., sleep quality for sleep skill)
- Specialized frameworks needed (e.g., tissue healing phases for PT)

**How to extend:**
- Keep shared dimensions (Safety, Progression Readiness, Goal Fit) where applicable
- Add domain-specific dimensions
- Use shared 0-100 scale
- Cite domain-specific frameworks

### Roadmap Extensions

**When to extend:**
- Domain-specific roadmap items required (e.g., sleep hygiene for sleep skill)
- Specialized protocols needed (e.g., graded exposure for chronic pain)

**How to extend:**
- Keep shared structure (Priority, Action, Effort, Impact, Rationale, Owner)
- Add domain-specific protocols
- Use shared prioritization principles

---

## Quality Assurance for Shared Components

### Testing Requirements

Before releasing a skill that uses shared sub-skills:

1. **Shared Sub-Skill Functionality Tests:**
   - Verify all shared sub-skills function correctly in your domain
   - Test edge cases specific to your domain
   - Verify integration with your extensions

2. **Cross-Domain Consistency Tests:**
   - Verify output format matches cluster standards
   - Verify scoring scale aligns with cluster expectations
   - Verify roadmap structure matches cluster format

3. **Regression Tests:**
   - Run all cluster regression tests
   - Run skill-specific regression tests
   - Document any deviations and rationale

### Documentation Requirements

Each skill using shared components must document:

1. **Which shared components are used**
2. **How they are extended for the domain**
3. **Any deviations from shared standards**
4. **Rationale for domain-specific choices**

---

## Version Control and Updates

### Shared Sub-Skill Updates

When a shared sub-skill is updated:

1. **Update the shared file** in the shared location
2. **Version the change** with a clear commit message
3. **Notify all dependent skills** of the update
4. **Test each dependent skill** for compatibility
5. **Update cluster documentation** if standards change

### Dependent Skill Updates

When updating a skill that uses shared sub-skills:

1. **Check for shared sub-skill updates** before releasing
2. **Test against latest shared versions**
3. **Update extension compatibility** if needed
4. **Document any breaking changes**
5. **Notify cluster maintainers** of significant changes

---

## Conflict Resolution

### When Shared Sub-Skills Don't Fit a Domain

**Options:**
1. **Extend** - Add domain-specific functionality via extensions (preferred)
2. **Adapt** - Modify shared sub-skill with cluster consensus
3. **Create domain-specific** - Only if shared approach fundamentally incompatible

**Decision Process:**
1. Document why shared sub-skill doesn't fit
2. Propose extension or modification
3. Get cluster consensus for modifications
4. Document rationale for domain-specific approach

---

## Cluster Coordination

### Cluster Maintainer Responsibilities

- Maintain shared sub-skill files
- Coordinate cross-skill testing
- Facilitate conflict resolution
- Document cluster standards
- Review new skill proposals for compatibility

### Skill Developer Responsibilities

- Use shared components where applicable
- Document extensions and deviations
- Participate in cluster coordination
- Test cross-skill compatibility
- Propose improvements to shared components

### Communication Channels

- **Cluster decisions:** `CLUSTER-DECISIONS.md`
- **Integration issues:** GitHub issues tagged `cluster-integration`
- **Feature proposals:** GitHub issues tagged `cluster-proposal`
- **Testing coordination:** Cluster testing sync meetings

---

## Example: Mental Health Skill Using Shared Components

```markdown
## Sub-skills Available
- `shared/sub-profile-intake` — Capture mental health condition, stage, diagnosis, symptoms, goals, context
  - Extension: Psychiatric history, current medications, crisis indicators
- `shared/sub-safety-screener` — Screen for red flags (suicidal ideation, psychosis, abuse)
  - Extension: Crisis risk assessment, safety planning
- `shared/sub-scoring-engine` — Score against mental health frameworks (symptom severity, functional impairment, stability)
  - Extension: Symptom-specific dimensions (depression, anxiety, mania)
- `shared/sub-improvement-roadmap` — Build prioritized mental health roadmap (effort × impact)
  - Extension: Therapy homework, coping strategies, crisis plan

## Workflow
1. Intake (shared pattern + psychiatric history extension)
2. Safety Gate (shared HARD GATE + crisis risk extension)
3. Evidence gathering (clinical practice guidelines, CBT frameworks)
4. Scoring (shared 0-100 scale + mental health dimensions)
5. Roadmap (shared prioritization + mental health interventions)
6. Quality gate (shared devil's advocate + mental health considerations)
```

---

## Compliance Checklist

For each new skill using shared components:

- [ ] Reviewed all available shared sub-skills
- [ ] Verified compatibility with domain requirements
- [ ] Documented extensions and deviations
- [ ] Implemented main harness referencing shared components
- [ ] Tested all shared sub-skill functionality
- [ ] Run cross-domain consistency tests
- [ ] Documented rationale for any domain-specific choices
- [ ] Committed to cluster coordination and updates
- [ ] Updated cluster documentation if standards changed
- [ ] Notified cluster maintainers of new skill
