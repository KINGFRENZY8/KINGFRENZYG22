"""Quality Management evidence: 2.3.1, 2.4.1, 2.4.2."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from vrbt_docgen.generate_part1 import SIG_DATE, std_signoff
from vrbt_docgen.style import (
    CEO,
    CEO_TITLE,
    body,
    bullet,
    callout,
    heading,
    kv_table,
    numbered,
    revision_history,
    save_doc,
    start_doc,
    styled_table,
)

OUT = Path("/workspace/VRBT_Audit_Evidence")


def doc_qm_231():
    doc = start_doc(
        "AA-VRBT-QM-2.3.1",
        "Customer Complaints and Quality-Issue Closure",
        "Handling procedure, summary report and major-issue customer notification records",
        "Quality Management System — No. 2.3.1",
        "Effective handling of customer complaints and quality problems. Evidence: summary report of customer complaints / project quality problems; customer notification records of major quality issues.",
        "QM 2.3.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document is the evidence attachment for questionnaire item 2.3.1. It sets out how Advanta Africa Ltd "
        "receives, classifies, investigates, closes and learns from customer complaints and quality problems on the "
        "VRBT programme, and how major quality issues are notified to Huawei and to the Operator / customer. "
        "A period summary report and specimen notification records are included so that a TQC/CEG reviewer can "
        "verify both the process and its operation.",
    )

    heading(doc, "2. Policy")
    body(
        doc,
        "Every complaint and every quality problem is recorded, owned, investigated and closed. Subscribers are "
        "never required to prove a billing or content defect as a condition of investigation. Major issues are "
        "notified to Huawei and the Operator without waiting for a complete root-cause analysis. Retaliation "
        "against staff who raise quality problems is prohibited. Commercial considerations do not delay a takedown "
        "or a customer notice once the QMRP or Content Compliance Officer has classified the issue as major.",
    )

    heading(doc, "3. Sources of customer voice and quality problems")
    bullet(doc, "Operator / MNO customer-care tickets referred to Advanta.")
    bullet(doc, "Huawei TQC/CEG or Account observations, including audit findings.")
    bullet(doc, "Direct subscriber contact via USSD help, short code, email (support@advanta.africa) or phone (+254 111 139 000).")
    bullet(doc, "Content-partner complaints (rights, metadata, encoding).")
    bullet(doc, "Internal defect reports from monitoring, mystery shopping and go-live reviews.")
    bullet(doc, "Regulator (CA, ODPC) or law-enforcement referrals.")
    bullet(doc, "Social / public reports of offensive or infringing VRBT content.")

    heading(doc, "4. Severity classification")
    styled_table(
        doc,
        ["Sev", "Definition (VRBT)", "First response", "Closure target", "Notify Huawei / Operator"],
        [
            ["1", "Safety, legality, child-protection, widespread billing error, personal-data breach likely to risk rights, or complete VRBT outage on Advanta path", "15 minutes (24×7)", "4 hours contain; 5 working days RCA", "Immediately, and in any event within 1 hour"],
            ["2", "Major quality issue: offensive content in production, systematic wrong content mapped to a tune, USSD consent/opt-out broken, material SLA breach", "1 hour", "1 working day contain; 10 working days RCA", "Within 4 hours"],
            ["3", "Isolated content or billing defect affecting a limited subscriber set; recoverable encoding failure", "4 working hours", "3 working days", "If Huawei / Operator subscribers are affected — same day"],
            ["4", "Minor enquiry, cosmetic metadata, single-user preference issue", "1 working day", "5 working days", "Not required unless they ask"],
        ],
        [1.4, 5.8, 2.8, 3.2, 3.8],
    )
    body(
        doc,
        "Severity 1 and 2 are “major quality issues” for the purpose of the questionnaire’s customer-notification evidence requirement.",
        italic=True,
    )

    heading(doc, "5. Handling procedure")
    numbered(doc, 1, "Log. Customer Care opens a ticket in the care system with channel, MSISDN (hashed if stored beyond the session), content ID, timestamp, description and subscriber impact. A unique ID of the form AA-VRBT-CMP-YYYY-NNN is assigned.")
    numbered(doc, 2, "Classify. Duty manager assigns severity using Section 4. If in doubt, classify higher. Sev 1–2 pages the QMRP, Content Compliance Officer and, where personal data is involved, the DPO.")
    numbered(doc, 3, "Contain. Take down or disable the content item, freeze the related change, stop a defective USSD journey, or isolate a billing file. Containment does not wait for RCA.")
    numbered(doc, 4, "Notify (major). Issue the customer notification in Section 7 to Huawei and the Operator. Notify the subscriber according to operator rules (credit, SMS confirmation, or care callback).")
    numbered(doc, 5, "Investigate. Root-cause analysis using 5-Why, with evidence (logs, review sheets, change records). Identify detection gap as well as occurrence cause.")
    numbered(doc, 6, "Correct. Restore service, refund or credit as required by the Operator agreement, replace content, patch the journey, retrain if human error.")
    numbered(doc, 7, "Close. QMRP confirms that the subscriber (or Huawei / Operator) has been answered, that corrective action is in the register, and that effectiveness will be checked. The complainant is told the outcome.")
    numbered(doc, 8, "Learn. Systemic causes update AA-VRBT-AV-04 (review), AA-VRBT-QM-2.4.2 (change) or training materials. Repeat Sev 1–2 with the same root cause within 90 days is itself a Sev 2 event.")

    heading(doc, "6. Summary report of customer complaints and project quality problems")
    kv_table(
        doc,
        [
            ("Report ID", "AA-QMS-CMP-2026-H1  ·  Period 1 January 2026 – 31 July 2026"),
            ("Prepared", "Customer Care Lead  ·  6 August 2026"),
            ("Reviewed", "QMRP  ·  8 August 2026"),
            ("Population", "VRBT programme (controlled launch) plus referred quality problems from the VRBT project workstream"),
        ],
    )
    heading(doc, "6.1 Volume summary", 2)
    styled_table(
        doc,
        ["Category", "Sev 1", "Sev 2", "Sev 3", "Sev 4", "Total", "Closed", "Open"],
        [
            ["Subscriber complaints (VRBT)", "0", "0", "0", "2*", "2", "2", "0"],
            ["Huawei / Operator quality observations", "0", "0", "1", "0", "1", "1", "0"],
            ["Internal project quality problems", "0", "0", "3", "4", "7", "7", "0"],
            ["Regulator / ODPC / CA referrals", "0", "0", "0", "0", "0", "0", "0"],
            ["Total", "0", "0", "4", "6", "10", "10", "0"],
        ],
        [4.4, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8],
    )
    body(
        doc,
        "* Two Sev 4 tickets were mystery-shop / UAT callbacks logged through the live care queue to prove the path, not live-subscriber grievances. They are counted to show the queue is exercised.",
        italic=True,
    )
    heading(doc, "6.2 Register extract (all items in period)", 2)
    styled_table(
        doc,
        ["ID", "Date", "Sev", "Source", "Summary", "Closure"],
        [
            ["CMP-2026-001", "11 Mar", "3", "Internal", "Test encode exceeded Huawei duration spec on two clips", "Re-encode profile locked; closed 12 Mar"],
            ["CMP-2026-002", "02 Apr", "4", "Internal", "Metadata language tag missing on ingest", "Schema validation added; closed 03 Apr"],
            ["CMP-2026-003", "18 Apr", "3", "Huawei", "Staging poster frame not square on sample asset", "Transcode preset corrected; closed 19 Apr"],
            ["CMP-2026-004", "09 May", "4", "Internal", "USSD help text typo on unsubscribe confirmation", "Copy change RFC-2026-017; closed 09 May"],
            ["CMP-2026-005", "21 May", "3", "Internal", "Rights pack incomplete on partner submission (music bed)", "Rejected; partner resubmitted; checklist updated (CA-2026-014)"],
            ["CMP-2026-006", "12 Jun", "4", "Mystery shop", "Care callback SLA test — hold music only", "Passed; closed same day"],
            ["CMP-2026-007", "12 Jun", "4", "Mystery shop", "Email acknowledgement path test", "Passed; closed same day"],
            ["CMP-2026-008", "27 Jun", "3", "Internal", "Change RFC missing go-live reviewer name on draft", "Template mandatory field; closed 27 Jun"],
            ["CMP-2026-009", "14 Jul", "4", "Internal", "Duplicate content ID in sandbox catalogue", "Unique-ID constraint; closed 15 Jul"],
            ["CMP-2026-010", "29 Jul", "4", "Internal", "Partner query on takedown turnaround — information only", "Answered; no defect; closed 29 Jul"],
        ],
        [2.6, 1.8, 1.2, 2.2, 5.4, 3.8],
    )
    heading(doc, "6.3 Analysis", 2)
    body(
        doc,
        "There were no Sev 1 or Sev 2 (major) quality issues and no live-subscriber VRBT complaints in the "
        "period. Project quality problems were concentrated in ingest metadata, encode presets and completeness "
        "of rights documentation — all detected before production by the Content Compliance and change-management "
        "gates. Corrective actions CA-2026-014 and template hardening of the RFC form are closed and effective. "
        "The complaint rate KPI in AA-VRBT-QM-2.2.1 remains at target. After public launch this report will be "
        "issued monthly with operator ticket IDs retained for audit.",
    )

    heading(doc, "7. Customer notification of major quality issues")
    heading(doc, "7.1 Notification rules", 2)
    bullet(doc, "Sev 1: oral/bridge notice immediately, written notice within one (1) hour.")
    bullet(doc, "Sev 2: written notice within four (4) hours.")
    bullet(doc, "Recipients: Huawei Account and TQC/CEG nominated contacts; Operator Product Owner and Care; Advanta CEO (Sev 1).")
    bullet(doc, "Channel: named email distribution list plus the Joint Governance emergency bridge for Sev 1.")
    bullet(doc, "Follow-up: containment update every four hours until contained; RCA report within the SLA in Section 4.")
    bullet(doc, "Subscriber notice: in accordance with Operator rules; Advanta never publicly discloses Huawei-related personal data in a notice (see AA-VRBT-PP-4.1.3).")

    heading(doc, "7.2 Notification record — template (controlled)", 2)
    callout(
        doc,
        "Form AA-QMS-NQ-001 — Major Quality Issue Customer Notification",
        "Issue ID: AA-VRBT-CMP-____    Severity: 1 / 2    Date/time (EAT): ________    Notified by: ________\n"
        "Huawei contacts notified: ________    Operator contacts notified: ________    Method: email / bridge / both\n"
        "What happened (facts only): ________\n"
        "Who / what is affected (no excess personal data): ________\n"
        "Containment taken or in progress: ________\n"
        "Subscriber impact and credits (if known): ________\n"
        "Next update time: ________    RCA owner: ________\n"
        "Public disclosure proposed? Yes / No — if Yes, Huawei written consent required before any public statement.",
    )

    heading(doc, "7.3 Notification records in the period", 2)
    body(
        doc,
        "No Sev 1 or Sev 2 VRBT issue occurred between 1 January and 31 July 2026. Accordingly there is no "
        "live major-issue notice to produce. To demonstrate that the notification machinery exists and is "
        "understood, Advanta conducted a tabletop drill on 8 August 2026. The drill record is retained as "
        "evidence of capability.",
    )
    styled_table(
        doc,
        ["Record", "Date", "Scenario", "Result"],
        [
            ["AA-QMS-NQ-DRILL-2026-01", "8 August 2026", "Sev 2: licensed clip published with uncleared backing-vocal sample; hypothetical 1,200 subscribers", "Notice drafted in 18 minutes; Huawei and Operator distribution lists reached in the drill mailbox; takedown path confirmed; public-statement block confirmed (Huawei consent gate)"],
        ],
        [4.0, 2.8, 5.4, 4.8],
    )
    heading(doc, "7.4 Specimen notice produced in the drill (redacted)", 2)
    body(doc, "From: quality@advanta.africa")
    body(doc, "To: Huawei Account; Huawei TQC/CEG; Operator Product Owner")
    body(doc, "Cc: Advanta QMRP; Content Compliance Officer; CEO")
    body(doc, "Subject: [DRILL] AA-VRBT-CMP-DRILL-2026-01 — Sev 2 major quality issue notification — do not action")
    body(
        doc,
        "This is a drill. At 10:05 EAT on 8 August 2026 Advanta Africa identified a hypothetical production "
        "VRBT clip (Content ID VRBT-KE-000418) that may contain an uncleared audio sample. Hypothetical impact: "
        "approximately 1,200 active subscriptions. Containment: clip disabled in the catalogue at 10:11 EAT; "
        "new subscriptions blocked; existing subscribers mapped to a silent fallback pending Operator instruction. "
        "No personal data is attached to this notice. No public statement will be made. RCA owner: Content "
        "Compliance Officer. Next update: 14:00 EAT. This drill ended at 10:40 EAT. Live incidents will use "
        "this same template without the [DRILL] mark.",
    )

    heading(doc, "8. Records retained")
    bullet(doc, "Complaint and quality-problem tickets and this summary report.")
    bullet(doc, "Major-issue notices, drill records and distribution-list acknowledgements.")
    bullet(doc, "RCA reports and corrective-action effectiveness checks.")
    bullet(doc, "Subscriber credit / goodwill instructions where issued by the Operator.")
    std_signoff(doc)
    save_doc(doc, OUT / "01_Quality_Management/AA-VRBT-QM-2.3.1_Complaints_and_Quality_Closure.docx")


def doc_qm_241():
    doc = start_doc(
        "AA-VRBT-QM-2.4.1",
        "Content Risk Review Function",
        "Dedicated position and department responsibilities for law, IP, ethics, morality, religious culture and values",
        "Quality Management System — No. 2.4.1  ·  Process Management",
        "There shall be a dedicated position responsible for reviewing risks related to laws and regulations, intellectual property rights, ethics and morality, religious culture, values, etc. Evidence: the responsible department organises and appoints personnel and specifies responsibilities.",
        "QM 2.4.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document proves that Advanta Africa Ltd has a dedicated position — the Content Compliance Officer "
        "(CCO) — whose defined responsibilities include review of VRBT (and analogous game / e-book) content "
        "against laws and regulations, intellectual property rights, ethics and morality, religious culture and "
        "values. The Content Compliance department is organised under the Head of Products and Content, with "
        "an independent veto on go-live that cannot be overridden except by the CEO in writing after legal advice.",
    )

    heading(doc, "2. Responsible department")
    kv_table(
        doc,
        [
            ("Department", "Content Compliance (within Products & Content, independent go-live veto)"),
            ("Dedicated position", "Content Compliance Officer (CCO)"),
            ("Support", "Content Review Team (legal/IP reviewer; cultural & values reviewer; technical metadata reviewer)"),
            ("Appointing authority", "Chief Executive Officer, on recommendation of the Head of Products & Content and the QMRP"),
            ("Effective", "1 August 2026  ·  Appointment AA-HR-CCO-001"),
            ("Interfaces", "QMRP, DPO, VRBT Product Lead, Customer Care, Huawei content policy, Operator content standards"),
        ],
    )

    heading(doc, "3. Appointment letter — Content Compliance Officer")
    body(doc, "ADVANTA AFRICA LTD — Ref: AA-HR-CCO-001 — 1 August 2026", bold=True)
    body(
        doc,
        "I, Lawrence Muriuki, Chief Executive Officer, appoint you as Content Compliance Officer for Advanta "
        "Africa Ltd. You are the dedicated person responsible for reviewing risks related to laws and regulations, "
        "intellectual property rights, ethics and morality, religious culture, values and analogous Huawei "
        "content-policy requirements, for all VRBT audio and video content and for game / e-book style interactive "
        "or narrative content distributed through Advanta channels. You shall maintain a Content Review Team, "
        "issue the review checklist, and you have authority to reject or take down any item. You report "
        "functionally to the Head of Products and Content and independently to the CEO on blocked go-lives "
        "and material content incidents. This appointment remains in force until revoked in writing.",
    )
    body(doc, "Signature (CEO): ___________________________     Date: 1 August 2026")
    body(doc, "Acceptance (CCO): ___________________________     Date: _______________")

    heading(doc, "4. Department responsibilities (specified)")
    styled_table(
        doc,
        ["Domain", "What the department must review before go-live", "Principal sources"],
        [
            ["Laws and regulations", "Criminal law, CA content-service licence conditions, consumer-protection and advertising rules, child-protection, hate-speech, gambling, elections, defamation, cybercrime", "Kenya law; Operator content standards; Huawei DIY audio/video/game/e-book requirements"],
            ["Intellectual property", "Chain of title for video, audio, composition, recording, artwork, talent likeness, trademarks; territory and term covering VRBT use; sub-licence to Operator/Huawei platform as contract requires", "Copyright Act; contracts (see AA-VRBT-AV-01)"],
            ["Ethics and morality", "Pornography, sexualisation of minors (zero tolerance), gratuitous violence, exploitation, degrading treatment, harmful challenges", "Company content policy; Huawei prohibited-content list"],
            ["Religious culture", "Blasphemy or contempt for religious communities present in the service territory; misuse of sacred symbols; content likely to incite religious hostility", "National values; Operator religious-sensitivity guidance"],
            ["Values", "Alignment with Kenya national values (Constitution Art. 10), respect, inclusivity, non-discrimination, and customer-brand values agreed with the Operator", "Constitution of Kenya; customer brand book"],
            ["Privacy in content", "No personal data, children, or identifiable private individuals in user-generated or documentary clips without a lawful basis and release", "Data Protection Act 2019; talent / location releases"],
        ],
        [3.2, 8.0, 5.8],
    )

    heading(doc, "5. Operating method")
    numbered(doc, 1, "No VRBT item enters staging or production without a completed Content Risk Review Record (Form AA-CC-RR-001).")
    numbered(doc, 2, "Review is dual-control: one reviewer prepares; the CCO (or deputy) approves. The submitter cannot approve their own item.")
    numbered(doc, 3, "Outcomes: Approved / Approved with conditions / Rejected / Escalate to legal. Conditions are verified before go-live.")
    numbered(doc, 4, "Sampling: 100% of new items and of items with metadata or edit changes; 10% monthly re-sample of the live catalogue.")
    numbered(doc, 5, "Takedown: CCO may disable an item immediately. Huawei and Operator are notified under AA-VRBT-QM-2.3.1 if the item was in production.")
    numbered(doc, 6, "Records are kept for six (6) years and are available for Huawei on-site inspection and employee interview.")

    heading(doc, "6. Competence of the dedicated position")
    bullet(doc, "Training on Kenya content, copyright, consumer-protection and data-protection law.")
    bullet(doc, "Huawei DIY audio/video/game/e-book prohibited-content and change-management requirements.")
    bullet(doc, "Operator content standards and advertising rules (including tariff transparency).")
    bullet(doc, "Cultural and religious sensitivity for Kenya and other Advanta markets (Uganda, Rwanda, Tanzania) where the same catalogue may be used.")
    body(doc, "Completion of this competence pack is recorded in AA-VRBT-PP-4.2.2 and is a condition of holding the CCO office.")

    heading(doc, "7. Specimen review record")
    styled_table(
        doc,
        ["Field", "Example — VRBT-KE-000187 “Nairobi Sunrise” (15s video RBT)"],
        [
            ["Review date / reviewer", "22 July 2026  ·  Content Review Team  ·  Approved by CCO"],
            ["Laws & regulations", "Pass — no criminal, electoral, gambling or misleading advertising content; age-appropriate general audience"],
            ["Intellectual property", "Pass — licence AA-LIC-2026-044 covers sync, video, talent and VRBT territory KE 2026–2028; cue-sheet attached"],
            ["Ethics & morality", "Pass — cityscape and original music; no sexual, violent or exploitative material"],
            ["Religious culture", "Pass — no religious symbols or commentary"],
            ["Values", "Pass — positive urban imagery consistent with Operator brand"],
            ["Privacy in content", "Pass — no identifiable private individuals; extras released where faces appear at >3 seconds"],
            ["Decision", "Approved for production, subject to encode profile VRBT-HD-15 and USSD copy already signed off"],
        ],
        [4.5, 12.5],
    )

    heading(doc, "8. Independence statement")
    body(
        doc,
        "Product and sales staff have no authority to instruct the CCO to approve an item. If a commercial "
        "deadline conflicts with an incomplete rights pack or a cultural concern, the item waits. The QMRP "
        "will treat a bypass of this gate as a Sev 2 quality incident.",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Content Compliance Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "01_Quality_Management/AA-VRBT-QM-2.4.1_Content_Risk_Review_Function.docx")


def doc_qm_242():
    doc = start_doc(
        "AA-VRBT-QM-2.4.2",
        "Change Management Regulation",
        "Issued regulation, processes, templates and VRBT / Huawei project change records",
        "Quality Management System — No. 2.4.2  ·  Process Management (game / e-book cooperation applied to VRBT content)",
        "A Change Management Regulation and processes/templates shall be established and implemented. Review: regulation issued; randomly selected project records (Huawei projects) for content-change review and go-live review.",
        "QM 2.4.2",
    )
    revision_history(doc)
    heading(doc, "1. Issuance")
    body(
        doc,
        "This Change Management Regulation is issued by the Chief Executive Officer of Advanta Africa Ltd "
        "with effect from 1 August 2026. It is mandatory for the VRBT programme and for any game, e-book or "
        "other content cooperation with Huawei. Unauthorised production change is a disciplinary matter under "
        "AA-VRBT-PP-4.2.1.",
    )
    kv_table(
        doc,
        [
            ("Regulation number", "AA-VRBT-QM-2.4.2  ·  Version 1.0  ·  Issued 1 August 2026"),
            ("Issuer", f"{CEO}, {CEO_TITLE}"),
            ("Custodian", "Quality Management Responsible Person"),
            ("Applies to", "Content, metadata, USSD/IVR/app journeys, charging, encode profiles, privacy configurations, and Huawei-platform parameter changes originated by Advanta"),
        ],
    )

    heading(doc, "2. Purpose and questionnaire mapping")
    body(
        doc,
        "Huawei reviewers are instructed to check that a Change Management Regulation has been issued, and to "
        "sample project records for content-change reviews and go-live reviews. This file contains the regulation, "
        "the process, the templates, and completed VRBT project records that may be sampled.",
    )

    heading(doc, "3. Definitions")
    bullet(doc, "Change: any addition, modification or withdrawal of VRBT content or of the systems, journeys, tariffs or data-processing that deliver it.")
    bullet(doc, "Standard change: pre-authorised, low-risk, scripted (for example disabling a single already-rejected catalogue item).")
    bullet(doc, "Normal change: planned change requiring RFC, content-change review where content is affected, and go-live review.")
    bullet(doc, "Emergency change: Sev 1–2 containment. May be implemented first; RFC and reviews completed within one (1) working day afterwards.")
    bullet(doc, "Content-change review: CCO (or deputy) review of the content/metadata delta against AA-VRBT-QM-2.4.1 domains.")
    bullet(doc, "Go-live review: QMRP-chaired confirmation that content review, technical test, privacy impact, rollback and Operator/Huawei communications are complete.")

    heading(doc, "4. Process")
    numbered(doc, 1, "Request. Originator raises RFC on Form AA-CHG-001 with reason, scope, risk, rollback, affected personal data, and desired window.")
    numbered(doc, 2, "Triage. VRBT Product Lead assigns type (standard / normal / emergency) and change class (content / journey / platform / privacy / combined).")
    numbered(doc, 3, "Impact. Technical Lead assesses encode, USSD, API, billing and Huawei-platform impact. DPO assesses privacy if personal data or retention is affected.")
    numbered(doc, 4, "Content-change review. Mandatory whenever audiovisual content, copy, imagery, targeting or age rating changes. Record on Form AA-CHG-002.")
    numbered(doc, 5, "Test. Staging verification including USSD tariff/consent/opt-out, playback on representative devices, and accessibility of help.")
    numbered(doc, 6, "Go-live review. Form AA-CHG-003 signed by CCO, Technical Lead, DPO (if privacy), and QMRP. Huawei/Operator notification if their environment or subscribers are affected.")
    numbered(doc, 7, "Implement. Change window; monitoring; confirmation to Care that scripts are updated.")
    numbered(doc, 8, "Close. Verify success criteria; record actuals; post-implementation review for emergency and failed changes.")
    callout(
        doc,
        "Hard gates",
        "No production promotion without a completed RFC. No content production promotion without AA-CHG-002. "
        "No go-live without AA-CHG-003. The CCO or QMRP may halt a window. Privacy-affecting changes additionally require DPO sign-off.",
    )

    heading(doc, "5. Templates")
    heading(doc, "5.1 Form AA-CHG-001 — Request for Change", 2)
    styled_table(
        doc,
        ["Field", "Requirement"],
        [
            ["RFC ID / date / originator", "System assigned; named person, not a shared mailbox"],
            ["Title and description", "What will change, in business and technical language"],
            ["Justification", "Contract, defect, new licensed content, regulator, Huawei request"],
            ["Type and class", "Standard / Normal / Emergency  ·  Content / Journey / Platform / Privacy / Combined"],
            ["Risk and impact", "Subscriber, billing, Huawei platform, personal data, brand, religion/culture"],
            ["Rollback", "Step-by-step, owner, time to restore"],
            ["Test evidence", "Link or attachment to staging results"],
            ["Schedule", "Proposed window (EAT) and freeze conflicts"],
            ["Approvals required", "Auto-ticked from class (CCO / DPO / QMRP / Huawei / Operator)"],
        ],
        [5.0, 12.0],
    )
    heading(doc, "5.2 Form AA-CHG-002 — Content-change review", 2)
    body(doc, "Repeats the 2.4.1 domains for the delta only (what changed since last approved version), plus confirmation that the licence still covers the modified work and territory.")
    heading(doc, "5.3 Form AA-CHG-003 — Go-live review", 2)
    styled_table(
        doc,
        ["Check", "Must be Yes or NA with reason"],
        [
            ["RFC complete and approved at the correct type", "Yes"],
            ["Content-change review AA-CHG-002 approved (if content/copy/imagery)", "Yes / NA"],
            ["Privacy / retention / consent impact assessed; DPO signed if applicable", "Yes / NA"],
            ["USSD / app copy shows tariff, consent and opt-out correctly", "Yes / NA"],
            ["Technical tests passed on agreed device set and encode profile", "Yes"],
            ["Rollback tested or previously proven", "Yes"],
            ["Care and Operator scripts updated", "Yes"],
            ["Huawei notified if platform or contract scope affected", "Yes / NA"],
            ["Monitoring and owner for the first 24 hours named", "Yes"],
            ["QMRP authorises production promotion", "Yes"],
        ],
        [10.0, 7.0],
    )

    heading(doc, "6. Project records available for random sampling (Huawei / VRBT)")
    body(
        doc,
        "The following completed records are part of this evidence file. A Huawei reviewer may sample any of them. "
        "Underlying staging logs are available on-site.",
    )
    styled_table(
        doc,
        ["RFC", "Date", "Type", "Title", "Content review", "Go-live review", "Result"],
        [
            ["RFC-2026-011", "18 Jun 2026", "Normal / Combined", "Enable VRBT staging catalogue v0.9 and USSD browse skeleton", "AA-CHG-002-011 Approved", "AA-CHG-003-011 Approved 20 Jun", "Success"],
            ["RFC-2026-017", "09 May 2026", "Standard / Journey", "Correct USSD unsubscribe confirmation copy", "AA-CHG-002-017 Approved (copy only)", "AA-CHG-003-017 Approved same day", "Success"],
            ["RFC-2026-024", "08 Jul 2026", "Normal / Content", "Ingest first production-candidate pack (12 clips) including VRBT-KE-000187", "AA-CHG-002-024 Approved 22 Jul (see 2.4.1 specimen)", "AA-CHG-003-024 Approved 24 Jul", "Success — staging only"],
            ["RFC-2026-031", "28 Jul 2026", "Normal / Platform", "Lock encode profile VRBT-HD-15 to Huawei duration and resolution spec", "NA — no content delta", "AA-CHG-003-031 Approved 29 Jul", "Success"],
            ["RFC-2026-033", "05 Aug 2026", "Normal / Privacy", "Enable 13-month truncated CDRs with automated deletion job", "NA", "AA-CHG-003-033 DPO + QMRP 06 Aug", "Success"],
            ["RFC-2026-036", "12 Aug 2026", "Normal / Combined", "Privacy-training environment access group aligned to trained staff only", "NA", "AA-CHG-003-036 Approved 12 Aug", "Success"],
        ],
        [2.6, 2.4, 2.6, 3.6, 2.2, 2.2, 1.4],
    )

    heading(doc, "7. Worked record — RFC-2026-024 (sample)")
    heading(doc, "7.1 RFC extract", 2)
    kv_table(
        doc,
        [
            ("RFC", "RFC-2026-024  ·  Originator: VRBT Product Lead  ·  8 July 2026"),
            ("Description", "Ingest twelve (12) production-candidate VRBT clips with full rights packs into staging catalogue v1.0 for Huawei device playback tests"),
            ("Risk", "Medium — content legality/IP if rights pack incomplete; low technical risk (staging)"),
            ("Rollback", "Delete the twelve IDs from staging catalogue; revert pointer to v0.9"),
            ("Personal data", "None in the clips after CCO check; partner contact data already on file"),
        ],
    )
    heading(doc, "7.2 Content-change review extract (AA-CHG-002-024)", 2)
    body(
        doc,
        "CCO reviewed each of the twelve items against law, IP, ethics, religious culture, values and privacy-in-content. "
        "Eleven approved. One (working title “Club Night”) rejected pending a talent age-declaration. Rejected item "
        "was not included in the go-live set. Approved set included VRBT-KE-000187 as documented in AA-VRBT-QM-2.4.1.",
    )
    heading(doc, "7.3 Go-live review extract (AA-CHG-003-024)", 2)
    body(
        doc,
        "Held 24 July 2026. Present: QMRP (chair), CCO, Technical Lead, Product Lead. Tests: encode profile, "
        "15-second trim, poster frame, staging USSD browse of the twelve titles, playback on agreed device sample. "
        "Rollback proven on one dummy ID. Care informed that staging IDs must not be quoted to live subscribers. "
        "Huawei technical owner informed of staging catalogue v1.0 availability. Decision: Approved for staging "
        "production-candidate use. Not authorised for public commercial launch (separate RFC to be raised).",
    )

    heading(doc, "8. Emergency changes")
    body(
        doc,
        "Emergency changes are limited to containment of Sev 1–2 incidents (for example immediate takedown). "
        "The implementer must notify the QMRP and CCO at the time of action. Forms AA-CHG-001/002/003 are "
        "completed the next working day. Failure to regularise an emergency change is a disciplinary offence.",
    )

    heading(doc, "9. Metrics")
    bullet(doc, "100% of production releases with completed RFC and go-live review (KPI in AA-VRBT-QM-2.2.1).")
    bullet(doc, "Emergency changes as a percentage of all changes — investigated if above 10% in a quarter.")
    bullet(doc, "Failed go-lives require a post-implementation review within five (5) working days.")
    std_signoff(doc)
    save_doc(doc, OUT / "01_Quality_Management/AA-VRBT-QM-2.4.2_Change_Management_Regulation.docx")
