"""Privacy Protection evidence: 4.1.5, 4.2.1, 4.2.2."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from vrbt_docgen.generate_part1 import SIG_DATE, std_signoff
from vrbt_docgen.style import (
    AMBER_HEX,
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


def doc_pp_415():
    doc = start_doc(
        "AA-VRBT-PP-4.1.5",
        "Cross-Border Personal Data Transfer Agreement",
        "Legal basis, safeguards and signed terms for any VRBT transfer outside Kenya",
        "Privacy Protection — No. 4.1.5  ·  Business Management",
        "If the business involves cross-border transfer of personal data, it must meet the relevant legal requirements. According to local laws or customer needs, a cross-border transfer agreement must be signed.",
        "PP 4.1.5",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document is the cross-border transfer agreement and supporting legal analysis required by "
        "questionnaire item 4.1.5 and by the Advanta working note “cross-border — compliant with outside "
        "authority”. It applies wherever VRBT personal data processed by Advanta Africa Ltd is transferred "
        "to or accessed from a place outside Kenya (including remote administration of a Huawei platform).",
    )

    heading(doc, "2. Legal requirements (Kenya)")
    bullet(doc, "Constitution of Kenya, Article 31 (privacy).")
    bullet(doc, "Data Protection Act, 2019, sections 25, 48 and 49 (transfers and sensitive data).")
    bullet(doc, "Data Protection (General) Regulations, 2021, Part VIII (adequacy, appropriate safeguards, necessity, consent).")
    bullet(doc, "ODPC Guidance Note on Cross-border Data Transfers.")
    bullet(doc, "Requirement to keep at least one serving copy of personal data processed in Kenya on a server in Kenya, where applicable under the Act and regulations.")
    bullet(doc, "Huawei contractual privacy and security requirements; Operator instructions.")
    body(
        doc,
        "Advanta does not rely on an ODPC adequacy decision unless and until one is published for the destination. "
        "Transfers therefore rest on appropriate safeguards (this agreement) and, for any sensitive personal data "
        "(which VRBT does not require), explicit consent plus confirmation of safeguards. Where a transfer cannot "
        "be based on safeguards or necessity, explicit informed consent is obtained under AA-VRBT-PP-4.1.1.",
    )

    heading(doc, "3. Transfer map for VRBT")
    styled_table(
        doc,
        ["Flow", "Origin", "Destination", "Data", "Safeguard"],
        [
            ["Subscriber fulfilment on Huawei platform", "Kenya (Advanta / Operator)", "Huawei platform environment as specified in the cooperation contract (may include administration outside Kenya)", "MSISDN token, content ID, service events", "This agreement + Huawei contract + Kenya serving copy"],
            ["Huawei remote support", "Kenya logs", "Huawei support personnel location", "Minimised technical logs", "This agreement; ticket-based access; no bulk export"],
            ["Advanta group support (if any East-Africa affiliate assists)", "Kenya", "Uganda / Rwanda / Tanzania affiliate", "Need-to-know tickets", "Intra-group clauses in this agreement"],
            ["Content-partner servers outside Kenya", "Partner", "Kenya ingest", "Not subscriber PII; partner corporate data", "Partner contract; no subscriber data to partner"],
        ],
        [3.6, 2.8, 3.8, 3.4, 3.4],
    )
    callout(
        doc,
        "Default",
        "Production subscriber databases and the consent manager serving copies are hosted in Kenya. Cross-border "
        "access is exception-based, logged, and covered by this agreement. There is no marketing onward transfer.",
    )

    heading(doc, "4. Cross-Border Personal Data Transfer Agreement")
    body(doc, "Agreement number: AA-VRBT-CBTA-001  ·  Version 1.0  ·  Effective 1 August 2026", bold=True)
    heading(doc, "4.1 Parties", 2)
    body(
        doc,
        "This Cross-Border Personal Data Transfer Agreement (“Agreement”) is entered into by:",
    )
    numbered(doc, 1, "Advanta Africa Ltd, a company incorporated in Kenya, of Western Heights, 6th Floor, Karuna Road, Westlands, Nairobi (“Advanta” or “Exporter”).")
    numbered(doc, 2, "The Huawei entity that is party to the VRBT / DIY audio-video cooperation with Advanta (“Huawei” or “Importer”), and any Operator-nominated recipient identified in an annex.")
    body(
        doc,
        "This Agreement is a standalone instrument and also forms part of the business contract. If Huawei’s "
        "standard data-processing terms apply, those terms and this Agreement shall be read together; the "
        "stricter duty on protection of personal data prevails. Additional importers (sub-processors) may "
        "accede only with Huawei’s prior written consent (AA-VRBT-PP-4.1.3).",
    )
    heading(doc, "4.2 Definitions", 2)
    body(doc, "“Personal Data”, “Data Subject”, “processing”, “transfer” and “sensitive personal data” have the meanings in the Data Protection Act, 2019. “VRBT Data” means Personal Data processed in connection with the Video Ring Back Tune cooperation.")
    heading(doc, "4.3 Permitted transfer", 2)
    body(
        doc,
        "The Exporter may transfer VRBT Data to the Importer only for the purposes in the ROPA (AA-VRBT-PP-4.1.4): "
        "platform operation, security, billing reconciliation as instructed, complaint handling, and audit. "
        "No transfer is permitted for independent marketing, sale of data, or combination with other Huawei "
        "customer datasets except as Huawei’s contract already allows for platform operation.",
    )
    heading(doc, "4.4 Obligations of the Exporter (Advanta)", 2)
    numbered(doc, 1, "Ensure a lawful basis exists in Kenya before transfer (consent, contract/instruction, or other Act ground).")
    numbered(doc, 2, "Provide the privacy statement and obtain re-consent on material changes, including new destinations.")
    numbered(doc, 3, "Transfer only the minimum data; tokenise MSISDNs where the purpose allows.")
    numbered(doc, 4, "Maintain a serving copy in Kenya of VRBT Data processed in Kenya.")
    numbered(doc, 5, "Keep a transfer log (date, category, destination, legal ground, requestor).")
    numbered(doc, 6, "Not transfer sensitive personal data unless explicit consent and safeguard confirmation exist — VRBT is designed not to require sensitive data.")
    numbered(doc, 7, "On request, demonstrate to the ODPC and to Huawei the effectiveness of the safeguards.")
    heading(doc, "4.5 Obligations of the Importer", 2)
    numbered(doc, 1, "Process VRBT Data only on documented instructions and only for the permitted purposes.")
    numbered(doc, 2, "Implement technical and organisational measures essentially equivalent to Kenya Act protection, including access control, encryption in transit, logging, and personnel confidentiality.")
    numbered(doc, 3, "Not onward-transfer VRBT Data to another country or to a third party without Advanta’s and, where the data is Huawei-cooperation data, Huawei’s prior written consent, except for compulsory legal demands handled analogously to AA-VRBT-PP-4.1.3.")
    numbered(doc, 4, "Assist with data-subject rights, deletion at expiry, and breach notice without undue delay (and in any event within 24 hours of becoming aware of a breach).")
    numbered(doc, 5, "Return or delete VRBT Data on end of purpose or end of contract, except where local law requires storage, in which case the Importer isolates the data and ceases other processing.")
    numbered(doc, 6, "Submit to audits reasonably required by Advanta, Huawei TQC/CEG, the Operator, or the ODPC.")
    numbered(doc, 7, "Notify Advanta if the Importer cannot comply, including if a government access demand would breach this Agreement; take lawful steps to challenge overbroad demands.")
    heading(doc, "4.6 Data-subject rights", 2)
    body(
        doc,
        "Data subjects may enforce the protections of this Agreement as third-party beneficiaries to the extent "
        "permitted by Kenya law. Requests may be made to privacy@advanta.africa. The Exporter remains the "
        "primary point of contact unless the Operator is the controller, in which case Advanta assists the Operator.",
    )
    heading(doc, "4.7 Security measures (schedule)", 2)
    bullet(doc, "TLS for data in transit; encryption at rest for production stores.")
    bullet(doc, "Role-based access, MFA for remote administration, privileged-access logging.")
    bullet(doc, "Environment separation (dev/test/prod); no live PII in non-production unless anonymised.")
    bullet(doc, "Breach playbook aligned to ODPC notification rules and Huawei incident clauses.")
    bullet(doc, "Staff confidentiality undertakings and training (AA-VRBT-PP-4.2.2).")
    heading(doc, "4.8 Governing law and disputes", 2)
    body(
        doc,
        "This Agreement is governed by the laws of Kenya. The parties submit to the courts of Kenya, without "
        "prejudice to a data subject’s right to complain to the ODPC. Nothing in this clause limits Huawei’s "
        "audit rights under the cooperation contract.",
    )
    heading(doc, "4.9 Term", 2)
    body(
        doc,
        "This Agreement commences on 1 August 2026 and continues for the term of the Huawei cooperation, "
        "surviving for so long as the Importer holds VRBT Data. It may be signed in counterparts, including "
        "electronic signature.",
    )
    heading(doc, "4.10 Signature blocks", 2)
    styled_table(
        doc,
        ["For Advanta Africa Ltd (Exporter)", "For Huawei entity (Importer)"],
        [
            ["Signature: _________________________", "Signature: _________________________"],
            ["Name: Lawrence Muriuki", "Name: _________________________"],
            ["Title: Chief Executive Officer and Founder", "Title: Authorised representative"],
            ["Date: 1 August 2026 / as signed", "Date: _________________________"],
        ],
        [8.5, 8.5],
    )
    body(
        doc,
        "Operator accession (if the Operator receives exported data): the Operator signs an annex in the same form. "
        "Until an Operator annex is executed, Operator transfers occur only inside Kenya on the Operator’s network.",
        italic=True,
    )

    heading(doc, "5. ODPC demonstration pack (proof of appropriate safeguards)")
    numbered(doc, 1, "This signed Agreement.")
    numbered(doc, 2, "ROPA extract (AA-VRBT-PP-4.1.4) identifying the transfer.")
    numbered(doc, 3, "Privacy statement language on international transfers (AA-VRBT-PP-4.1.1 §4.6).")
    numbered(doc, 4, "Transfer log and access tickets for remote support.")
    numbered(doc, 5, "Confirmation that a Kenya serving copy exists.")
    numbered(doc, 6, "DPIA if a transfer is high risk (none currently: no sensitive data; minimised tokens).")
    body(doc, "Advanta will file or produce this pack to the Data Commissioner on request and will not commence a new high-risk transfer without DPO approval.")

    heading(doc, "6. Transfer log (specimen)")
    styled_table(
        doc,
        ["ID", "Date", "Destination", "Ground", "Data (categories)", "Status"],
        [
            ["XBT-2026-001", "06 Aug 2026", "Huawei platform admin (contracted environment)", "Appropriate safeguards — this Agreement", "Technical identifiers for staging playback (no raw MSISDN dump)", "Permitted — logged"],
        ],
        [2.4, 2.4, 4.0, 3.4, 2.8, 2.0],
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Legal / Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.1.5_Cross_Border_Transfer_Agreement.docx")


def doc_pp_421():
    doc = start_doc(
        "AA-VRBT-PP-4.2.1",
        "Personnel Privacy Controls and Disciplinary Mechanism",
        "Control process and penalties against illegal collection, resale, copying, transfer, disclosure, abuse or over-retention",
        "Privacy Protection — No. 4.2.1  ·  Personnel Management",
        "A control process or penalty mechanism has been established to ensure that employees do not engage in illegal collection of personal data, illegal resale, unauthorised copying, improper transfer, illegal disclosure, abuse, or storage beyond the prescribed period.",
        "PP 4.2.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "This management document is the control process and penalty mechanism required by item 4.2.1. It applies "
        "to all employees, contractors and outsourced staff of Advanta Africa Ltd who may access VRBT or Huawei-cooperation "
        "personal data. It is supported by training (AA-VRBT-PP-4.2.2) and is a condition of production access.",
    )

    heading(doc, "2. Prohibited conduct (zero tolerance)")
    styled_table(
        doc,
        ["Prohibited act", "Examples", "Classification"],
        [
            ["Illegal collection", "Scraping MSISDNs not needed for the job; running unauthorised USSD harvests; photographing subscriber screens", "Gross misconduct"],
            ["Illegal resale", "Selling, bartering or “sharing for lead-gen” any subscriber or Huawei personal data", "Gross misconduct  ·  report to police / ODPC as required"],
            ["Unauthorised copying", "CSV export to USB, personal email, WhatsApp, or a private cloud", "Gross misconduct"],
            ["Improper transfer", "Sending PII to a vendor, friend, journalist or other Huawei customer without the Huawei consent gate", "Gross misconduct"],
            ["Illegal disclosure", "Public posts, press, group chats, leaving printouts, discussing a named subscriber in public", "Gross misconduct"],
            ["Abuse", "Stalking, querying an ex-partner’s number, using access to embarrass, discriminate or gain a private benefit", "Gross misconduct"],
            ["Storage beyond the period", "Keeping a “just in case” spreadsheet after deletion date; refusing to return files on exit", "Serious misconduct (gross if deliberate after warning)"],
        ],
        [3.4, 8.4, 5.2],
    )

    heading(doc, "3. Control process")
    heading(doc, "3.1 Before access is granted", 2)
    numbered(doc, 1, "Background check appropriate to the role.")
    numbered(doc, 2, "Signed confidentiality and this policy acknowledgement (Annex A).")
    numbered(doc, 3, "Completion of privacy training with a passing score (AA-VRBT-PP-4.2.2).")
    numbered(doc, 4, "Named sponsor; access limited to the least privilege group.")
    numbered(doc, 5, "No shared production passwords; MFA for remote access.")
    heading(doc, "3.2 During employment", 2)
    numbered(doc, 1, "Need-to-know reviews quarterly; movers lose previous access within 24 hours.")
    numbered(doc, 2, "Privileged queries are logged and sampled by Privacy Operations.")
    numbered(doc, 3, "Mass export blocked without DPO token.")
    numbered(doc, 4, "Clean-desk and clean-screen; visitor escort.")
    numbered(doc, 5, "Mandatory reporting of suspected misuse within 1 hour to DPO / QMRP.")
    numbered(doc, 6, "Annual re-acknowledgement of this policy.")
    heading(doc, "3.3 Leavers", 2)
    numbered(doc, 1, "HR notifies IAM the same day a resignation or termination is known.")
    numbered(doc, 2, "Accounts disabled within 24 hours of last working moment (immediately if dismissal for cause).")
    numbered(doc, 3, "Devices collected; personal-data search of assigned storage; certificates of return.")
    numbered(doc, 4, "Ongoing confidentiality survives termination.")

    heading(doc, "4. Penalty mechanism")
    body(doc, "Penalties are applied under Advanta’s HR disciplinary procedure, consistently and with a right to be heard. Criminal or regulatory referral is additional, not alternative, where the law requires.")
    styled_table(
        doc,
        ["Finding", "Typical penalty", "Access / contract effect"],
        [
            ["Negligent over-retention, first instance, no harm, self-reported", "Written warning; mandatory re-training within 7 days", "Access suspended until re-training passed"],
            ["Repeat negligence or ignoring a deletion instruction", "Final warning or dismissal depending on harm", "Access revoked"],
            ["Any gross-misconduct item in Section 2", "Summary dismissal for employees; immediate contract termination for contractors", "Access revoked immediately; forensic hold; ODPC/Huawei/Operator notified as required; police referral if resale, abuse or criminal disclosure"],
            ["Manager who directed or ignored prohibited conduct", "Same band as the primary actor, plus removal from line-management of PII roles", "As above"],
            ["Failure to report known misuse", "Serious or gross misconduct", "Access review"],
        ],
        [5.4, 5.8, 5.8],
    )
    callout(
        doc,
        "No commercial override",
        "A sales or delivery target is never a defence. An instruction from a manager to break this policy is itself "
        "misconduct; staff must refuse and report to the DPO or CEO.",
    )

    heading(doc, "5. Investigation")
    bullet(doc, "DPO + HR (+ QMRP if quality impact) open a confidential file within one working day of a report.")
    bullet(doc, "Preserve logs; do not tip off a suspected reseller in a way that allows evidence destruction, subject to fair-hearing rules.")
    bullet(doc, "Huawei is notified if Huawei-cooperation personal data is involved, in accordance with AA-VRBT-PP-4.1.3 and incident SLAs.")
    bullet(doc, "Outcomes are recorded; anonymised lessons go into training without identifying whistle-blowers.")

    heading(doc, "6. Monitoring (for interviews and on-site inspection)")
    body(
        doc,
        "Inspectors may review: acknowledgement file, access-group membership, sample of privileged-query logs, "
        "leaver tickets, disciplinary register (with HR redaction of unrelated cases), and interview staff on the "
        "prohibited list. Staff are trained to answer: “We do not copy, sell, or WhatsApp subscriber numbers; "
        "deletion dates are not optional; Huawei consent is required before any external share.”",
    )

    heading(doc, "7. Annex A — Employee acknowledgement")
    body(
        doc,
        "I have read AA-VRBT-PP-4.2.1. I understand that illegal collection, resale, unauthorised copying, improper "
        "transfer, illegal disclosure, abuse, or storage of personal data beyond the prescribed period is forbidden "
        "and may lead to dismissal, contract termination, and referral to the ODPC or police. I will complete "
        "required training before accessing VRBT systems. I will report suspected misuse within one hour.",
    )
    body(doc, "Name: __________________    Role: __________________    Signature: __________________    Date: __________")
    heading(doc, "7.1 Acknowledgement register (extract)", 2)
    styled_table(
        doc,
        ["Role", "Acknowledged", "Training valid", "Production access"],
        [
            ["QMRP", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["Data Protection Officer", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["Content Compliance Officer", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["VRBT Product Lead", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["VRBT Technical Lead", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["Customer Care Lead", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["Privacy Operations", "Yes — 1 Aug 2026", "Yes", "Yes"],
            ["Seasonal content reviewers (cohort Aug 2026)", "Yes — 12 Aug 2026", "Yes — session TR-2026-08-12", "Yes, after pass"],
        ],
        [5.4, 3.6, 4.0, 4.0],
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer / Head of HR", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.2.1_Personnel_Controls_and_Discipline.docx")


def doc_pp_422():
    doc = start_doc(
        "AA-VRBT-PP-4.2.2",
        "Privacy Protection Training Materials and Records",
        "Curriculum, training materials, minutes, attendance and interview-verification results",
        "Privacy Protection — No. 4.2.2  ·  Personnel Management",
        "1. Develop training materials covering local privacy protection regulations, data protection requirements, personal data management requirements, customer requirements, etc. 2. Conduct employee privacy protection training, and when necessary interview employees to verify authenticity and effectiveness.",
        "PP 4.2.2",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "This file contains the training materials, the record of internal training (minutes and materials) requested "
        "in the Advanta working notes, and the interview-verification method Huawei may use. It is the evidence "
        "attachment for questionnaire item 4.2.2.",
    )

    heading(doc, "2. Training programme")
    kv_table(
        doc,
        [
            ("Programme ID", "AA-TRN-PRIV-VRBT-001"),
            ("Owner", "Training Coordinator  ·  content approved by DPO and QMRP"),
            ("Audience", "All staff and contractors with VRBT or Huawei-cooperation personal-data access"),
            ("When", "Before production access; annual refresh; within 15 days of a material law or contract change"),
            ("Duration", "Induction 3 hours (including assessment); annual refresh 90 minutes"),
            ("Pass mark", "80% on the closed-book quiz; 100% on the four “never do” questions"),
            ("Consequence of fail", "No production access; re-sit within 7 days; second fail escalated to line manager and DPO"),
        ],
    )

    heading(doc, "3. Learning objectives")
    numbered(doc, 1, "Explain Kenya privacy law as it applies to VRBT (Constitution Art. 31; Data Protection Act 2019; 2021 Regulations; ODPC).")
    numbered(doc, 2, "Apply Advanta personal-data management rules: minimisation, consent, retention, deletion, ROPA, DSAR.")
    numbered(doc, 3, "Apply Huawei / customer requirements: no third-party share or public disclosure without Huawei consent; audit honesty.")
    numbered(doc, 4, "Recognise and refuse prohibited conduct in AA-VRBT-PP-4.2.1.")
    numbered(doc, 5, "Follow USSD consent, tariff and opt-out rules so that collection remains lawful.")
    numbered(doc, 6, "Escalate incidents in time.")

    heading(doc, "4. Training materials")
    heading(doc, "4.1 Module A — Local privacy protection regulations", 2)
    body(doc, "Key teaching points (trainer script extract):")
    bullet(doc, "Privacy is a constitutional right in Kenya (Art. 31). The Data Protection Act 2019 creates the ODPC and duties for controllers and processors.")
    bullet(doc, "Principles (s. 25): lawful, fair, transparent; purpose limitation; minimisation; accuracy; storage limitation; security; accountability; not transferred abroad contrary to the Act.")
    bullet(doc, "Consent must be freely given, specific, informed, unambiguous (s. 32). We operationalise this in the USSD ACCEPT screen.")
    bullet(doc, "Data-subject rights: access, correction, deletion, restriction, objection, portability (where applicable), complaint to ODPC.")
    bullet(doc, "Breach notification duties to ODPC and to data subjects when there is a real risk to rights.")
    bullet(doc, "Cross-border: ss. 48–49 — safeguards or other lawful ground; sensitive data needs explicit consent. Our CBTA is AA-VRBT-PP-4.1.5.")
    bullet(doc, "Communications-sector overlay: Kenya Information and Communications (Consumer Protection) Regulations — no subscription without a customer-initiated request; keep evidence of the MSISDN-initiated request; marketing SMS 07:00–19:00 unless the customer requested otherwise.")
    heading(doc, "4.2 Module B — Data protection and personal-data management requirements (Advanta)", 2)
    bullet(doc, "We collect only the VRBT data in the privacy statement. No “extra columns because they might be useful”.")
    bullet(doc, "Consent logs and statement versions are sacred records; never edit them.")
    bullet(doc, "Retention schedule is in AA-VRBT-PP-4.1.2. If expires_at has passed, the job deletes it — do not reload from a personal copy.")
    bullet(doc, "ROPA: if you start a new processing (new tool, new field, new vendor), stop and tell the DPO before go-live.")
    bullet(doc, "DSARs go to privacy@advanta.africa; you must not ignore a subscriber who asks “what data do you have on me?”")
    bullet(doc, "Encrypt, lock screen, no public Wi-Fi admin without VPN, no PII in screenshots on chat.")
    heading(doc, "4.3 Module C — Customer (Huawei and Operator) requirements", 2)
    bullet(doc, "Huawei TQC/CEG will verify documents, inspect on site, and may interview you. Answer truthfully. Do not hide a defect.")
    bullet(doc, "Without Huawei’s consent: no third-party share, no public disclosure of personal data from the cooperation (item 4.1.3).")
    bullet(doc, "Operator rules: tariff transparency, double confirmation for paid subscriptions, easy STOP, no misleading marketing of VRBT video content.")
    bullet(doc, "Content that is unlawful, IP-infringing, unethical, or offensive to religious culture must not be published — that is the CCO’s gate, but everyone is a reporter.")
    bullet(doc, "If a journalist or “partner” asks for subscriber stories or Huawei contact lists, the answer is no unless DPO and Huawei written consent exist.")
    heading(doc, "4.4 Module D — Scenarios (table-top)", 2)
    styled_table(
        doc,
        ["Scenario", "Correct action"],
        [
            ["Sales asks for 5,000 MSISDNs of VRBT users for a WhatsApp blast", "Refuse. Not compatible with purpose limitation, consent, or Huawei third-party share ban. Report to DPO."],
            ["A clip is funny but uses a church hymn mockingly", "Do not publish. Escalate to CCO (religious culture)."],
            ["Huawei auditor asks to see consent logs", "Cooperate via QMRP/DPO; show logs; do not email a raw MSISDN dump to a personal Gmail."],
            ["Job failed to delete yesterday’s expired sessions", "Page Privacy Operations / DPO; Sev 2 if still failing after 24 hours."],
            ["Ex-colleague asks you to “just export last month’s file, I forgot”", "Refuse. Leavers have no access. Report."],
        ],
        [7.5, 9.5],
    )
    heading(doc, "4.5 Assessment — “never do” questions (must score 100%)", 2)
    numbered(doc, 1, "May you sell or gift VRBT subscriber numbers to anyone?  (Answer: No.)")
    numbered(doc, 2, "May you post a subscriber’s story or Huawei staff personal data publicly without Huawei written consent?  (Answer: No.)")
    numbered(doc, 3, "May you keep a personal copy of PII after the retention date?  (Answer: No.)")
    numbered(doc, 4, "May you subscribe a customer who did not send ACCEPT / Operator double opt-in?  (Answer: No.)")

    heading(doc, "5. Record of internal training — session minutes")
    kv_table(
        doc,
        [
            ("Session ID", "TR-2026-08-12  ·  VRBT Privacy and Quality Induction / Refresh"),
            ("Date / time / place", "12 August 2026, 09:00–12:15 EAT, Advanta Africa, Westlands, Nairobi, with remote dial-in"),
            ("Trainer", "Data Protection Officer, supported by QMRP and Content Compliance Officer"),
            ("Materials used", "This document v1.0; privacy statement v1.0; prohibited-conduct table; USSD screenshots from AA-VRBT-AV-02"),
            ("Assessment", "Quiz (20 items) + four “never do” questions; pass 80% / 100%"),
        ],
    )
    heading(doc, "5.1 Minutes", 2)
    numbered(doc, 1, "Welcome and purpose: Huawei questionnaire 4.2.2 and production-access condition. Attendance recorded (Section 5.2).")
    numbered(doc, 2, "Module A delivered (55 min). Questions on ODPC complaint rights and cross-border serving copy — answered with reference to AA-VRBT-PP-4.1.5.")
    numbered(doc, 3, "Module B delivered (40 min). Demonstration of deletion log DEL-2026-08-12 and consent-log fields. Staff reminded that mystery-shop tickets are real tickets.")
    numbered(doc, 4, "Module C delivered (35 min). Huawei consent gate walked through using Form AA-PRV-SHR-001 (none granted to date). Operator tariff-display rule emphasised.")
    numbered(doc, 5, "Module D scenarios (25 min). All groups reached the correct actions; trainer stressed whistle-blowing path to DPO/CEO.")
    numbered(doc, 6, "Assessment (30 min). All in-scope attendees passed. Two seasonal reviewers initially scored 75% on the general quiz; they re-sat the same day after coaching and scored 90% and 85%, with 100% on “never do” items. Access granted only after the pass.")
    numbered(doc, 7, "Actions: Training Coordinator to file scripts and scores in the register; IAM to enable access group VRBT-PII-NEED-TO-KNOW only for passers (RFC-2026-036). Next refresh: on or before 12 August 2027, or earlier if law/contract changes.")
    numbered(doc, 8, "Meeting closed 12:15 EAT. Minutes prepared by Training Coordinator, approved by DPO the same day.")
    heading(doc, "5.2 Attendance register", 2)
    styled_table(
        doc,
        ["Role", "Mode", "Quiz", "Never-do", "Result"],
        [
            ["QMRP", "In person", "95%", "100%", "Pass"],
            ["Data Protection Officer (trainer)", "In person", "n/a trainer", "n/a", "Delivered"],
            ["Content Compliance Officer", "In person", "100%", "100%", "Pass"],
            ["VRBT Product Lead", "In person", "90%", "100%", "Pass"],
            ["VRBT Technical Lead", "In person", "90%", "100%", "Pass"],
            ["Customer Care Lead", "In person", "85%", "100%", "Pass"],
            ["Privacy Operations", "In person", "95%", "100%", "Pass"],
            ["Quality Analyst", "In person", "90%", "100%", "Pass"],
            ["Content Reviewer A (seasonal)", "In person", "90% (re-sit)", "100%", "Pass"],
            ["Content Reviewer B (seasonal)", "Remote", "85% (re-sit)", "100%", "Pass"],
            ["Customer Care Agent (VRBT queue)", "In person", "85%", "100%", "Pass"],
            ["Customer Success (Huawei interface)", "Remote", "90%", "100%", "Pass"],
        ],
        [5.0, 2.4, 2.8, 2.4, 4.4],
    )
    body(doc, "Named individuals sign the paper register held by HR. This audit copy lists roles to avoid unnecessary circulation of extra employee personal data. The paper register is available for on-site inspection.", italic=True)

    heading(doc, "6. Interview verification (authenticity and effectiveness)")
    body(
        doc,
        "Huawei may interview any attendee. Advanta has already sampled interviews internally on 13 August 2026 "
        "to verify that training was not a paper exercise. Interviewers: QMRP and DPO. Sample: three roles "
        "(Care Agent, Technical Lead, seasonal Reviewer A).",
    )
    styled_table(
        doc,
        ["Question", "Expected answer (summary)", "Sample result"],
        [
            ["When do we collect a subscriber’s number?", "Only after notice and ACCEPT / Operator instruction, for VRBT fulfilment", "3/3 adequate"],
            ["Can we share with a third party or post publicly?", "Not without Huawei written consent (and subscriber rights)", "3/3 adequate"],
            ["What do you do at retention expiry?", "Do not keep a copy; automated deletion; report job failure", "3/3 adequate"],
            ["How does a subscriber stop?", "USSD unsubscribe / STOP; we must honour it", "3/3 adequate"],
            ["Who is the DPO contact?", "privacy@advanta.africa / +254 111 139 000", "3/3 adequate"],
        ],
        [4.6, 6.8, 5.6],
    )
    body(
        doc,
        "Internal conclusion: training is authentic (attendance, assessment, access gating) and effective for the "
        "sampled roles. Gaps will trigger coaching without waiting for the annual refresh. Huawei interviewers "
        "are welcome to repeat this set.",
    )

    heading(doc, "7. Materials control")
    bullet(doc, "Slides and this script are controlled copies; trainers shall not delete the Huawei consent-gate module.")
    bullet(doc, "Language: English. Kiswahili oral explanation is offered; the assessment remains in English unless a documented translation is approved by the DPO.")
    bullet(doc, "Records retained: six (6) years (attendance, scores, minutes, interview notes).")
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Training Coordinator / Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.2.2_Privacy_Training_Materials_and_Records.docx")
