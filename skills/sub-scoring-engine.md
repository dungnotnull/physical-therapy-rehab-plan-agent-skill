---
name: physical-therapy-rehab-plan-sub-scoring-engine
description: Score recovery stage, safety, and progression readiness against healing-phase and CPG criteria.
---

## Role
Sub-skill of `physical-therapy-rehab-plan` (Physical Therapy / Rehab Plan Support). Acts as the **stage**.

## Purpose
Score recovery stage, safety, and progression readiness against healing-phase and CPG criteria.

## Inputs
- The user request and any artifacts supplied.
- Structured output from the previous harness stage.

## Procedure
1. Validate that required inputs are present; request missing items.
2. Apply the relevant framework(s): Tissue-healing phases (inflammatory/proliferative/remodeling), Progressive overload & graded exposure, Clinical practice guidelines (APTA, JOSPT), Red-flag screening (serious pathology).
3. Produce a structured, schema-valid payload for the next stage.
4. Record assumptions and confidence.

## Outputs
- A structured payload (JSON-like) consumed by the next stage.

## Quality Gate
- [ ] Inputs validated
- [ ] Framework applied and cited
- [ ] Output schema valid and complete
