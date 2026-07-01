---
name: physical-therapy-rehab-plan-sub-safety-screener
description: Screen for red flags (fracture, infection, DVT, neuro deficits) and gate referral before any exercise guidance.
---

## Role
Sub-skill of `physical-therapy-rehab-plan` (Physical Therapy / Rehab Plan Support). Acts as the **safety/risk/compliance HARD GATE**.

## Purpose
Screen for red flags (fracture, infection, DVT, neuro deficits) and gate referral before any exercise guidance.

## Inputs
- The user request and any artifacts supplied.
- Structured output from the previous harness stage.

## Procedure
1. Validate that required inputs are present; request missing items.
2. Apply the relevant framework(s): Tissue-healing phases (inflammatory/proliferative/remodeling), Progressive overload & graded exposure, Clinical practice guidelines (APTA, JOSPT), Red-flag screening (serious pathology).
3. Evaluate blocking conditions and decide pass/refer.
4. Record assumptions and confidence.

## Gate Behavior (BLOCKING)
This sub-skill is a HARD GATE. If any blocking condition is detected:
1. STOP the harness immediately.
2. Do NOT produce scores, plans, or optimizations.
3. Emit the appropriate referral / disclaimer / support resource.
4. Only allow the harness to continue when all blocking conditions are clear.

## Outputs
- A structured payload (JSON-like) consumed by the next stage, plus a pass/refer verdict.

## Quality Gate
- [ ] Inputs validated
- [ ] Framework applied and cited
- [ ] Blocking conditions explicitly checked
