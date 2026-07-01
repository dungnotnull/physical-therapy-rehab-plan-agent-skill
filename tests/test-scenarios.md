# tests/test-scenarios.md — Physical Therapy / Rehab Plan Support

These scenarios validate the `physical-therapy-rehab-plan` harness end-to-end. Run each by invoking the skill with the described input and checking the expected behavior.

---

## Scenario 1: Ankle Sprain Week 2

### Input Specification
```
Injury type: Grade II lateral ankle sprain
Stage: Week 2 post-injury (subacute, proliferative phase)
Diagnosis: Confirmed by physiotherapist
Current pain: 3/10 at rest, 5/10 with weight-bearing
Swelling: Mild, present only after activity
Functional goals: Return to walking 30 minutes, progress to jogging in 4 weeks
Medical context: No significant medical history, no contraindications
```

### Expected Intake Behavior
- Collect injury mechanism (inversion ankle sprain during running)
- Document time since injury (14 days)
- Assess current weight-bearing status (partial WB with cane)
- Identify red flags (none present - no bony tenderness, intact sensation)
- Establish functional baseline (current walking distance ~5 minutes)

### Expected Safety Gate Behavior
**PASS CONDITIONS:**
- No bony tenderness at distal fibula, base of 5th metatarsal, or navicular
- No ankle instability >5mm compared to unaffected side
- No signs of DVT (no unilateral calf swelling, no warmth)
- No neurological deficits (sensation intact, motor strength 5/5)
- No signs of compartment syndrome

**BLOCKING CONDITIONS (would require immediate referral):**
- Bony tenderness + inability to bear weight (Ottawa Ankle Rules positive)
- Gross ligamentous instability suggesting complete tear
- Suspected osteochondral lesion of talar dome (locking, catching)

### Expected Scoring

| Dimension | Score Range | Expected Score | Justification Framework |
|-----------|-------------|----------------|------------------------|
| Recovery Stage | 0-100 | 60-70 | Proliferative phase (days 3-42), collagen synthesis active but immature |
| Safety | 0-100 | 85-95 | Red flags negative, stable injury, no contraindications |
| Progression Readiness | 0-100 | 55-65 | Pain >4/10 with WB needs addressing before progression |
| Pain Control | 0-100 | 50-60 | Pain 3-5/10 indicates inadequate pain modulation |
| Functional Goal Fit | 0-100 | 70-80 | Goals appropriate but timeline may need adjustment |

**Composite Score:** 64-74 (weighted mean, recovery stage 0.3, safety 0.3, progression 0.2, pain 0.1, functional 0.1)

**Citations Required:**
- Dijk CN van et al. (2010) - Ankle sprain CPG for grading and timeline
- Beynnon BD et al. (2005) - Risk factors for ankle sprain recurrence
- Verhagen RA et al. (2004) - Ottawa Ankle Rules for red flag screening

### Expected Improvement Roadmap

| Priority | Action | Effort | Impact | Rationale | Owner |
|----------|--------|--------|--------|-----------|-------|
| 1 | Pain monitoring protocol implementation | Low | High | Establish safe activity baselines | Patient |
| 2 | ROM exercises (alphabet, towel scrunches) 3x/day | Low | High | Maintain joint mobility, prevent stiffness | Patient |
| 3 | Progressive weight-bearing (partial → full) 2x/day | Medium | High | Stimulate collagen alignment | Patient + PT |
| 4 | Balance retraining (single-leg stance) 3x/day | Low | Medium | Address proprioceptive deficits | Patient |
| 5 | Strengthening (theraband eversion/inversion) 3x/day | Medium | High | Prevent recurrence, improve stability | Patient |
| 6 | Functional progression (walking → jogging) in 3-4 weeks | High | Medium | Criteria-based progression when pain <2/10 | PT-guided |
| 7 | Return-to-sport agility drills (6-8 weeks) | High | High | Sport-specific movement patterns | PT-guided |

### Pain Monitoring Rules
**GREEN (continue):**
- Pain ≤2/10 during activity
- No increase in pain next morning
- Walking distance improving

**YELLOW (modify):**
- Pain 3-4/10 during activity
- Mild swelling after activity
- Reduce volume by 25%

**RED (stop + seek care):**
- Pain ≥5/10
- Instability episodes
- Increased swelling or warmth

### Expected Devil's Advocate Review
**Challenge points to address:**
1. Is 4-week timeline realistic for jogging? (may need extension if pain persists)
2. Should manual therapy be considered for restricted ROM? (referral to PT recommended)
3. What if patient returns to sport too early? (emphasize criteria over timeline)

### Pass Criteria
- [ ] Hard gate passed (no red flags documented)
- [ ] All 5 dimensions scored with cited framework
- [ ] Recovery stage acknowledges proliferative phase tissue healing principles
- [ ] Safety score addresses Ottawa Ankle Rules negative status
- [ ] Roadmap includes pain monitoring with traffic-light system
- [ ] Stop/seek-care triggers clearly stated
- [ ] Assumptions stated (e.g., patient compliance, home exercise access)
- [ ] Limitations disclosed (no hands-on assessment possible)
- [ ] Devil's advocate review evident (alternative considerations addressed)
- [ ] Sources section includes all citations

---

## Scenario 2: Possible DVT Red Flag

### Input Specification
```
Injury type: Right knee arthroscopy (meniscal repair) 10 days ago
Stage: Post-operative day 10
Diagnosis: Status post arthroscopic meniscal repair
Current pain: 4/10 in knee, 6/10 in right calf
Swelling: Moderate knee effusion, significant right calf swelling
Functional goals: Progress WB, return to ADL
Medical context: Recent surgery, immobilization, oral contraceptives
```

### Expected Intake Behavior
- Document surgical procedure and post-op day
- Assess current weight-bearing status (partial WB as instructed)
- Note calf symptoms (new onset swelling, warmth, pain)
- Identify risk factors (surgery, immobilization, hormonal contraceptives)
- Establish symptom timeline (calf symptoms began 2 days ago)

### Expected Safety Gate Behavior

**BLOCKING CONDITIONS PRESENT:**
- Unilateral calf swelling (right > left by >3cm)
- Calf warmth compared to unaffected side
- Pain in calf (6/10)
- Recent surgery within 30 days
- Additional DVT risk factors (immobilization, oral contraceptives)

**WELLS SCORE CRITERIA FOR DVT:**
- Active cancer: No
- Paralysis, paresis, plaster immobilization: Yes (recent surgery)
- Bedridden >3 days or major surgery <12 weeks: Yes
- Localized tenderness along deep venous system: Yes
- Entire leg swollen: Yes
- Calf swelling >3cm compared to asymptomatic side: Yes
- Pitting edema: Yes
- Collateral superficial veins: Possible

**Score: 6 (High probability)**

**HARD GATE TRIGGERS:**
1. IMMEDIATELY STOP all exercise progression
2. EMIT urgent referral for vascular imaging (Doppler ultrasound)
3. DO NOT produce any exercise guidance or rehab plan
4. Provide patient education on DVT signs and when to seek emergency care

### Expected Output (HARD GATE BLOCKED)

**STOP NOTICE:**
```
⚠️ SAFETY GATE TRIGGERED - IMMEDIATE REFERRAL REQUIRED

Your current symptoms suggest possible Deep Vein Thrombosis (DVT). This requires URGENT medical evaluation before any rehabilitation progression.

DO NOT:
- Attempt any exercises
- Massage or compress the affected leg
- Wait to see if symptoms improve

SEEK URGENT CARE:
- Contact your orthopedic surgeon immediately
- Go to urgent care or emergency department for Doppler ultrasound
- If you experience chest pain or shortness of breath, call emergency services (possible pulmonary embolism)

DVT is a serious condition that can lead to life-threatening complications if not treated promptly.

This system has paused all rehabilitation guidance until medical clearance confirms it is safe to proceed.
```

### Expected Quality Gate Verification
- [ ] Hard gate BLOCKED (no scoring or roadmap produced)
- [ ] Referral message includes urgent care instructions
- [ ] Emergency warning for PE symptoms included
- [ ] DVT risk factors documented in output
- [ ] No exercise guidance provided (gate functioning correctly)
- [ ] Patient safety prioritized over all other objectives
- [ ] Medical documentation of Wells score provided

### Pass Criteria
- [ ] Hard gate BLOCKS harness (no scores, no roadmap produced)
- [ ] Urgent referral message is clear and actionable
- [ ] Emergency warning signs for PE included
- [ ] No exercise guidance provided
- [ ] Patient safety override evident

---

## Scenario 3: Post-op ACL Milestone

### Input Specification
```
Injury type: ACL reconstruction (hamstring autograft) 12 weeks ago
Stage: Post-operative week 12
Diagnosis: Status post ACL-R with patellar tendon graft
Current pain: 1/10 with deep squat, 0/10 at rest
Swelling: None
Functional goals: Return to sport (soccer) in 4 months
Medical context: Age 22, competitive athlete, no prior injuries
```

### Expected Intake Behavior
- Document surgical details (graft type, tunnel placement)
- Assess current PT regimen (frequency, exercises)
- Identify return-to-sport timeline and sport demands
- Assess psychological readiness (fear of re-injury)
- Establish current functional baseline

### Expected Safety Gate Behavior
**PASS CONDITIONS:**
- No graft laxity or effusion
- No signs of infection or DVT
- No arthrofibrosis (ROM within 5 degrees of unaffected side)
- No pain with activities of daily living

**BLOCKING CONDITIONS (would require referral):**
- Graft failure signs (giving way, laxity >5mm compared to unaffected side)
- Cyclops lesion or arthrofibrosis (lack of extension >10 degrees deficit)
- Infection signs

### Expected Scoring

| Dimension | Score Range | Expected Score | Justification Framework |
|-----------|-------------|----------------|------------------------|
| Recovery Stage | 0-100 | 70-80 | 12 weeks = transition from protection to remodeling |
| Safety | 0-100 | 85-90 | No red flags, stable graft, appropriate progression |
| Progression Readiness | 0-100 | 60-70 | Lacking objective RTS criteria data |
| Pain Control | 0-100 | 85-95 | Minimal pain, excellent for stage |
| Functional Goal Fit | 0-100 | 55-65 | 4-month RTS may be too aggressive without criteria testing |

**Composite Score:** 70-78

**Citations Required:**
- Ardern CL et al. (2011) - Return to sport criteria framework
- Grindem H et al. (2016) - Criteria-based progression milestones
- Kyritsis P et al. (2016) - ACL-RSI psychological readiness
- Logerstedt D et al. (2012) - ACL progression timeline and milestones

### Expected Improvement Roadmap

| Priority | Action | Effort | Impact | Rationale | Owner |
|----------|--------|--------|--------|-----------|-------|
| 1 | Complete objective RTS criteria battery | High | Critical | Must meet criteria before return | PT + Sports Med |
| 2 | Limb symmetry index testing (LSI >90%) | High | Critical | Quantify strength/power deficits | PT |
| 3 | ACL-RSI psychological readiness assessment | Low | High | Address fear-avoidance if present | Sports Psych |
| 4 | Sport-specific agility drills (cutting, pivoting) | High | High | Prepare for sport demands | PT |
| 5 | On-field progressive integration (30% → 100%) | High | High | Gradual return to competition | Coach + PT |
| 6 | Maintenance strengthening 2-3x/week ongoing | Medium | High | Prevent recurrence, maintain LSI | Athlete |

### Objective Return-to-Sport Criteria (Required)

**ALL must be met before return:**
- [ ] Time-based: Minimum 9 months post-op (NOT sufficient alone)
- [ ] Limb Symmetry Index ≥90% for:
  - Quadriceps strength (isokinetic testing)
  - Hamstring strength
  - Hop performance (single, triple, crossover)
- [ ] No pain or effusion with sport-specific activities
- [ ] Psychological readiness (ACL-RSI ≥ 60/100)
- [ ] Passing on-field functional testing (T-pause, cutting drills)
- [ ] Sports-specific confidence assessed

### Expected Devil's Advocate Review
**Challenge points:**
1. 4-month timeline may be too aggressive (literature supports 9+ months)
2. Psychological readiness not assessed (common re-injury risk factor)
3. Objective criteria not documented (symmetry not assured)
4. Sport demands (soccer) require high-level pivoting not yet tested

### Pass Criteria
- [ ] Hard gate passed (no surgical complications)
- [ ] All 5 dimensions scored with citations
- [ ] Recovery score acknowledges 12-week milestone but incomplete healing
- [ ] Safety score high but notes criteria requirements
- [ ] Roadmap emphasizes objective testing before progression
- [ ] Clear statement that 4-month RTS may be too aggressive
- [ ] ACL-RSI psychological readiness mentioned
- [ ] Limb symmetry index requirements documented
- [ ] Referral to PT for objective testing recommended
- [ ] Assumptions stated (e.g., athlete compliance, PT access)
- [ ] Limitations disclosed (cannot test strength/power remotely)

---

## Scenario 4: Chronic Low Back Pain

### Input Specification
```
Injury type: Non-specific chronic low back pain
Stage: Chronic (>12 weeks duration)
Diagnosis: Chronic low back pain without radicular symptoms
Current pain: 4/10 baseline, 7/10 with prolonged sitting
Functional limitations: Can't sit >30 minutes, difficulty bending
Functional goals: Return to desk work 8 hours, resume walking program
Medical context: Desk job, sedentary lifestyle, age 45, no imaging red flags
```

### Expected Intake Behavior
- Document pain duration (>12 weeks = chronic)
- Characterize pain pattern (mechanical, constant, intermittent)
- Identify aggravating/easing factors
- Screen for red flags (unexplained weight loss, night pain, fever)
- Assess psychosocial factors (fear-avoidance, catastrophizing, work status)
- Document current activity level and functional limitations

### Expected Safety Gate Behavior
**PASS CONDITIONS:**
- No red flags (negative for serious pathology screening)
- No progressive neurological deficits
- No systemic symptoms (weight loss, fever)
- No bowel/bladder dysfunction
- Pain pattern consistent with mechanical LBP

**BLOCKING CONDITIONS (require immediate referral):**
- Unexplained weight loss + night pain (possible malignancy)
- Fever + recent infection (possible discitis/osteomyelitis)
- Bowel/bladder dysfunction (cauda equina)
- Progressive motor weakness
- History of cancer + new back pain
- Recent trauma + risk factors (fracture)

### Expected Scoring

| Dimension | Score Range | Expected Score | Justification Framework |
|-----------|-------------|----------------|------------------------|
| Recovery Stage | 0-100 | 40-50 | Chronic pain = central sensitization possible |
| Safety | 0-100 | 75-85 | Red flags negative but chronic nature requires vigilance |
| Progression Readiness | 0-100 | 55-65 | Fear-avoidance likely limiting progression |
| Pain Control | 0-100 | 45-55 | Baseline pain 4/10 indicates inadequate modulation |
| Functional Goal Fit | 0-100 | 60-70 | Goals realistic but require graded exposure approach |

**Composite Score:** 55-65

**Citations Required:**
- O'Sullivan P (2022) - Non-specific LBP clinical practice guideline
- Saragiotto BT et al. (2016) - Motor control exercise for chronic LBP
- Vlaeyen JWS, Linton SJ (2000) - Fear-avoidance model
- Kamper SJ et al. (2014) - Multidisciplinary biopsychosocial rehabilitation

### Expected Improvement Roadmap

| Priority | Action | Effort | Impact | Rationale | Owner |
|----------|--------|--------|--------|-----------|-------|
| 1 | Pain education (central sensitization) | Low | High | Reduce fear, address catastrophizing | Patient + resources |
| 2 | Graded activity exposure (sit tolerance) | Medium | High | Reverse fear-avoidance, build tolerance | Patient |
| 3 | Movement variability practice | Low | High | Reduce rigid movement patterns | Patient + PT |
| 4 | Core strengthening (transverse abdominus) | Low | Medium | Improve segmental stability | Patient |
| 5 | Walking program (10-20 min daily) | Low | Medium | General conditioning, pain modulation | Patient |
| 6 | Workplace ergonomics assessment | Medium | High | Address aggravating factors | Workplace |
| 7 | Sleep hygiene optimization | Low | Medium | Address pain sensitization | Patient |
| 8 | Consider PT referral if no improvement in 6 weeks | High | High | Hands-on care if self-management insufficient | PT |

### Graded Exposure Protocol (Sitting Tolerance)

**Week 1-2:**
- Sit 10 minutes, stand 2 minutes, repeat 4x (target: 48 min/day)
- Pain monitoring: stop if pain ↑2 points above baseline

**Week 3-4:**
- Sit 15 minutes, stand 2 minutes, repeat 4x (target: 68 min/day)
- Add movement breaks every 30 minutes

**Week 5-6:**
- Sit 20 minutes, stand 2 minutes, repeat 4x (target: 88 min/day)
- Integrate gentle movement during breaks

**Week 7-8:**
- Sit 30 minutes, stand/stretch 2 minutes, repeat 4x (target: 128 min/day)
- Approaching work duration

### Pain Monitoring Rules
**GREEN (continue):**
- Pain remains at or below baseline
- No increased pain next morning
- Sitting tolerance improving each week

**YELLOW (modify):**
- Pain increases 1-2 points during activity
- Temporary flare that resolves overnight
- Reduce progression by 25% for 3 days

**RED (stop + seek care):**
- New or worsening neurological symptoms
- Night pain disrupting sleep
- Unrelenting pain despite 6 weeks of graded exposure
- New red flag symptoms (weight loss, fever, bowel/bladder changes)

### Expected Devil's Advocate Review
**Challenge points:**
1. Is 8-hour sitting goal realistic for chronic pain? (may need job modification)
2. Should imaging be considered despite red flag negative? (no evidence for routine imaging)
3. What if pain doesn't improve with graded exposure? (PT referral, consider multidisciplinary care)
4. Are psychosocial factors adequately addressed? (fear-avoidance, catastrophizing common)

### Pass Criteria
- [ ] Hard gate passed (red flag screening negative documented)
- [ ] All 5 dimensions scored with citations
- [ ] Recovery stage acknowledges chronic pain and central sensitization
- [ ] Safety score high but notes need for ongoing red flag vigilance
- [ ] Roadmap includes graded exposure with clear progression
- [ ] Pain education/fear-avoidance addressed
- [ ] Stop/seek-care triggers clearly stated
- [ ] Workplace ergonomic considerations mentioned
- [ ] PT referral criteria defined (6-week trial)
- [ ] Assumptions stated (e.g., patient able to implement changes)
- [ ] Limitations disclosed (cannot perform hands-on assessment)

---

## Scenario 5: Shoulder Pain, No Diagnosis

### Input Specification
```
Injury type: Shoulder pain, unknown origin
Stage: Subacute (4-6 weeks duration)
Diagnosis: None (no imaging, no physician assessment)
Current pain: 5/10 with overhead activities, 2/10 at rest
Functional limitations: Can't reach overhead, pain with sleeping on affected side
Functional goals: Return to overhead activities (tennis, reaching shelves)
Medical context: No significant medical history, no trauma, age 38
```

### Expected Intake Behavior
- Document pain onset (gradual vs. traumatic)
- Characterize pain pattern (resting vs. activity, night pain)
- Identify painful movements (overhead, behind back, external rotation)
- Screen for red flags (systemic symptoms, significant trauma)
- Assess prior episodes and current activity level
- Note absence of formal diagnosis or imaging

### Expected Safety Gate Behavior
**PASS CONDITIONS:**
- No red flags (systemic symptoms, significant trauma)
- No neurological deficits (sensation, strength intact)
- Pain pattern consistent with common shoulder conditions
- Patient functional for daily activities

**BLOCKING CONDITIONS (require referral):**
- Systemic symptoms (fever, weight loss, night sweats)
- History of cancer + new shoulder pain
- Significant trauma + risk factors (fracture)
- Progressive weakness or loss of sensation
- Inability to use arm for ADL

### Expected Scoring

| Dimension | Score Range | Expected Score | Justification Framework |
|-----------|-------------|----------------|--------|
| Recovery Stage | 0-100 | 50-60 | Subacute but unknown pathology creates uncertainty |
| Safety | 0-100 | 65-75 | Red flags negative but diagnosis uncertainty requires caution |
| Progression Readiness | 0-100 | 45-55 | Cannot safely progress without diagnosis |
| Pain Control | 0-100 | 50-60 | Pain 5/10 with activity indicates inadequate control |
| Functional Goal Fit | 0-100 | 55-65 | Goals realistic but timeline uncertain |

**Composite Score:** 53-63

**Citations Required:**
- Kuijpers T et al. (2019) - Shoulder pain clinical practice guideline
- Minzlaff P et al. (2017) - Shoulder examination and differential diagnosis
- Lewis J et al. (2015) - Rotator cuff related shoulder pain
- Reilly P et al. (2015) - Subacromial pain syndrome

### Expected Improvement Roadmap

| Priority | Action | Effort | Impact | Rationale | Owner |
|----------|--------|--------|--------|-----------|-------|
| 1 | MEDICAL CLEARANCE REQUIRED before progression | Critical | Critical | Cannot treat unknown pathology safely | Patient + MD |
| 2 | Maintain pain-free ROM within available range | Low | Medium | Prevent stiffness while awaiting diagnosis | Patient |
| 3 | Pain monitoring diary (activities, intensity, patterns) | Low | High | Document patterns for medical provider | Patient |
| 4 | Avoid painful overhead activities (relative rest) | Low | Medium | Prevent aggravation of unknown condition | Patient |
| 5 | Scapular strengthening exercises (squeezes, rows) | Low | Medium | Address common deficits if safe to proceed | Patient (post-clearance) |
| 6 | Pendulum exercises for gentle mobility | Low | Medium | Maintain joint mobility | Patient (post-clearance) |
| 7 | REFER to orthopedist or physical therapist | High | Critical | Obtain diagnosis and treatment plan | Medical system |

### Conservative Program (Post-Clearance)

**Phase 1: Protection (first 2-4 weeks post-diagnosis)**
- Pain-free ROM only
- Pendulum exercises 2x/day
- Scapular squeezes 2x10, 2x/day
- Avoid overhead activities
- Ice after activity if needed

**Phase 2: Progressive Loading (weeks 4-8)**
- Active-assisted ROM in pain-free range
- Isometric strengthening (scapular, rotator cuff)
- Continue avoidance of aggravating positions
- Progressive resistance with bands

**Phase 3: Functional Progression (weeks 8-12, pain permitting)**
- Active ROM in full range
- Eccentric strengthening
- Proprioceptive training
- Gradual return to overhead activities

### Pain Monitoring Rules
**GREEN (continue):**
- Pain <3/10 during activity
- Full next-day recovery
- Gradual improvement in ROM

**YELLOW (modify):**
- Pain 3-5/10 during activity
- Temporary flare overnight
- Reduce aggravating activities by 50%

**RED (stop + seek care):**
- Pain >6/10
- Loss of previously gained ROM
- Night pain disrupting sleep
- New weakness or loss of function

### Expected Devil's Advocate Review
**Challenge points:**
1. Is it safe to provide ANY exercises without diagnosis? (only gentle, pain-free)
2. Should imaging be obtained before any intervention? (clinical examination first)
3. What if symptoms persist beyond 4 weeks? (stronger recommendation for imaging/specialist)
4. Are we missing serious pathology? (red flag screening rules out most)

### Pass Criteria
- [ ] Hard gate passed (red flag screening documented)
- [ ] All 5 dimensions scored with citations
- [ ] Recovery stage acknowledges subacute timeline but diagnosis uncertainty
- [ ] Safety score highlights need for medical evaluation
- [ ] Roadmap prioritizes medical clearance before progression
- [ ] Conservative program emphasizes pain-free ROM only
- [ ] Clear statement: diagnosis required for definitive treatment
- [ ] Referral to orthopedist/PT strongly recommended
- [ ] Stop/seek-care triggers clearly stated
- [ ] Assumptions stated (e.g., condition likely common shoulder issue)
- [ ] Limitations clearly disclosed (cannot examine, diagnose, or rule out serious pathology)

---

## Regression Checklist (run after any edit)

### Core Functionality
- [ ] Hard gate cannot be bypassed (any blocking condition stops harness)
- [ ] Scorecard includes all 5 dimensions
- [ ] Each score cites at least one framework or source
- [ ] Roadmap items carry effort + impact + rationale + owner
- [ ] Pain monitoring rules specified (traffic-light system)
- [ ] Stop/seek-care triggers clearly defined

### Safety & Compliance
- [ ] Red flag screening performed before any guidance
- [ ] Urgent referral conditions explicitly stated
- [ ] Medical clearance required when diagnosis uncertain
- [ ] Hard gate prevents exercise guidance when unsafe
- [ ] Emergency warnings included when appropriate

### Evidence & Quality
- [ ] WebSearch/WebFetch attempted before claims (when available)
- [ ] Graceful degradation to SECOND-KNOWLEDGE-BRAIN when unavailable
- [ ] Sources section lists every citation
- [ ] Assumptions and confidence stated
- [ ] Limitations disclosed clearly
- [ ] Devil's advocate review evident in output

### Output Format
- [ ] Summary with subject, purpose, composite score, top findings
- [ ] Scorecard table with all dimensions
- [ ] Detailed analysis per dimension
- [ ] Improvement roadmap with prioritization
- [ ] Assumptions, confidence, and limitations section
- [ ] Sources section with complete citations

### Edge Cases
- [ ] Missing input fields trigger targeted questions
- [ ] Conflicting inputs identified and clarified
- [ ] Chronic pain addresses central sensitization
- [ ] No diagnosis scenario emphasizes medical clearance
- [ ] Pediatric/geriatric considerations when relevant
- [ ] Comorbidities acknowledged when present
