# Annotator Worksheet — Held-Out Validation Set (n=50)

Second, separate batch — different scenarios from the first 50. Read the protocol
text, amendment text, and current text of the context sections below for each
scenario. Do not consult any system output or the first worksheet. For each
scenario, list impacted section codes from the fixed scheme and governing
references from the fixed pool. Context sections provide inspectable current
text for common downstream targets, but the allowed section codes are the full
scheme below.

## Section scheme (choose from these codes only)

- `4.1` — Study Population / Key Inclusion Criteria
- `4.2` — Key Exclusion Criteria
- `5.1` — Study Design Overview
- `5.2` — Dosing and Administration
- `5.3` — Dose Modification Rules
- `6.1` — Concomitant Medications
- `6.2` — Prohibited Medications
- `7.1` — Efficacy Endpoints
- `7.2` — Endpoint Assessment Schedule
- `8.1` — Visit Schedule / Schedule of Assessments
- `8.2` — Procedures at Each Visit
- `9.1` — Informed Consent Process
- `9.2` — Assent / Re-consent Requirements
- `10.1` — Discontinuation Criteria
- `10.2` — Withdrawal Procedures
- `11.1` — Adverse Event Definitions
- `11.2` — Serious Adverse Event Reporting
- `11.3` — Safety Monitoring Plan
- `11.4` — Data Safety Monitoring Board Review
- `11.5` — Stopping Rules
- `12.1` — Statistical Analysis Plan

## Governing reference pool (choose from these only)

- **FDA** — 21 CFR 312.30 (IND protocol amendment reporting requirement)
- **FDA** — 21 CFR 312.32 (IND safety reporting requirement)
- **EMA** — EMA GCP Q&A Section 3 (substantial amendment definition and notification)
- **EMA** — EMA GCP Q&A Section 5 (informed consent re-consent requirement)
- **ICH** — ICH E6(R2) Section 4.5 (protocol deviation and amendment handling)
- **Internal SOP** — SOP-DoseChange-01 (dose-change citation and cross-reference requirement)
- **Internal SOP** — SOP-SafetyMonitoring-02 (safety monitoring plan update requirement)
- **Internal SOP** — SOP-Eligibility-03 (eligibility criteria change sign-off requirement)

---

## heldout_001 — dose_change — H-NEP-200 (Nephrology)

**Previous protocol text (Section being amended):** Protocol H-NEP-200, Version 1: Subjects with IgA nephropathy receive the investigational compound at 10 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-NEP-200, Amendment 2: Section 5.2 is revised. The dose is changed from 10 mg once daily to 80 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 10 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with IgA nephropathy at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (10 mg once daily to 80 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 80 mg once daily as the current dose and keep 10 mg once daily as the prior protocol state.

---

## heldout_002 — eligibility_change — H-HEP-201 (Hepatology)

**Previous protocol text (Section being amended):** Protocol H-HEP-201, Version 1: Subjects with non-alcoholic steatohepatitis and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-HEP-201, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 20 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with non-alcoholic steatohepatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_003 — visit_schedule_change — H-HEM-202 (Hematology)

**Previous protocol text (Section being amended):** Protocol H-HEM-202, Version 1: Subjects with sickle cell disease attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-HEM-202, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 40 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with sickle cell disease at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_004 — safety_monitoring_change — H-OPH-203 (Ophthalmology)

**Previous protocol text (Section being amended):** Protocol H-OPH-203, Version 1: Safety monitoring for the study drug includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-OPH-203, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 80 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with diabetic macular edema at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_005 — endpoint_change — H-GAS-204 (Gastroenterology)

**Previous protocol text (Section being amended):** Protocol H-GAS-204, Version 1: The primary efficacy endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52.

**Amendment text:** Protocol H-GAS-204, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 120 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_006 — informed_consent_change — H-URO-205 (Urology)

**Previous protocol text (Section being amended):** Protocol H-URO-205, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-URO-205, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 160 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with overactive bladder at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_007 — discontinuation_criteria_change — H-ALL-206 (Allergy/Immunology)

**Previous protocol text (Section being amended):** Protocol H-ALL-206, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-ALL-206, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 240 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic spontaneous urticaria at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_008 — drug_interaction_change — H-ORT-207 (Orthopedics)

**Previous protocol text (Section being amended):** Protocol H-ORT-207, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-ORT-207, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the investigational analgesic.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational analgesic is administered at 10 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational analgesic are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational analgesic.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with post-surgical pain at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational analgesic for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_009 — dose_change — H-END-208 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol H-END-208, Version 1: Subjects with obesity with weight-related comorbidity receive the investigational agent at 20 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-END-208, Amendment 2: Section 5.2 is revised. The dose is changed from 20 mg once daily to 120 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 20 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with obesity with weight-related comorbidity at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (20 mg once daily to 120 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 120 mg once daily as the current dose and keep 20 mg once daily as the prior protocol state.

---

## heldout_010 — eligibility_change — H-PUL-209 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol H-PUL-209, Version 1: Subjects with severe eosinophilic asthma and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-PUL-209, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 40 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with severe eosinophilic asthma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_011 — visit_schedule_change — H-CAR-210 (Cardiology)

**Previous protocol text (Section being amended):** Protocol H-CAR-210, Version 1: Subjects with resistant hypertension attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-CAR-210, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 80 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with resistant hypertension at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_012 — safety_monitoring_change — H-ONC-211 (Oncology)

**Previous protocol text (Section being amended):** Protocol H-ONC-211, Version 1: Safety monitoring for the investigational therapy includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-ONC-211, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 120 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with relapsed/refractory multiple myeloma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_013 — endpoint_change — H-NEU-212 (Neurology)

**Previous protocol text (Section being amended):** Protocol H-NEU-212, Version 1: The primary efficacy endpoint is clinical remission in subjects with chronic migraine at Week 52.

**Amendment text:** Protocol H-NEU-212, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 160 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic migraine at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_014 — informed_consent_change — H-RHE-213 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol H-RHE-213, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-RHE-213, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 240 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with active psoriatic arthritis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_015 — discontinuation_criteria_change — H-INF-214 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol H-INF-214, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-INF-214, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antimicrobial agent is administered at 10 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the antimicrobial agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the antimicrobial agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with complicated urinary tract infection at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antimicrobial agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_016 — drug_interaction_change — H-DER-215 (Dermatology)

**Previous protocol text (Section being amended):** Protocol H-DER-215, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-DER-215, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the study agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 20 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe atopic dermatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_017 — dose_change — H-NEP-216 (Nephrology)

**Previous protocol text (Section being amended):** Protocol H-NEP-216, Version 1: Subjects with IgA nephropathy receive the investigational compound at 40 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-NEP-216, Amendment 2: Section 5.2 is revised. The dose is changed from 40 mg once daily to 160 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 40 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with IgA nephropathy at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (40 mg once daily to 160 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 160 mg once daily as the current dose and keep 40 mg once daily as the prior protocol state.

---

## heldout_018 — eligibility_change — H-HEP-217 (Hepatology)

**Previous protocol text (Section being amended):** Protocol H-HEP-217, Version 1: Subjects with non-alcoholic steatohepatitis and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-HEP-217, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 80 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with non-alcoholic steatohepatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_019 — visit_schedule_change — H-HEM-218 (Hematology)

**Previous protocol text (Section being amended):** Protocol H-HEM-218, Version 1: Subjects with sickle cell disease attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-HEM-218, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 120 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with sickle cell disease at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_020 — safety_monitoring_change — H-OPH-219 (Ophthalmology)

**Previous protocol text (Section being amended):** Protocol H-OPH-219, Version 1: Safety monitoring for the study drug includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-OPH-219, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 160 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with diabetic macular edema at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_021 — endpoint_change — H-GAS-220 (Gastroenterology)

**Previous protocol text (Section being amended):** Protocol H-GAS-220, Version 1: The primary efficacy endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52.

**Amendment text:** Protocol H-GAS-220, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 240 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_022 — informed_consent_change — H-URO-221 (Urology)

**Previous protocol text (Section being amended):** Protocol H-URO-221, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-URO-221, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 10 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with overactive bladder at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_023 — discontinuation_criteria_change — H-ALL-222 (Allergy/Immunology)

**Previous protocol text (Section being amended):** Protocol H-ALL-222, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-ALL-222, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 20 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic spontaneous urticaria at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_024 — drug_interaction_change — H-ORT-223 (Orthopedics)

**Previous protocol text (Section being amended):** Protocol H-ORT-223, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-ORT-223, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the investigational analgesic.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational analgesic is administered at 40 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational analgesic are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational analgesic.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with post-surgical pain at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational analgesic for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_025 — dose_change — H-END-224 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol H-END-224, Version 1: Subjects with obesity with weight-related comorbidity receive the investigational agent at 80 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-END-224, Amendment 2: Section 5.2 is revised. The dose is changed from 80 mg once daily to 240 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 80 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with obesity with weight-related comorbidity at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (80 mg once daily to 240 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 240 mg once daily as the current dose and keep 80 mg once daily as the prior protocol state.

---

## heldout_026 — eligibility_change — H-PUL-225 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol H-PUL-225, Version 1: Subjects with severe eosinophilic asthma and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-PUL-225, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 120 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with severe eosinophilic asthma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_027 — visit_schedule_change — H-CAR-226 (Cardiology)

**Previous protocol text (Section being amended):** Protocol H-CAR-226, Version 1: Subjects with resistant hypertension attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-CAR-226, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 160 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with resistant hypertension at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_028 — safety_monitoring_change — H-ONC-227 (Oncology)

**Previous protocol text (Section being amended):** Protocol H-ONC-227, Version 1: Safety monitoring for the investigational therapy includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-ONC-227, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 240 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with relapsed/refractory multiple myeloma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_029 — endpoint_change — H-NEU-228 (Neurology)

**Previous protocol text (Section being amended):** Protocol H-NEU-228, Version 1: The primary efficacy endpoint is clinical remission in subjects with chronic migraine at Week 52.

**Amendment text:** Protocol H-NEU-228, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 10 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic migraine at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_030 — informed_consent_change — H-RHE-229 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol H-RHE-229, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-RHE-229, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 20 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with active psoriatic arthritis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_031 — discontinuation_criteria_change — H-INF-230 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol H-INF-230, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-INF-230, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antimicrobial agent is administered at 40 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the antimicrobial agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the antimicrobial agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with complicated urinary tract infection at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antimicrobial agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_032 — drug_interaction_change — H-DER-231 (Dermatology)

**Previous protocol text (Section being amended):** Protocol H-DER-231, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-DER-231, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the study agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 80 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe atopic dermatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_033 — dose_change — H-NEP-232 (Nephrology)

**Previous protocol text (Section being amended):** Protocol H-NEP-232, Version 1: Subjects with IgA nephropathy receive the investigational compound at 120 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-NEP-232, Amendment 2: Section 5.2 is revised. The dose is changed from 120 mg once daily to 10 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 120 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with IgA nephropathy at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (120 mg once daily to 10 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 10 mg once daily as the current dose and keep 120 mg once daily as the prior protocol state.

---

## heldout_034 — eligibility_change — H-HEP-233 (Hepatology)

**Previous protocol text (Section being amended):** Protocol H-HEP-233, Version 1: Subjects with non-alcoholic steatohepatitis and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-HEP-233, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 160 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with non-alcoholic steatohepatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_035 — visit_schedule_change — H-HEM-234 (Hematology)

**Previous protocol text (Section being amended):** Protocol H-HEM-234, Version 1: Subjects with sickle cell disease attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-HEM-234, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 240 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with sickle cell disease at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_036 — safety_monitoring_change — H-OPH-235 (Ophthalmology)

**Previous protocol text (Section being amended):** Protocol H-OPH-235, Version 1: Safety monitoring for the study drug includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-OPH-235, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 10 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with diabetic macular edema at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_037 — endpoint_change — H-GAS-236 (Gastroenterology)

**Previous protocol text (Section being amended):** Protocol H-GAS-236, Version 1: The primary efficacy endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52.

**Amendment text:** Protocol H-GAS-236, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 20 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe ulcerative colitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_038 — informed_consent_change — H-URO-237 (Urology)

**Previous protocol text (Section being amended):** Protocol H-URO-237, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-URO-237, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 40 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with overactive bladder at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_039 — discontinuation_criteria_change — H-ALL-238 (Allergy/Immunology)

**Previous protocol text (Section being amended):** Protocol H-ALL-238, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-ALL-238, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 80 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic spontaneous urticaria at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_040 — drug_interaction_change — H-ORT-239 (Orthopedics)

**Previous protocol text (Section being amended):** Protocol H-ORT-239, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-ORT-239, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the investigational analgesic.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational analgesic is administered at 120 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational analgesic are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational analgesic.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with post-surgical pain at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational analgesic for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_041 — dose_change — H-END-240 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol H-END-240, Version 1: Subjects with obesity with weight-related comorbidity receive the investigational agent at 160 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-END-240, Amendment 2: Section 5.2 is revised. The dose is changed from 160 mg once daily to 20 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 160 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with obesity with weight-related comorbidity at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (160 mg once daily to 20 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 20 mg once daily as the current dose and keep 160 mg once daily as the prior protocol state.

---

## heldout_042 — eligibility_change — H-PUL-241 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol H-PUL-241, Version 1: Subjects with severe eosinophilic asthma and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-PUL-241, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 240 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with severe eosinophilic asthma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

## heldout_043 — visit_schedule_change — H-CAR-242 (Cardiology)

**Previous protocol text (Section being amended):** Protocol H-CAR-242, Version 1: Subjects with resistant hypertension attend visits at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.

**Amendment text:** Protocol H-CAR-242, Amendment 2: Section 8.1 is revised. A Week 4 visit is added for an interim efficacy assessment requested by the data monitoring committee.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 10 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with resistant hypertension at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.2, 8.1, 8.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a Week 4 visit, so 8.1 is directly affected. I also marked 8.2 and 7.2 because the new visit is for an interim efficacy assessment, so the visit procedures and endpoint assessment schedule need to show what is collected at Week 4.

---

## heldout_044 — safety_monitoring_change — H-ONC-243 (Oncology)

**Previous protocol text (Section being amended):** Protocol H-ONC-243, Version 1: Safety monitoring for the investigational therapy includes standard laboratory panels at each scheduled visit.

**Amendment text:** Protocol H-ONC-243, Amendment 2: Section 11.3 is revised. Renal function panels are now required every 4 weeks for the first 6 months, following a nephrotoxicity signal observed in a related compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational therapy is administered at 20 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational therapy are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational therapy.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with relapsed/refractory multiple myeloma at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational therapy for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3, 11.4

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because renal function panels are added every 4 weeks for the first 6 months. I marked 8.1 and 8.2 because that cadence may need to appear in the assessment schedule and visit procedures. I also marked 11.4 because the change is driven by a nephrotoxicity signal that may need safety-review oversight.

---

## heldout_045 — endpoint_change — H-NEU-244 (Neurology)

**Previous protocol text (Section being amended):** Protocol H-NEU-244, Version 1: The primary efficacy endpoint is clinical remission in subjects with chronic migraine at Week 52.

**Amendment text:** Protocol H-NEU-244, Amendment 2: Section 7.1 is revised. A key secondary endpoint of sustained remission at Week 24 is added following updated regulatory feedback.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 40 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with chronic migraine at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.2, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint stays at Week 52, but a key secondary endpoint at Week 24 is added. I marked 7.1, 7.2, and 12.1 because the endpoint list, endpoint timing, and statistical analysis plan all need updates. I also marked 8.2 so the Week 24 visit procedures include the sustained-remission assessment.

---

## heldout_046 — informed_consent_change — H-RHE-245 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol H-RHE-245, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol H-RHE-245, Amendment 2: Section 9.1 is revised. An optional genetic sub-study consent is added, requiring separate written consent from participating subjects.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 80 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with active psoriatic arthritis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds a separate optional genetic sub-study consent. Section 9.1 is direct, and 9.2 should be checked for any assent, separate-consent, or re-consent handling that applies to participating subjects. I did not include the FDA safety-reporting rule because this is not a new safety-risk consent update.

---

## heldout_047 — discontinuation_criteria_change — H-INF-246 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol H-INF-246, Version 1: Subjects are discontinued for lack of clinical benefit at Week 24 or withdrawal of consent.

**Amendment text:** Protocol H-INF-246, Amendment 2: Section 10.1 is revised. Pregnancy during the treatment period is added as a mandatory discontinuation criterion.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antimicrobial agent is administered at 120 mg once weekly. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the antimicrobial agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the antimicrobial agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with complicated urinary tract infection at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antimicrobial agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 10.1, 10.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** Section 10.1 is directly affected because pregnancy during treatment is added as a mandatory discontinuation criterion. I also marked 10.2 because the protocol should say what withdrawal or follow-up steps occur after discontinuation for pregnancy. I did not mark AE definitions or safety monitoring because the change is not framed as an adverse-event stopping rule.

---

## heldout_048 — drug_interaction_change — H-DER-247 (Dermatology)

**Previous protocol text (Section being amended):** Protocol H-DER-247, Version 1: Concomitant use of live vaccines is permitted with a 2-week washout before dosing.

**Amendment text:** Protocol H-DER-247, Amendment 2: Section 6.2 is revised. The live-vaccine washout period is extended from 2 to 4 weeks before any dose of the study agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 160 mg every 4 weeks. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with moderate-to-severe atopic dermatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.2, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment extends the live-vaccine washout from 2 to 4 weeks before dosing. Section 6.2 is direct, and 6.1 should be checked so the general concomitant-medication language matches the new washout. I also marked 4.2 because screening eligibility depends on prohibited concomitant medications.

---

## heldout_049 — dose_change — H-NEP-248 (Nephrology)

**Previous protocol text (Section being amended):** Protocol H-NEP-248, Version 1: Subjects with IgA nephropathy receive the investigational compound at 240 mg once daily, unchanged throughout the treatment period.

**Amendment text:** Protocol H-NEP-248, Amendment 2: Section 5.2 is revised. The dose is changed from 240 mg once daily to 40 mg once daily following a planned interim pharmacokinetic review.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 240 mg once daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with IgA nephropathy at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (240 mg once daily to 40 mg once daily). I included 5.3 and 11.3 because dose-interruption rules and safety monitoring should be checked after a large exposure change. After Amendment 2, I would treat 40 mg once daily as the current dose and keep 240 mg once daily as the prior protocol state.

---

## heldout_050 — eligibility_change — H-HEP-249 (Hepatology)

**Previous protocol text (Section being amended):** Protocol H-HEP-249, Version 1: Subjects with non-alcoholic steatohepatitis and an estimated glomerular filtration rate below 30 mL/min/1.73m² are excluded.

**Amendment text:** Protocol H-HEP-249, Amendment 2: Section 4.2 is revised. The eGFR exclusion threshold is lowered from 30 to 20 mL/min/1.73m², broadening eligibility based on a completed renal-impairment sub-study.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with an active infection requiring systemic therapy within 30 days of screening are excluded. Subjects requiring a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study agent is administered at 10 mg twice daily. Dose is not adjusted based on body weight.
- `5.3`: Section 5.3, Dose Modification Rules: Dose interruptions for the study agent are permitted for Grade 2 or higher treatment-related adverse events, resuming at the same dose upon resolution to Grade 1 or lower.
- `6.2`: Section 6.2, Prohibited Medications: Live vaccines are prohibited within 4 weeks of any dose of the study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical remission in subjects with non-alcoholic steatohepatitis at Week 52, as defined in Appendix B.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 2, Week 8, Week 24, and Week 52.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study agent for lack of clinical benefit at Week 24, withdrawal of consent, or unacceptable toxicity.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels are collected at each scheduled visit per Section 8.1.

**Impacted sections (list codes from above):** 4.1, 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This directly changes the renal-function exclusion criterion in 4.2 by lowering the eGFR cutoff from 30 to 20 mL/min/1.73m². I also marked 4.1 because broadening eligibility changes the study population being enrolled. I did not mark dosing or monitoring because the amendment does not change treatment administration or visit procedures.

---

