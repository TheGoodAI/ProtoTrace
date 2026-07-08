# Annotator Worksheet — Pilot Impact/Governance Labeling (n=50)

Read the protocol text, amendment text, and the current text of the context
sections below for each scenario. Do not consult any system output. For each
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

## pilot_001 — dose_change — ONC-100 (Oncology)

**Previous protocol text (Section being amended):** Protocol ONC-100, Version 1: Eligible subjects with solid-tumor will receive the investigational agent at a dose of 25 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol ONC-100, Amendment 1: Section 5.2 is revised. The dose of the investigational agent is changed from 25 mg once daily to 75 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 25 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with solid-tumor at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (25 mg once daily to 75 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 75 mg once daily as the current dose for post-amendment enrollment and keep 25 mg once daily as the prior protocol state.

---

## pilot_002 — eligibility_change — CAR-101 (Cardiology)

**Previous protocol text (Section being amended):** Protocol CAR-101, Version 1: Key exclusion criteria for this cardiology study in heart-failure include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol CAR-101, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 50 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with heart-failure at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_003 — visit_schedule_change — END-102 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol END-102, Version 1: Subjects with type 2 diabetes will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol END-102, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 75 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with type 2 diabetes at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_004 — safety_monitoring_change — INF-103 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol INF-103, Version 1: Safety monitoring for subjects receiving the antiviral agent includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol INF-103, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antiviral agent is administered at 100 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the antiviral agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the antiviral agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic hepatitis B at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antiviral agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_005 — endpoint_change — NEU-104 (Neurology)

**Previous protocol text (Section being amended):** Protocol NEU-104, Version 1: The primary efficacy endpoint is the proportion of subjects with relapsing multiple sclerosis achieving clinical response at Week 24.

**Amendment text:** Protocol NEU-104, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study treatment is administered at 150 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study treatment are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study treatment.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with relapsing multiple sclerosis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study treatment for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_006 — informed_consent_change — RHE-105 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol RHE-105, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol RHE-105, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the biologic agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 200 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe rheumatoid arthritis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_007 — discontinuation_criteria_change — PSY-106 (Psychiatry)

**Previous protocol text (Section being amended):** Protocol PSY-106, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol PSY-106, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the investigational drug.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational drug is administered at 300 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with treatment-resistant major depressive disorder at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_008 — drug_interaction_change — DER-107 (Dermatology)

**Previous protocol text (Section being amended):** Protocol DER-107, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol DER-107, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the study medication, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 25 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe plaque psoriasis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_009 — dose_change — PUL-108 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol PUL-108, Version 1: Eligible subjects with chronic obstructive pulmonary disease will receive the inhaled study agent at a dose of 50 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol PUL-108, Amendment 1: Section 5.2 is revised. The dose of the inhaled study agent is changed from 50 mg once daily to 100 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The inhaled study agent is administered at 50 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the inhaled study agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the inhaled study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic obstructive pulmonary disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the inhaled study agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (50 mg once daily to 100 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 100 mg once daily as the current dose for post-amendment enrollment and keep 50 mg once daily as the prior protocol state.

---

## pilot_010 — eligibility_change — NEP-109 (Nephrology)

**Previous protocol text (Section being amended):** Protocol NEP-109, Version 1: Key exclusion criteria for this nephrology study in diabetic kidney disease include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol NEP-109, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 75 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with diabetic kidney disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_011 — visit_schedule_change — ONC-110 (Oncology)

**Previous protocol text (Section being amended):** Protocol ONC-110, Version 1: Subjects with solid-tumor will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol ONC-110, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 100 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with solid-tumor at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_012 — safety_monitoring_change — CAR-111 (Cardiology)

**Previous protocol text (Section being amended):** Protocol CAR-111, Version 1: Safety monitoring for subjects receiving the study drug includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol CAR-111, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 150 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with heart-failure at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_013 — endpoint_change — END-112 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol END-112, Version 1: The primary efficacy endpoint is the proportion of subjects with type 2 diabetes achieving clinical response at Week 24.

**Amendment text:** Protocol END-112, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 200 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with type 2 diabetes at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_014 — informed_consent_change — INF-113 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol INF-113, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol INF-113, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the antiviral agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antiviral agent is administered at 300 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the antiviral agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the antiviral agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic hepatitis B at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antiviral agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_015 — discontinuation_criteria_change — NEU-114 (Neurology)

**Previous protocol text (Section being amended):** Protocol NEU-114, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol NEU-114, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the study treatment.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study treatment is administered at 25 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study treatment are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study treatment.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with relapsing multiple sclerosis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study treatment for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_016 — drug_interaction_change — RHE-115 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol RHE-115, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol RHE-115, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the biologic agent, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 50 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe rheumatoid arthritis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_017 — dose_change — PSY-116 (Psychiatry)

**Previous protocol text (Section being amended):** Protocol PSY-116, Version 1: Eligible subjects with treatment-resistant major depressive disorder will receive the investigational drug at a dose of 75 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol PSY-116, Amendment 1: Section 5.2 is revised. The dose of the investigational drug is changed from 75 mg once daily to 150 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational drug is administered at 75 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with treatment-resistant major depressive disorder at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (75 mg once daily to 150 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 150 mg once daily as the current dose for post-amendment enrollment and keep 75 mg once daily as the prior protocol state.

---

## pilot_018 — eligibility_change — DER-117 (Dermatology)

**Previous protocol text (Section being amended):** Protocol DER-117, Version 1: Key exclusion criteria for this dermatology study in moderate-to-severe plaque psoriasis include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol DER-117, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 100 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe plaque psoriasis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_019 — visit_schedule_change — PUL-118 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol PUL-118, Version 1: Subjects with chronic obstructive pulmonary disease will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol PUL-118, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The inhaled study agent is administered at 150 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the inhaled study agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the inhaled study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic obstructive pulmonary disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the inhaled study agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_020 — safety_monitoring_change — NEP-119 (Nephrology)

**Previous protocol text (Section being amended):** Protocol NEP-119, Version 1: Safety monitoring for subjects receiving the investigational compound includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol NEP-119, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 200 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with diabetic kidney disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_021 — endpoint_change — ONC-120 (Oncology)

**Previous protocol text (Section being amended):** Protocol ONC-120, Version 1: The primary efficacy endpoint is the proportion of subjects with solid-tumor achieving clinical response at Week 24.

**Amendment text:** Protocol ONC-120, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 300 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with solid-tumor at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_022 — informed_consent_change — CAR-121 (Cardiology)

**Previous protocol text (Section being amended):** Protocol CAR-121, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol CAR-121, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the study drug.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 25 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with heart-failure at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_023 — discontinuation_criteria_change — END-122 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol END-122, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol END-122, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the investigational compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 50 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with type 2 diabetes at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_024 — drug_interaction_change — INF-123 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol INF-123, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol INF-123, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the antiviral agent, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antiviral agent is administered at 75 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the antiviral agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the antiviral agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic hepatitis B at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antiviral agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_025 — dose_change — NEU-124 (Neurology)

**Previous protocol text (Section being amended):** Protocol NEU-124, Version 1: Eligible subjects with relapsing multiple sclerosis will receive the study treatment at a dose of 100 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol NEU-124, Amendment 1: Section 5.2 is revised. The dose of the study treatment is changed from 100 mg once daily to 200 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study treatment is administered at 100 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study treatment are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study treatment.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with relapsing multiple sclerosis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study treatment for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (100 mg once daily to 200 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 200 mg once daily as the current dose for post-amendment enrollment and keep 100 mg once daily as the prior protocol state.

---

## pilot_026 — eligibility_change — RHE-125 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol RHE-125, Version 1: Key exclusion criteria for this rheumatology study in moderate-to-severe rheumatoid arthritis include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol RHE-125, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 150 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe rheumatoid arthritis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_027 — visit_schedule_change — PSY-126 (Psychiatry)

**Previous protocol text (Section being amended):** Protocol PSY-126, Version 1: Subjects with treatment-resistant major depressive disorder will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol PSY-126, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational drug is administered at 200 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with treatment-resistant major depressive disorder at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_028 — safety_monitoring_change — DER-127 (Dermatology)

**Previous protocol text (Section being amended):** Protocol DER-127, Version 1: Safety monitoring for subjects receiving the study medication includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol DER-127, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 300 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe plaque psoriasis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_029 — endpoint_change — PUL-128 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol PUL-128, Version 1: The primary efficacy endpoint is the proportion of subjects with chronic obstructive pulmonary disease achieving clinical response at Week 24.

**Amendment text:** Protocol PUL-128, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The inhaled study agent is administered at 25 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the inhaled study agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the inhaled study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic obstructive pulmonary disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the inhaled study agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_030 — informed_consent_change — NEP-129 (Nephrology)

**Previous protocol text (Section being amended):** Protocol NEP-129, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol NEP-129, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the investigational compound.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 50 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with diabetic kidney disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_031 — discontinuation_criteria_change — ONC-130 (Oncology)

**Previous protocol text (Section being amended):** Protocol ONC-130, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol ONC-130, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the investigational agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 75 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with solid-tumor at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_032 — drug_interaction_change — CAR-131 (Cardiology)

**Previous protocol text (Section being amended):** Protocol CAR-131, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol CAR-131, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the study drug, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 100 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with heart-failure at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_033 — dose_change — END-132 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol END-132, Version 1: Eligible subjects with type 2 diabetes will receive the investigational compound at a dose of 150 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol END-132, Amendment 1: Section 5.2 is revised. The dose of the investigational compound is changed from 150 mg once daily to 300 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 150 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with type 2 diabetes at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (150 mg once daily to 300 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 300 mg once daily as the current dose for post-amendment enrollment and keep 150 mg once daily as the prior protocol state.

---

## pilot_034 — eligibility_change — INF-133 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol INF-133, Version 1: Key exclusion criteria for this infectious disease study in chronic hepatitis B include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol INF-133, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antiviral agent is administered at 200 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the antiviral agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the antiviral agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic hepatitis B at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antiviral agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_035 — visit_schedule_change — NEU-134 (Neurology)

**Previous protocol text (Section being amended):** Protocol NEU-134, Version 1: Subjects with relapsing multiple sclerosis will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol NEU-134, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study treatment is administered at 300 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study treatment are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study treatment.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with relapsing multiple sclerosis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study treatment for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_036 — safety_monitoring_change — RHE-135 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol RHE-135, Version 1: Safety monitoring for subjects receiving the biologic agent includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol RHE-135, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 25 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe rheumatoid arthritis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_037 — endpoint_change — PSY-136 (Psychiatry)

**Previous protocol text (Section being amended):** Protocol PSY-136, Version 1: The primary efficacy endpoint is the proportion of subjects with treatment-resistant major depressive disorder achieving clinical response at Week 24.

**Amendment text:** Protocol PSY-136, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational drug is administered at 50 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with treatment-resistant major depressive disorder at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_038 — informed_consent_change — DER-137 (Dermatology)

**Previous protocol text (Section being amended):** Protocol DER-137, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol DER-137, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the study medication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 75 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe plaque psoriasis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_039 — discontinuation_criteria_change — PUL-138 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol PUL-138, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol PUL-138, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the inhaled study agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The inhaled study agent is administered at 100 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the inhaled study agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the inhaled study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic obstructive pulmonary disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the inhaled study agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_040 — drug_interaction_change — NEP-139 (Nephrology)

**Previous protocol text (Section being amended):** Protocol NEP-139, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol NEP-139, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the investigational compound, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 150 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with diabetic kidney disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_041 — dose_change — ONC-140 (Oncology)

**Previous protocol text (Section being amended):** Protocol ONC-140, Version 1: Eligible subjects with solid-tumor will receive the investigational agent at a dose of 200 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol ONC-140, Amendment 1: Section 5.2 is revised. The dose of the investigational agent is changed from 200 mg once daily to 25 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational agent is administered at 200 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with solid-tumor at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (200 mg once daily to 25 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 25 mg once daily as the current dose for post-amendment enrollment and keep 200 mg once daily as the prior protocol state.

---

## pilot_042 — eligibility_change — CAR-141 (Cardiology)

**Previous protocol text (Section being amended):** Protocol CAR-141, Version 1: Key exclusion criteria for this cardiology study in heart-failure include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol CAR-141, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study drug is administered at 300 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with heart-failure at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---

## pilot_043 — visit_schedule_change — END-142 (Endocrinology)

**Previous protocol text (Section being amended):** Protocol END-142, Version 1: Subjects with type 2 diabetes will attend study visits at Screening, Day 1, Week 4, Week 12, and Week 24 for efficacy and safety assessments.

**Amendment text:** Protocol END-142, Amendment 1: Section 8.1 is revised. An additional interim safety visit at Week 8 is added to the schedule of assessments to allow earlier detection of hepatic laboratory abnormalities.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 25 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with type 2 diabetes at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** The amendment adds an interim safety visit at Week 8, so 8.1 is directly affected. I also marked 8.2 and 11.3 because visit procedures and safety labs need to reflect the added visit. This is an added schedule point, not a replacement of the whole visit schedule.

---

## pilot_044 — safety_monitoring_change — INF-143 (Infectious Disease)

**Previous protocol text (Section being amended):** Protocol INF-143, Version 1: Safety monitoring for subjects receiving the antiviral agent includes standard laboratory panels collected at each scheduled visit.

**Amendment text:** Protocol INF-143, Amendment 1: Section 11.3 is revised. Liver function tests are now required every 2 weeks for the first 3 months of treatment, in addition to the standard visit-based panel, following a hepatotoxicity signal in a related compound class.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The antiviral agent is administered at 50 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the antiviral agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the antiviral agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic hepatitis B at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the antiviral agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 8.1, 8.2, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 11.3 is the direct change because LFT monitoring is more frequent for the first 3 months. I included 8.1 and 8.2 because the extra lab cadence may require added visits or procedures outside the standard schedule. The safety-reporting references apply because the change is driven by a hepatotoxicity signal.

---

## pilot_045 — endpoint_change — NEU-144 (Neurology)

**Previous protocol text (Section being amended):** Protocol NEU-144, Version 1: The primary efficacy endpoint is the proportion of subjects with relapsing multiple sclerosis achieving clinical response at Week 24.

**Amendment text:** Protocol NEU-144, Amendment 1: Section 7.1 is revised. The primary endpoint assessment timepoint is changed from Week 24 to Week 16 to align with the revised regulatory guidance for this indication.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study treatment is administered at 75 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study treatment are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study treatment.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with relapsing multiple sclerosis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study treatment for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 7.1, 7.2, 8.1, 12.1

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The primary endpoint timepoint changes from Week 24 to Week 16. I marked 7.2, 8.1, and 12.1 as downstream checks because the assessment schedule, visit windows, and analysis plan all need to line up with the earlier endpoint. I would use Amendment 1 as the source for the current endpoint timing.

---

## pilot_046 — informed_consent_change — RHE-145 (Rheumatology)

**Previous protocol text (Section being amended):** Protocol RHE-145, Version 1: Subjects provide written informed consent prior to any study-related procedures.

**Amendment text:** Protocol RHE-145, Amendment 1: Section 9.1 is revised. A re-consent process is added for all currently enrolled subjects to reflect the newly identified risk of hepatic enzyme elevation associated with the biologic agent.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The biologic agent is administered at 100 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the biologic agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the biologic agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe rheumatoid arthritis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the biologic agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 9.1, 9.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; EMA: EMA GCP Q&A Section 5; ICH: ICH E6(R2) Section 4.5

**Annotator notes (optional):** The amendment adds re-consent for currently enrolled subjects because of a newly identified hepatic risk. Section 9.1 is direct, and 9.2 should be checked for any assent or re-consent handling requirements. I included the safety and EMA re-consent references because the consent change is risk-driven.

---

## pilot_047 — discontinuation_criteria_change — PSY-146 (Psychiatry)

**Previous protocol text (Section being amended):** Protocol PSY-146, Version 1: Subjects will be discontinued from study treatment for confirmed disease progression or unacceptable toxicity per the treating investigator's assessment.

**Amendment text:** Protocol PSY-146, Amendment 1: Section 10.1 is revised. A new mandatory discontinuation criterion is added: any subject with a confirmed Grade 3 or higher hepatic adverse event must permanently discontinue the investigational drug.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational drug is administered at 150 mg once weekly, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational drug are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational drug.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with treatment-resistant major depressive disorder at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational drug for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 10.1, 10.2, 11.1, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; FDA: 21 CFR 312.32; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-SafetyMonitoring-02

**Annotator notes (optional):** Section 10.1 is directly affected because a mandatory stop rule is added for confirmed Grade 3 or higher hepatic AEs. I marked 10.2, 11.1, and 11.3 because withdrawal steps, AE grading/definitions, and monitoring need to be consistent with that new rule. Safety references apply because this is an AE-driven discontinuation change.

---

## pilot_048 — drug_interaction_change — DER-147 (Dermatology)

**Previous protocol text (Section being amended):** Protocol DER-147, Version 1: Concomitant use of strong CYP3A4 inhibitors is permitted with dose adjustment per investigator discretion.

**Amendment text:** Protocol DER-147, Amendment 1: Section 6.2 is revised. Concomitant use of strong CYP3A4 inhibitors is now prohibited for subjects receiving the study medication, based on updated drug-drug interaction modeling.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The study medication is administered at 200 mg every other week, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the study medication are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the study medication.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with moderate-to-severe plaque psoriasis at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the study medication for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2, 5.3, 6.1, 6.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** The amendment changes strong CYP3A4 inhibitors from allowed with dose adjustment to prohibited. Section 6.2 is direct; 6.1, 5.3, and 4.2 should also be checked so concomitant-medication instructions, dose-adjustment language, and exclusion criteria do not contradict the new prohibition.

---

## pilot_049 — dose_change — PUL-148 (Pulmonology)

**Previous protocol text (Section being amended):** Protocol PUL-148, Version 1: Eligible subjects with chronic obstructive pulmonary disease will receive the inhaled study agent at a dose of 300 mg once daily by oral administration, beginning on Day 1 and continuing for the duration of the treatment period.

**Amendment text:** Protocol PUL-148, Amendment 1: Section 5.2 is revised. The dose of the inhaled study agent is changed from 300 mg once daily to 50 mg once daily, effective for all subjects enrolled after the amendment effective date, based on emerging pharmacokinetic data from the ongoing dose-finding cohort.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The inhaled study agent is administered at 300 mg once daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the inhaled study agent are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the inhaled study agent.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with chronic obstructive pulmonary disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the inhaled study agent for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 5.2, 5.3, 11.3

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-DoseChange-01

**Annotator notes (optional):** Direct change is Section 5.2 (300 mg once daily to 50 mg once daily). I included 5.3 and 11.3 because dose modification rules and safety monitoring should be checked when exposure changes. After Amendment 1, I would treat 50 mg once daily as the current dose for post-amendment enrollment and keep 300 mg once daily as the prior protocol state.

---

## pilot_050 — eligibility_change — NEP-149 (Nephrology)

**Previous protocol text (Section being amended):** Protocol NEP-149, Version 1: Key exclusion criteria for this nephrology study in diabetic kidney disease include prior use of a biologic agent within 12 weeks of screening.

**Amendment text:** Protocol NEP-149, Amendment 1: Section 4.2 is revised. The washout period for prior biologic use is extended from 12 weeks to 16 weeks prior to screening, following a safety signal identified in a related program.

**Current text of candidate sections (read these to judge impact):**

- `4.2`: Section 4.2, Key Exclusion Criteria: Subjects with clinically significant hepatic impairment (ALT or AST > 2.5x ULN) at screening are excluded. Subjects requiring chronic use of a prohibited concomitant medication (see Section 6.2) are excluded.
- `5.2`: Section 5.2, Dosing and Administration: The investigational compound is administered at 25 mg twice daily, taken with food. No dose escalation is permitted outside the schedule defined in this section.
- `5.3`: Section 5.3, Dose Modification Rules: Dose reductions for the investigational compound are permitted for Grade 2 or higher treatment-related adverse events, per the dose modification table in Appendix C. No more than two dose reductions are permitted per subject.
- `6.2`: Section 6.2, Prohibited Medications: Strong CYP3A4 inhibitors and inducers are prohibited from 14 days prior to Day 1 through end of treatment for subjects receiving the investigational compound.
- `7.1`: Section 7.1, Efficacy Endpoints: The primary endpoint is clinical response in subjects with diabetic kidney disease at Week 24, as defined in Appendix B. Key secondary endpoints are assessed at the same visit.
- `8.1`: Section 8.1, Schedule of Assessments: Study visits occur at Screening, Day 1, Week 4, Week 12, and Week 24. Laboratory safety panels and vital signs are collected at every visit.
- `10.1`: Section 10.1, Discontinuation Criteria: Subjects are discontinued from the investigational compound for confirmed disease progression, withdrawal of consent, or unacceptable toxicity per investigator judgment.
- `11.3`: Section 11.3, Safety Monitoring Plan: Standard laboratory safety panels, including hepatic function tests, are collected at each scheduled visit per Section 8.1. Results are reviewed by the investigator prior to the next dose.

**Impacted sections (list codes from above):** 4.2

**Governing references (list authority/citation from pool above):** FDA: 21 CFR 312.30; EMA: EMA GCP Q&A Section 3; ICH: ICH E6(R2) Section 4.5; Internal SOP: SOP-Eligibility-03

**Annotator notes (optional):** This is a direct exclusion-criteria update: the biologic washout window moves from 12 weeks to 16 weeks. I only marked 4.2 because the amendment does not change dosing, visits, endpoints, or monitoring language. After Amendment 1, the operative eligibility rule is the 16-week washout.

---





