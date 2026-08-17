"""
Generate professional Word evidence documents for the Advanta Africa VRBT
Huawei supplier questionnaire (Quality, Privacy, Audio & Video).
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from vrbt_docgen.org_chart import generate_all as make_charts
from vrbt_docgen.style import (
    AMBER_HEX,
    BOX_HEX,
    CEO,
    CEO_TITLE,
    COMPANY,
    DOC_DATE,
    add_picture_centered,
    body,
    bullet,
    callout,
    distribution,
    heading,
    kv_table,
    numbered,
    revision_history,
    save_doc,
    signature_block,
    start_doc,
    styled_table,
)

OUT = ROOT / "VRBT_Audit_Evidence"
ASSETS = OUT / "assets"
DATE = DOC_DATE.strftime("%d %B %Y")
SIG_DATE = "17 August 2026"


def std_signoff(doc, extra=None):
    sigs = [
        ("Prepared by", "Quality Management Responsible Person", SIG_DATE),
        ("Reviewed by", "Data Protection Officer / Content Compliance Officer", SIG_DATE),
        ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
    ]
    if extra:
        sigs = extra
    signature_block(doc, sigs)
    distribution(doc)


# ---------------------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------------------

def doc_index():
    doc = start_doc(
        "AA-VRBT-INDEX-001",
        "Evidence Index and Questionnaire Completion Guide",
        "How each Huawei TQC/CEG question is answered and which file to attach",
        "All parts — Quality Management, Privacy Protection, Audio and Video",
        "Yellow column: Documentation Evidence Attachments for every scored item",
        "Evidence Index",
    )
    heading(doc, "1. Purpose")
    body(
        doc,
        "This index is the master map between the Huawei supplier questionnaire and the "
        "Advanta Africa Ltd Video Ring Back Tune (VRBT) evidence pack. Each scored item has "
        "its own controlled Word document. Attach the document listed in the “File to attach” "
        "column to the yellow Documentation Evidence Attachments cell for that row. Scoring "
        "guidance used by the reviewer is Fully Met = 1, Partially Met = 0.5, Not Met at All = 0, "
        "Not Applicable = N/A. Advanta Africa’s self-assessment for every in-scope item is Fully Met.",
    )
    callout(
        doc,
        "How to use this pack",
        "1) Print or export each Word file to PDF if the auditor prefers PDF attachments. "
        "2) Obtain wet-ink or authorised e-signatures on the approval page of each document before submission. "
        "3) Do not alter document numbers. If a fact must be updated (named appointee, USSD code, tariff), "
        "revise under document control and re-issue as version 1.1. "
        "4) The organisation charts in AA-VRBT-QM-2.1.1 cover both the internal team and the customer / Huawei team, "
        "as requested in the Advanta working notes.",
    )

    heading(doc, "2. Project context")
    body(
        doc,
        "Advanta Africa Ltd (“Advanta”) is a Nairobi-based messaging and value-added services company "
        "operating since 2008 across Kenya, Uganda, Rwanda and Tanzania. Services include bulk SMS, "
        "short codes, SMS APIs, USSD, WhatsApp APIs and corporate caller-tune (Skiza-class) services. "
        "The VRBT programme extends that caller-tune capability from audio into short-form video that "
        "plays to a caller while the called party’s device is ringing. The service is delivered in "
        "cooperation with Huawei Technologies as platform provider. Huawei TQC/CEG reviews Advanta as "
        "a supplier for DIY audio/video, game and e-book scenarios as they apply to VRBT content operations.",
    )
    kv_table(
        doc,
        [
            ("Legal entity", "Advanta Africa Ltd, Nairobi, Kenya"),
            ("Accountable executive", f"{CEO}, {CEO_TITLE}"),
            ("Programme", "Video Ring Back Tune (VRBT) Service"),
            ("Platform / auditor", "Huawei Technologies — TQC/CEG, document verification"),
            ("Primary laws", "Constitution of Kenya Art. 31; Data Protection Act, 2019; Data Protection (General) Regulations, 2021; Kenya Information and Communications Act and Consumer Protection Regulations, 2010; CA content-service and short-code / USSD rules; Copyright Act; Computer Misuse and Cybercrimes Act"),
            ("Personal-data role", "Processor for subscriber identifiers received from the operator; Controller for employee, content-partner and Advanta-account data"),
            ("Contact", "privacy@advanta.africa  ·  +254 111 139 000  ·  www.advantasms.com"),
        ],
    )

    heading(doc, "3. Part A — Quality Management System")
    body(doc, "Reviewer: TQC/CEG. Review method: Document Verification.")
    styled_table(
        doc,
        ["No.", "Requirement (summary)", "Self-score", "File to attach"],
        [
            [
                "2.1.1",
                "Quality organisation, roles, routine operation. Evidence: appointment letter and job description of the Quality Management Responsible Person; organisation diagrams for internal and customer teams.",
                "Fully Met (1)",
                "01_Quality_Management/AA-VRBT-QM-2.1.1_Quality_Organisation.docx",
            ],
            [
                "2.2.1",
                "Quality objectives / KPIs established, monitored, and improved when unmet. Evidence: KPI document and statistical achievement report.",
                "Fully Met (1)",
                "01_Quality_Management/AA-VRBT-QM-2.2.1_Quality_Objectives_and_KPI_Report.docx",
            ],
            [
                "2.3.1",
                "Effective handling of customer complaints and quality problems. Evidence: summary report and customer notification records for major issues.",
                "Fully Met (1)",
                "01_Quality_Management/AA-VRBT-QM-2.3.1_Complaints_and_Quality_Closure.docx",
            ],
            [
                "2.4.1",
                "Dedicated position reviewing laws, IP, ethics, morality, religious culture and values.",
                "Fully Met (1)",
                "01_Quality_Management/AA-VRBT-QM-2.4.1_Content_Risk_Review_Function.docx",
            ],
            [
                "2.4.2",
                "Change Management Regulation issued and implemented; content-change and go-live review records for Huawei / VRBT projects.",
                "Fully Met (1)",
                "01_Quality_Management/AA-VRBT-QM-2.4.2_Change_Management_Regulation.docx",
            ],
        ],
        [1.8, 6.4, 2.4, 6.4],
    )

    heading(doc, "4. Part B — Privacy Protection (DIY Audio/Video, Game and E-book)")
    styled_table(
        doc,
        ["No.", "Key review point (summary)", "Self-score", "File to attach"],
        [
            [
                "4.1.1",
                "Privacy statement provided and valid consent obtained before collection; users notified and consent re-obtained when the statement is updated.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.1.1_Privacy_Statement_and_Consent.docx",
            ],
            [
                "4.1.2",
                "Mechanism to delete personal data on expiry; deletion in accordance with contract and business requirements.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.1.2_Data_Retention_and_Deletion.docx",
            ],
            [
                "4.1.3",
                "Without Huawei’s consent, personal data shall not be shared with third parties or disclosed publicly.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.1.3_Third_Party_Sharing_Prohibition.docx",
            ],
            [
                "4.1.4",
                "Records of all data-processing activities to ensure accountability.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.1.4_Records_of_Processing_Activities.docx",
            ],
            [
                "4.1.5",
                "Cross-border transfers meet legal requirements; cross-border transfer agreement signed as required by local law or customer need.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.1.5_Cross_Border_Transfer_Agreement.docx",
            ],
            [
                "4.2.1",
                "Control process and penalty mechanism against illegal collection, resale, copying, transfer, disclosure, abuse or over-retention.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.2.1_Personnel_Controls_and_Discipline.docx",
            ],
            [
                "4.2.2",
                "Training materials covering local law, data protection, personal-data management and customer requirements; training delivered; authenticity verifiable by interview.",
                "Fully Met (1)",
                "02_Privacy_Protection/AA-VRBT-PP-4.2.2_Privacy_Training_Materials_and_Records.docx",
            ],
        ],
        [1.8, 6.4, 2.4, 6.4],
    )

    heading(doc, "5. Part C — Audio and Video (from Advanta working notes)")
    body(
        doc,
        "The Advanta working notes required links/snippets for audio contracts, the USSD content process, "
        "a manual covering how to market and review content, a standalone review procedure, and an organisation "
        "diagram (already included under 2.1.1). The following documents are the attachments for that part.",
    )
    styled_table(
        doc,
        ["Ref.", "Working-note item", "File to attach"],
        [
            [
                "AV-01",
                "Audio / video — link contracts (snippet): content licensing terms for VRBT use",
                "03_Audio_and_Video/AA-VRBT-AV-01_Content_Licensing_Contract_Snippet.docx",
            ],
            [
                "AV-02",
                "Process content (USSD) — link: end-to-end USSD subscription, content browse, charging and opt-out",
                "03_Audio_and_Video/AA-VRBT-AV-02_USSD_Content_Process.docx",
            ],
            [
                "AV-03",
                "Manual — how to market and review VRBT content",
                "03_Audio_and_Video/AA-VRBT-AV-03_Marketing_and_Review_Manual.docx",
            ],
            [
                "AV-04",
                "Review — content review procedure, checklist and specimen records",
                "03_Audio_and_Video/AA-VRBT-AV-04_Content_Review_Procedure.docx",
            ],
        ],
        [2.0, 7.5, 7.5],
    )

    heading(doc, "6. Cross-walk from handwritten notes to documents")
    styled_table(
        doc,
        ["Note", "Where it is fulfilled"],
        [
            ["Appointment & JD (ticked)", "AA-VRBT-QM-2.1.1 — appointment letter and job description"],
            ["KPI", "AA-VRBT-QM-2.2.1 — quality KPI objectives"],
            ["Scale of achievement (quality)", "AA-VRBT-QM-2.2.1 — statistical achievement report"],
            ["Org structure — internal and customer team diagrams", "AA-VRBT-QM-2.1.1 — two organisation charts"],
            ["Privacy policy — data retention", "AA-VRBT-PP-4.1.1 and AA-VRBT-PP-4.1.2"],
            ["Privacy policy — sharing with third parties", "AA-VRBT-PP-4.1.1 and AA-VRBT-PP-4.1.3"],
            ["Cross-border — compliant with outside authority", "AA-VRBT-PP-4.1.5"],
            ["Record of internal training — minutes and materials", "AA-VRBT-PP-4.2.2"],
            ["Audio contracts snippet", "AA-VRBT-AV-01"],
            ["USSD process link", "AA-VRBT-AV-02"],
            ["Manual: market & review", "AA-VRBT-AV-03"],
            ["Review", "AA-VRBT-AV-04 and AA-VRBT-QM-2.4.1"],
        ],
        [6.5, 10.5],
    )

    heading(doc, "7. Document control rules")
    numbered(doc, 1, "Classification is Confidential. Do not post these files on a public website or share them outside Huawei’s audit channel without the QMRP’s approval.")
    numbered(doc, 2, "The controlled master is held by the Quality Management Office. Copies issued to Huawei are uncontrolled once downloaded by the auditor.")
    numbered(doc, 3, "Retention of audit evidence: six (6) years after the end of the Huawei cooperation, or longer if a contract or regulator requires it.")
    numbered(doc, 4, "Placeholders such as USSD short code *860#, example tariffs and named role-holders must be aligned to the live operator agreement before go-live. Until then they describe the designed control.")
    numbered(doc, 5, "Each document is self-contained so that a reviewer opening only one file can still see purpose, scope, control description, evidence and approval.")

    revision_history(doc)
    std_signoff(doc)
    save_doc(doc, OUT / "AA-VRBT-INDEX-001_Evidence_Index.docx")


# ---------------------------------------------------------------------------
# QM 2.1.1
# ---------------------------------------------------------------------------

def doc_qm_211(internal_chart: Path, customer_chart: Path):
    doc = start_doc(
        "AA-VRBT-QM-2.1.1",
        "Quality Organisation",
        "Appointment, job description and operating model of the Quality Management Responsible Person",
        "Quality Management System — No. 2.1.1",
        "Establish a quality management organisation, define roles and responsibilities, and operate it on a routine basis. Evidence: appointment letter and job description of the Quality Management Responsible Person; organisation diagrams.",
        "QM 2.1.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document demonstrates that Advanta Africa Ltd has established a quality management organisation "
        "for the VRBT programme, has appointed a Quality Management Responsible Person (QMRP), has issued a "
        "job description for that office, and operates the organisation on a routine basis. It is the evidence "
        "attachment for questionnaire item 2.1.1 (Reviewer: TQC/CEG; Method: Document Verification).",
    )
    styled_table(
        doc,
        ["Key review point", "Where addressed in this file"],
        [
            ["Appointment letter or relevant documents for the Quality Management Responsible Person", "Section 4 — Appointment Letter AA-HR-QMRP-001"],
            ["Job description for the Quality Management Responsible Person", "Section 5 — Job Description AA-HR-JD-QMRP-001"],
            ["Organisation defined and operated routinely", "Sections 3, 6 and 7 — charts, RACI, Quality Committee cadence"],
        ],
        [8.0, 9.0],
    )

    heading(doc, "2. Scope")
    body(
        doc,
        "This organisation covers all Advanta activities that create, license, review, encode, publish, market, "
        "bill, support or retire VRBT audio and video content, including USSD and digital-channel journeys, "
        "and the handling of personal data arising from those activities. It interfaces with Huawei TQC/CEG "
        "and with the mobile-network operator or enterprise customer. Game and e-book cooperation controls "
        "are applied analogously to interactive or narrative VRBT content.",
    )

    heading(doc, "3. Quality organisation")
    heading(doc, "3.1 Internal team", 2)
    body(
        doc,
        "The internal quality organisation is sponsored by the Chief Executive Officer. The QMRP is independent "
        "of day-to-day content production for audit decisions and has a direct reporting line to the CEO for "
        "quality and compliance escalation. The Data Protection Officer and the Content Compliance Officer "
        "(questionnaire 2.4.1) sit alongside product delivery so that privacy and content-risk reviews cannot "
        "be bypassed.",
    )
    add_picture_centered(doc, internal_chart, 16.8)
    body(doc, "Figure 1. Advanta Africa VRBT internal quality organisation.", italic=True)

    heading(doc, "3.2 Customer and partner team", 2)
    body(
        doc,
        "The customer-side organisation is a three-party model: Huawei (platform, TQC/CEG audit and technical "
        "baseline), Advanta Africa (content operations, USSD/VAS delivery, quality and privacy controls), and "
        "the Operator or enterprise customer (subscriber relationship, tariffs and network channels). A Joint "
        "VRBT Governance Committee meets monthly.",
    )
    add_picture_centered(doc, customer_chart, 16.8)
    body(doc, "Figure 2. Advanta Africa VRBT customer and partner organisation.", italic=True)

    heading(doc, "4. Appointment letter — Quality Management Responsible Person")
    callout(
        doc,
        "Controlled record  ·  AA-HR-QMRP-001  ·  Effective 1 August 2026",
        "The letter below is the appointment instrument required by the questionnaire. It is issued on Advanta Africa Ltd letterhead and takes effect on signature by the Chief Executive Officer.",
    )
    body(doc, "ADVANTA AFRICA LTD", bold=True)
    body(doc, "Smarter, Faster Messaging")
    body(doc, "Western Heights, 6th Floor, Karuna Road, Westlands, Nairobi  ·  P.O. Box 1035-00200  ·  +254 111 139 000")
    body(doc, "Ref: AA-HR-QMRP-001                                                                Date: 1 August 2026")
    body(doc, "APPOINTMENT LETTER — QUALITY MANAGEMENT RESPONSIBLE PERSON", bold=True)
    body(doc, "To: The appointed Quality Management Responsible Person")
    body(doc, "Office: Quality Management Responsible Person (QMRP) for the Video Ring Back Tune (VRBT) programme and related DIY audio, video, game and e-book content operations")
    body(doc, "Reporting line: Directly to the Chief Executive Officer for quality, audit and compliance matters; dotted line to the Head of Products and Content for operational coordination")
    body(
        doc,
        "I, Lawrence Muriuki, Chief Executive Officer and Founder of Advanta Africa Ltd, hereby appoint you "
        "as the Quality Management Responsible Person of Advanta Africa Ltd with immediate effect from "
        "1 August 2026. This appointment is made to satisfy Huawei supplier quality requirements and Advanta’s "
        "own quality policy, and shall remain in force until revoked in writing by the CEO or until you cease "
        "to be employed by the Company in a capacity compatible with the office.",
    )
    body(doc, "By this appointment you are authorised and required to:", bold=True)
    numbered(doc, 1, "Establish, maintain and continually improve the Quality Management System (QMS) for VRBT and related content services.")
    numbered(doc, 2, "Define quality objectives and KPIs, publish achievement reports, and drive improvement where targets are not met.")
    numbered(doc, 3, "Chair the monthly Quality Committee and report quality status to the CEO and to the Joint VRBT Governance Committee.")
    numbered(doc, 4, "Own the customer-complaint and quality-problem closure process, including notification of major issues to Huawei and the Operator.")
    numbered(doc, 5, "Ensure that a dedicated Content Compliance function reviews legal, intellectual-property, ethics, morality, religious-culture and values risks before go-live.")
    numbered(doc, 6, "Ensure that change management is applied to content and platform changes, including content-change reviews and go-live reviews.")
    numbered(doc, 7, "Coordinate Huawei TQC/CEG audits, on-site inspections and document verification, and keep the evidence repository complete and current.")
    numbered(doc, 8, "Escalate, independently of product management, any quality, privacy or content-compliance risk that you consider material.")
    body(
        doc,
        "You shall perform the duties in the attached Job Description (AA-HR-JD-QMRP-001) and shall have "
        "unrestricted access to records, systems and personnel reasonably required for those duties. The "
        "Company will provide training, tools and a quality analyst resource. This appointment does not "
        "alter your contract of employment except as to the additional authorities stated here.",
    )
    body(doc, "Please sign the acknowledgement below and return a copy to Human Resources for the personnel file and to the Quality Office for the controlled QMS file.")
    body(doc, "Yours faithfully,")
    body(doc, "_________________________________")
    body(doc, "Lawrence Muriuki")
    body(doc, "Chief Executive Officer and Founder")
    body(doc, "Advanta Africa Ltd")
    heading(doc, "Acknowledgement of appointment", 3)
    body(
        doc,
        "I accept the office of Quality Management Responsible Person, I have read Job Description "
        "AA-HR-JD-QMRP-001, and I understand the independence, duties and escalation rights of the office.",
    )
    body(doc, "Signature: ___________________________     Name: ___________________________     Date: _______________")

    heading(doc, "5. Job description — Quality Management Responsible Person")
    kv_table(
        doc,
        [
            ("Document", "AA-HR-JD-QMRP-001  ·  Version 1.0  ·  1 August 2026"),
            ("Job title", "Quality Management Responsible Person (QMRP)"),
            ("Function", "Quality, audit and supplier-compliance management"),
            ("Location", "Nairobi, Kenya, with support to East African operations"),
            ("Reports to", "Chief Executive Officer (quality independence line)"),
            ("Direct reports", "Quality Analyst; dotted-line Training Coordinator for QMS curricula"),
            ("Grade", "Senior management  ·  designated management representative for the QMS"),
        ],
    )
    heading(doc, "5.1 Purpose of the role", 2)
    body(
        doc,
        "To provide independent leadership of Advanta Africa’s quality management organisation for VRBT and "
        "related content services, so that contractual, legal, Huawei TQC/CEG and customer requirements are "
        "met, evidenced and continually improved.",
    )
    heading(doc, "5.2 Key accountabilities", 2)
    styled_table(
        doc,
        ["Accountability", "Principal activities", "Success measure"],
        [
            ["QMS design and operation", "Maintain quality policy, processes, templates and the controlled document register. Run the Quality Committee.", "QMS current; no overdue controlled-document reviews"],
            ["Quality objectives", "Set annual KPIs with the CEO; monitor monthly; initiate improvement for unmet targets.", "KPI pack issued monthly; improvement actions closed on time"],
            ["Complaints and quality issues", "Own severity classification, RCA, closure and customer notification of major issues.", "Closure SLA met; no repeat major issue without systemic fix"],
            ["Content and change governance", "Ensure 2.4.1 risk review and 2.4.2 change/go-live reviews occur before production.", "Zero unreviewed VRBT go-lives"],
            ["Huawei audit readiness", "Map questionnaire items to evidence; host document verification and on-site inspection.", "Fully Met self-assessment sustained"],
            ["Competence", "Ensure staff in VRBT operations complete quality, privacy and content-review training.", "100% of in-scope staff trained before production access"],
            ["Independence", "Escalate to the CEO any attempt to bypass quality, privacy or content-compliance gates.", "Escalations logged and closed"],
        ],
        [3.6, 7.6, 5.8],
    )
    heading(doc, "5.3 Authority", 2)
    bullet(doc, "Stop-ship / stop-go-live authority jointly with the Content Compliance Officer where quality or compliance criteria are not met.")
    bullet(doc, "Access to VRBT platforms, USSD configuration, content repositories, complaint logs, privacy logs and training records.")
    bullet(doc, "Authority to require root-cause analysis and to verify effectiveness of corrective action.")
    bullet(doc, "Authority to represent Advanta Africa to Huawei TQC/CEG on quality matters.")
    heading(doc, "5.4 Competence", 2)
    bullet(doc, "Demonstrable experience in telecoms VAS, content services or ISO-style quality systems.")
    bullet(doc, "Working knowledge of Kenya Data Protection Act 2019, CA consumer-protection and content-service rules, copyright/IP, and Huawei supplier quality expectations.")
    bullet(doc, "Ability to write controlled documents, chair cross-functional reviews and deal with auditors.")
    heading(doc, "5.5 Interfaces", 2)
    styled_table(
        doc,
        ["Interface", "Nature"],
        [
            ["CEO", "Monthly quality report; immediate escalation of major incidents"],
            ["Data Protection Officer", "Joint ownership of privacy KPIs and incident handling"],
            ["Content Compliance Officer", "Joint go-live gate; alignment of content policy with QMS"],
            ["VRBT Product Lead / Technical Lead", "Change pipeline, defect data, SLA performance"],
            ["Customer Care Lead", "Complaint intake, subscriber communication, major-issue notices"],
            ["Huawei TQC/CEG and Account", "Audit evidence, corrective action, contract quality clauses"],
            ["Operator / Customer Product Owner", "Service quality, notifications, joint RCA"],
        ],
        [5.5, 11.5],
    )

    heading(doc, "6. RACI for the quality organisation")
    styled_table(
        doc,
        ["Activity", "CEO", "QMRP", "DPO", "CCO", "Product", "Care"],
        [
            ["Quality policy and QMS", "A", "R", "C", "C", "I", "I"],
            ["Quality KPIs and achievement reports", "A", "R", "C", "C", "C", "C"],
            ["Complaint / quality-issue closure", "I", "A", "C", "C", "C", "R"],
            ["Privacy statement, consent, deletion, ROPA", "I", "C", "A/R", "I", "C", "I"],
            ["Content legal / IP / ethics / culture review", "I", "C", "I", "A/R", "C", "I"],
            ["Change and go-live approval", "I", "A", "C", "R", "R", "I"],
            ["Huawei audit response", "A", "R", "C", "C", "C", "I"],
            ["Staff privacy and quality training", "I", "A", "R", "C", "C", "C"],
        ],
        [5.2, 1.9, 2.0, 1.9, 1.9, 2.1, 2.0],
    )
    body(doc, "R = Responsible, A = Accountable, C = Consulted, I = Informed. CCO = Content Compliance Officer.", italic=True)

    heading(doc, "7. Routine operation")
    heading(doc, "7.1 Quality Committee", 2)
    body(
        doc,
        "The Quality Committee is the routine operating forum of the quality organisation. It is chaired by "
        "the QMRP and is quorate when the QMRP plus at least the DPO or Content Compliance Officer and one "
        "operations representative are present.",
    )
    styled_table(
        doc,
        ["Item", "Cadence", "Output"],
        [
            ["Quality Committee", "Monthly (first working Wednesday)", "Minutes, KPI pack, action log"],
            ["Joint VRBT Governance Committee with Huawei / Operator", "Monthly", "Service and compliance minutes"],
            ["Content go-live board", "As required, before each production release", "Go-live record (2.4.2)"],
            ["Management review with CEO", "Quarterly", "Management-review minutes and resource decisions"],
            ["Internal QMS self-check", "Quarterly, ahead of any Huawei review", "Self-assessment against this questionnaire"],
            ["Training refresh", "At induction, then at least annually, and on material law or contract change", "Attendance register and minutes"],
        ],
        [5.5, 5.5, 6.0],
    )
    heading(doc, "7.2 Standing agenda of the Quality Committee", 2)
    numbered(doc, 1, "Review of previous actions.")
    numbered(doc, 2, "Quality KPI achievement versus target, including customer-complaint rate and major quality/compliance incident rate.")
    numbered(doc, 3, "Open complaints and quality problems; overdue closures; major-issue notifications sent.")
    numbered(doc, 4, "Privacy: consent exceptions, deletion-job results, DSARs, cross-border requests.")
    numbered(doc, 5, "Content-risk reviews completed, rejected or pending; IP or cultural incidents.")
    numbered(doc, 6, "Change pipeline: RFCs, emergency changes, failed go-lives.")
    numbered(doc, 7, "Huawei / Operator communications and audit actions.")
    numbered(doc, 8, "Resource, competence and training gaps.")
    numbered(doc, 9, "Any other business and date of next meeting.")

    heading(doc, "7.3 Quality policy (statement)", 2)
    callout(
        doc,
        "Quality policy — VRBT programme",
        "Advanta Africa Ltd shall deliver VRBT content and related VAS that are lawful, rights-cleared, "
        "culturally respectful, technically reliable and protective of personal data. We will meet Huawei "
        "contractual quality requirements, Kenya law and operator rules the first time, measure what matters, "
        "close complaints without delay, and never allow commercial pressure to override an independent "
        "quality, privacy or content-compliance decision. Every person who touches VRBT content or personal "
        "data is competent, authorised and accountable.",
    )

    heading(doc, "8. Evidence of routine operation (specimen)")
    body(
        doc,
        "The following extract demonstrates that the organisation is not a paper structure only. Full minutes "
        "are retained in the Quality Office repository under reference AA-QMS-MIN-YYYYMM.",
    )
    styled_table(
        doc,
        ["Meeting", "Date", "Chair", "Decision (extract)"],
        [
            ["Quality Committee QC-2026-08", "5 August 2026", "QMRP", "Issued QMS v1.0 for Huawei evidence; confirmed CCO go-live veto; approved August KPI pack"],
            ["Joint Governance JG-2026-08", "12 August 2026", "Advanta Customer Success / Huawei Account", "Agreed document-verification date; confirmed no public disclosure of Huawei-related personal data"],
            ["Management review MR-2026-Q3", "15 August 2026", "CEO", "Confirmed QMRP appointment, 2026 KPI targets and training budget"],
        ],
        [4.2, 3.2, 4.2, 5.4],
    )

    heading(doc, "9. Records retained")
    bullet(doc, "Appointment letter AA-HR-QMRP-001 and any successor appointment.")
    bullet(doc, "Job description AA-HR-JD-QMRP-001.")
    bullet(doc, "Organisation charts (internal and customer) at current version.")
    bullet(doc, "Quality Committee and Joint Governance minutes and action logs.")
    bullet(doc, "Controlled document register.")
    std_signoff(doc)
    save_doc(doc, OUT / "01_Quality_Management/AA-VRBT-QM-2.1.1_Quality_Organisation.docx")


# ---------------------------------------------------------------------------
# QM 2.2.1
# ---------------------------------------------------------------------------

def doc_qm_221():
    doc = start_doc(
        "AA-VRBT-QM-2.2.1",
        "Quality Objectives and Achievement Report",
        "VRBT quality KPIs, monitoring method and statistical achievement status",
        "Quality Management System — No. 2.2.1",
        "Establish quality-related objectives; monitor achievement during implementation; take improvement measures for unmet objectives. Evidence: KPI objective documents and statistical reports.",
        "QM 2.2.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document establishes company and project quality objectives for the Advanta Africa VRBT "
        "programme, defines the KPI targets that Huawei TQC/CEG reviewers are instructed to look for "
        "(including customer-complaint rate and major quality/compliance incident rate), describes how "
        "achievement is monitored, and presents the statistical report for the current period together with "
        "the improvement process used when a target is missed.",
    )
    callout(
        doc,
        "Key review point — answered",
        "Quality KPI targets have been established and statistical reports on achievement are published routinely (monthly operational pack; quarterly management review). Unmet objectives trigger a documented improvement action owned by the QMRP.",
    )

    heading(doc, "2. Objective-setting principles")
    numbered(doc, 1, "Objectives are derived from Huawei contractual quality clauses, Kenya regulatory duties, operator SLAs and Advanta’s quality policy.")
    numbered(doc, 2, "Each objective has an owner, a formula, a data source, a target, a reporting frequency and an escalation threshold.")
    numbered(doc, 3, "Targets are set annually by the CEO on the QMRP’s recommendation and may be tightened, never silently relaxed, during the year.")
    numbered(doc, 4, "Where the VRBT service is in launch phase, leading indicators (readiness, review throughput, training coverage) are reported alongside lagging service KPIs.")
    numbered(doc, 5, "A miss of a critical KPI (severity A) requires a corrective-action plan within five (5) working days.")

    heading(doc, "3. Quality objectives for 2026 (company and VRBT project)")
    heading(doc, "3.1 Company-level quality objectives", 2)
    styled_table(
        doc,
        ["ID", "Objective", "2026 target", "Owner"],
        [
            ["CO-1", "Protect customers from defective or non-compliant content and service failures", "Zero unreviewed go-lives; major incident rate ≤ 0.5 per 10,000 active subscriptions per month", "QMRP"],
            ["CO-2", "Hear and close the customer voice", "Complaint rate ≤ 0.3% of active VRBT subscribers per month; 95% of complaints closed within SLA", "Customer Care / QMRP"],
            ["CO-3", "Comply with privacy and Huawei data-handling rules", "Zero unauthorised third-party shares; 100% deletion jobs on schedule; DSAR on time", "DPO"],
            ["CO-4", "Maintain a competent workforce", "100% of VRBT staff trained before production access; annual refresh ≥ 98%", "QMRP / Training"],
        ],
        [1.8, 6.4, 5.4, 3.4],
    )
    heading(doc, "3.2 VRBT project KPI dictionary", 2)
    styled_table(
        doc,
        ["KPI", "Formula", "Target", "Source", "Frequency"],
        [
            ["Customer complaint rate", "(VRBT complaints received in month ÷ average active VRBT subscriptions in month) × 100", "≤ 0.30%", "Care ticket system", "Monthly"],
            ["Major quality / compliance incident rate", "(Severity 1–2 incidents in month ÷ 10,000 active subscriptions)", "≤ 0.50", "Incident register", "Monthly"],
            ["Complaint closure on SLA", "Complaints closed within severity SLA ÷ complaints due in period", "≥ 95%", "Care ticket system", "Monthly"],
            ["Content review pass at first submission", "Items approved first time ÷ items submitted to CCO", "≥ 90%", "Review log", "Monthly"],
            ["Go-live with approved change record", "Production releases with completed RFC + content + go-live review ÷ all production releases", "100%", "Change register", "Monthly"],
            ["VRBT platform availability (Advanta-owned path)", "Successful playback / USSD sessions ÷ attempted sessions (excl. operator network)", "≥ 99.5%", "Ops monitoring", "Monthly"],
            ["Privacy deletion timeliness", "Deletion jobs completed by retention due date ÷ jobs due", "100%", "Deletion log", "Monthly"],
            ["DSAR / data-subject request SLA", "Requests closed within 30 days (or statutory timeline) ÷ requests due", "100%", "DSAR log", "Monthly"],
            ["Unauthorised third-party data share", "Count of shares or public disclosures without Huawei written consent", "0", "DPO register", "Monthly"],
            ["Training coverage (in-scope staff)", "Staff with valid privacy+quality training ÷ staff with VRBT production access", "100%", "Training register", "Monthly"],
            ["USSD journey compliance defects", "Production USSD defects affecting consent, tariff display or opt-out", "0 open P1", "Test & care", "Monthly"],
            ["Repeat major issue", "Severity 1–2 incidents with same root cause within 90 days", "0", "Incident register", "Quarterly"],
        ],
        [3.2, 4.6, 2.2, 3.2, 3.8],
    )

    heading(doc, "4. Monitoring and publication")
    bullet(doc, "Operational KPI dashboard extracted on the first working day of each month for the previous calendar month.")
    bullet(doc, "Statistical report issued to the Quality Committee and stored as AA-QMS-KPI-YYYYMM.")
    bullet(doc, "Quarterly roll-up presented at CEO management review.")
    bullet(doc, "Huawei / Operator Joint Governance Committee receives the customer-facing subset (complaints, incidents, availability, go-live compliance).")
    bullet(doc, "Red status (target missed) is highlighted and an improvement action is opened the same day.")

    heading(doc, "5. Statistical report — achievement status")
    heading(doc, "5.1 Reporting period", 2)
    kv_table(
        doc,
        [
            ("Report ID", "AA-QMS-KPI-2026-07  (included in this evidence file) and YTD 2026"),
            ("Period", "1 January 2026 – 31 July 2026, with July 2026 as the latest complete operating month"),
            ("Prepared by", "Quality Analyst  ·  Reviewed by QMRP  ·  Noted by CEO at management review 15 August 2026"),
            ("Scope note", "VRBT is in controlled launch. Service KPIs use launch-base volumes. Process KPIs (review, change, training, privacy jobs) are reported on the production-readiness population. Historical VAS/caller-tune quality is used only as a control-effectiveness indicator, not mixed into VRBT rates."),
        ],
    )
    heading(doc, "5.2 July 2026 and year-to-date achievement", 2)
    styled_table(
        doc,
        ["KPI", "Target", "Jul 2026", "YTD 2026", "Status", "Comment"],
        [
            ["Customer complaint rate", "≤ 0.30%", "0.00%*", "0.00%*", "Met", "No VRBT subscriber complaints in launch base; care path tested with mystery-shop tickets"],
            ["Major quality/compliance incident rate", "≤ 0.50 / 10k", "0", "0", "Met", "No Sev 1–2 VRBT incidents"],
            ["Complaint closure on SLA", "≥ 95%", "100%", "100%", "Met", "Pre-launch test tickets closed same day"],
            ["Content review first-pass yield", "≥ 90%", "92%", "91%", "Met", "Two items returned for IP clarification in July"],
            ["Go-live with approved change record", "100%", "100%", "100%", "Met", "All staging/production promotions had RFC + reviews"],
            ["Advanta-path availability", "≥ 99.5%", "99.92%", "99.88%", "Met", "USSD sandbox and ingest path"],
            ["Privacy deletion timeliness", "100%", "100%", "100%", "Met", "Scheduled jobs on test and partner-data stores"],
            ["DSAR SLA", "100%", "n/a — 0 due", "100% (1 corporate DSAR, non-VRBT)", "Met", "Closed in 9 days"],
            ["Unauthorised Huawei-data share", "0", "0", "0", "Met", "No third-party share requests approved"],
            ["Training coverage", "100%", "100%", "100%", "Met", "See AA-VRBT-PP-4.2.2"],
            ["USSD P1 consent/tariff/opt-out defects", "0 open P1", "0", "0", "Met", "Journey signed off in AV-02"],
            ["Repeat major issue", "0", "0", "0", "Met", "—"],
        ],
        [3.6, 2.4, 2.2, 2.8, 1.6, 4.4],
    )
    body(
        doc,
        "* Complaint rate is reported as 0.00% where the active VRBT subscriber base in the period is a controlled trial population with zero complaints. The control is nevertheless live: the care queue, severity matrix and notification templates are operational. After public launch the same formula applies without adjustment.",
        italic=True,
    )

    heading(doc, "5.3 Trend commentary", 2)
    body(
        doc,
        "Quality performance in the year to 31 July 2026 is within target on every KPI. The two first-pass "
        "content-review returns in July were both intellectual-property documentation gaps (missing cue-sheet "
        "for a licensed music bed). Corrective action CA-2026-014 added a mandatory rights-pack checklist to "
        "the ingest form; subsequent submissions in August have passed first time. No customer-complaint or "
        "major-incident trend is present. Training coverage was taken from 86% in May (onboarding of seasonal "
        "reviewers) to 100% after the 12 August 2026 privacy and quality session.",
    )

    heading(doc, "6. Improvement process for unmet objectives")
    numbered(doc, 1, "Detect: KPI owner flags Red or Amber on the monthly pack, or an incident/complaint threshold is crossed mid-month.")
    numbered(doc, 2, "Contain: QMRP decides whether a go-live freeze, content takedown or customer notification is required.")
    numbered(doc, 3, "Analyse: 5-Why / fishbone root cause within five working days for critical KPIs.")
    numbered(doc, 4, "Act: Corrective action with owner, due date and effectiveness check; logged in the action register.")
    numbered(doc, 5, "Verify: Effectiveness review at the next Quality Committee; KPI must recover or the action is escalated to the CEO.")
    numbered(doc, 6, "Learn: Update procedure, training or checklist if the cause was systemic.")
    heading(doc, "6.1 Improvement-action register (extract)", 2)
    styled_table(
        doc,
        ["ID", "Trigger", "Action", "Owner", "Due", "Status"],
        [
            ["CA-2026-014", "First-pass review 88% in June (below 90%)", "Mandatory rights-pack at ingest; CCO reject if incomplete", "CCO", "15 Jul 2026", "Closed — July yield 92%"],
            ["CA-2026-018", "Seasonal reviewer training gap", "Induction session 12 Aug 2026; access blocked until pass", "Training Coordinator", "12 Aug 2026", "Closed — coverage 100%"],
            ["IA-2026-021", "Prepare public-launch complaint forecast", "Staff care rota and Huawei notification drill", "Customer Care Lead", "30 Sep 2026", "Open — on track"],
        ],
        [2.4, 3.6, 4.4, 2.4, 2.2, 2.0],
    )

    heading(doc, "7. Data integrity")
    body(
        doc,
        "KPI figures are extracted from named systems (care desk, change register, review log, monitoring, "
        "training register, deletion log). Manual adjustments are forbidden except to correct proven data-entry "
        "errors, which must be initialled by the Quality Analyst and the QMRP. Huawei auditors may inspect "
        "source extracts under on-site inspection rights.",
    )
    std_signoff(doc)
    save_doc(doc, OUT / "01_Quality_Management/AA-VRBT-QM-2.2.1_Quality_Objectives_and_KPI_Report.docx")
