"""Privacy Protection evidence: 4.1.1 through 4.2.2."""

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


def doc_pp_411():
    doc = start_doc(
        "AA-VRBT-PP-4.1.1",
        "Privacy Statement and Consent Management",
        "Pre-collection notice, valid consent, and re-consent when the privacy statement is updated",
        "Privacy Protection — No. 4.1.1  ·  Business Management",
        "Before collecting personal data, a privacy statement is provided and valid consent is obtained, in compliance with the business contract. When the privacy statement is updated, the user is notified through effective means and consent is re-obtained.",
        "PP 4.1.1",
    )
    revision_history(doc)
    heading(doc, "1. Purpose and questionnaire mapping")
    body(
        doc,
        "This document is the management document and privacy statement required as evidence for item 4.1.1. "
        "It describes how Advanta Africa Ltd provides a privacy statement and obtains valid consent before "
        "collecting personal data for the VRBT service, how that practice meets the Huawei business-contract "
        "requirements, and how users are notified and asked to re-consent when the statement is updated.",
    )
    styled_table(
        doc,
        ["Review question", "Control"],
        [
            ["Is a privacy statement provided before collection?", "Yes — USSD/app/web notice plus this full statement, before MSISDN, profile or payment data is stored by Advanta"],
            ["Is valid consent obtained from the data subject?", "Yes — affirmative opt-in (USSD accept / tick box / recorded Operator consent token), not bundled with unrelated terms, withdrawable"],
            ["Does this comply with the business contract?", "Yes — Huawei personal-data clauses, Operator VAS rules, and Kenya Data Protection Act 2019 ss. 25–32"],
            ["When the statement is updated, is the user notified by effective means?", "Yes — in-journey notice, SMS to active subscribers, website posting, Operator care scripts"],
            ["Is consent re-obtained?", "Yes — material updates require a fresh accept; service is not charged until accept is logged"],
        ],
        [7.0, 10.0],
    )

    heading(doc, "2. Roles and lawful bases")
    bullet(doc, "Operator / MNO: typically the data controller for subscriber MSISDN, service subscription and billing.")
    bullet(doc, "Advanta Africa: data processor for Operator-originated subscriber data; data controller for employee data, content-partner data, and Advanta website/account data.")
    bullet(doc, "Huawei: platform provider. Advanta does not treat Huawei as a public disclosure channel and does not share Huawei-related personal data with any other party without Huawei’s written consent (AA-VRBT-PP-4.1.3).")
    body(
        doc,
        "Where Advanta is a processor, it processes only on documented instructions (the Operator agreement and Huawei cooperation terms). Where Advanta is a controller, the primary lawful bases under the Data Protection Act, 2019 are: consent (s. 32) for marketing and optional profile features; contract (s. 30) for service delivery the person has requested; legal obligation for retention required by communications or tax law; and legitimate interests only where a documented assessment shows they are not overridden by the data subject’s rights. Sensitive personal data is not required for VRBT and is not collected.",
    )

    heading(doc, "3. Personal data collected for VRBT (minimum necessary)")
    styled_table(
        doc,
        ["Data", "Source", "Purpose", "Collected only after notice + consent / instruction"],
        [
            ["MSISDN (calling / called party as applicable)", "Operator / USSD session", "Provision of VRBT, charging correlation, unsubscribe", "Yes"],
            ["Subscription state, content ID, timestamp", "Service platform", "Fulfil the requested tune, support, dispute", "Yes"],
            ["USSD / channel consent log (yes/no, time, version of statement)", "Consent manager", "Demonstrate valid consent and version", "Yes — this is the consent record itself"],
            ["Device type (coarse) where required for video compatibility", "Operator / app", "Deliver a playable asset", "Yes"],
            ["Content-partner contact and KYC", "Partner onboarding", "Licensing and payments", "Yes — partner contract + notice"],
            ["Employee user IDs and access logs", "HR / IAM", "Security and accountability", "Employment contract / legal obligation"],
            ["Payment card PAN / bank OTP", "—", "Not collected by Advanta for Operator-billed VRBT", "Not collected"],
            ["Precise location, contacts, photos, special-category data", "—", "Not required", "Not collected"],
        ],
        [4.2, 3.0, 4.6, 5.2],
    )

    heading(doc, "4. VRBT Privacy Statement (public-facing text)")
    callout(
        doc,
        "Advanta Africa Ltd — VRBT Privacy Statement  ·  Version 1.0  ·  Effective 1 August 2026",
        "This is the statement presented to the data subject before Advanta stores VRBT-related personal data. "
        "A short-form version appears on USSD (see AA-VRBT-AV-02). The long-form version is at "
        "www.advanta.africa/privacy-policy and is issued below for audit.",
    )
    heading(doc, "4.1 Who we are", 2)
    body(
        doc,
        "Advanta Africa Ltd, Western Heights, 6th Floor, Karuna Road, Westlands, Nairobi, Kenya, telephone "
        "+254 111 139 000, email privacy@advanta.africa, is a value-added services and messaging company. "
        "For Video Ring Back Tune (VRBT), we provide content operations and technical services in cooperation "
        "with Huawei Technologies and with your mobile-network operator. Your operator remains responsible "
        "for your mobile subscription. Our Data Protection Officer may be contacted at privacy@advanta.africa.",
    )
    heading(doc, "4.2 What we collect and why", 2)
    body(
        doc,
        "If you subscribe to a VRBT, we process the mobile number used to subscribe, the tune you choose, "
        "time and channel of subscription and unsubscription, and technical data needed to play the video to "
        "callers on compatible devices. We use this information to provide the service you request, to charge "
        "only for services you accepted, to handle complaints, to meet Kenya law, and to meet our contracts "
        "with your operator and with Huawei. We do not sell, rent or trade your personal data.",
    )
    heading(doc, "4.3 Consent", 2)
    body(
        doc,
        "We will show you a privacy notice and the price before you are subscribed. You must send a clear YES "
        "/ ACCEPT (or equivalent Operator double opt-in). Silence, pre-ticked boxes or a marketing SMS alone "
        "are not consent. You may withdraw consent at any time by the unsubscribe command in the USSD menu, "
        "by sending the published STOP code, or by asking your operator. Withdrawal does not affect processing "
        "that was lawful before withdrawal. We keep a log of the notice version you accepted.",
    )
    heading(doc, "4.4 Sharing", 2)
    body(
        doc,
        "We share data with your operator to bill and support the service, and with Huawei only as required to "
        "operate the VRBT platform under contract. We do not share Huawei-related or VRBT personal data with "
        "any other third party, and we do not publish it, unless Huawei has given prior written consent or "
        "Kenya law requires disclosure (for example a court order). If the law requires disclosure, we share "
        "the minimum and we record the request. Details: AA-VRBT-PP-4.1.3.",
    )
    heading(doc, "4.5 Retention and deletion", 2)
    body(
        doc,
        "We keep subscription and consent logs only as long as needed to provide the service, resolve disputes "
        "and meet legal retention (see the schedule in AA-VRBT-PP-4.1.2). When the period expires, or if you "
        "successfully request deletion and no overriding legal duty applies, we delete or irreversibly anonymise "
        "the data. Deletion is logged.",
    )
    heading(doc, "4.6 Cross-border transfer", 2)
    body(
        doc,
        "Some platform support may involve transfer of personal data outside Kenya (for example Huawei platform "
        "administration). We do so only with a signed cross-border transfer agreement, appropriate safeguards "
        "under the Data Protection Act 2019 ss. 48–49 and the 2021 General Regulations, and — where required — "
        "your informed consent. A serving copy of data processed in Kenya is retained in Kenya. Details: "
        "AA-VRBT-PP-4.1.5.",
    )
    heading(doc, "4.7 Your rights", 2)
    body(
        doc,
        "You may request access, correction, deletion, restriction, objection, portability (where applicable), "
        "and withdrawal of consent, and you may complain to the Office of the Data Protection Commissioner "
        "(ODPC), Kenya. We will respond within the statutory period. Contact privacy@advanta.africa or "
        "+254 111 139 000. If you are an Operator subscriber, you may also use your Operator’s care channels; "
        "we will cooperate with the Operator to fulfil the request.",
    )
    heading(doc, "4.8 Security", 2)
    body(
        doc,
        "We apply access control, encryption in transit, environment segregation, logging, staff vetting and "
        "training, and supplier due diligence. No method is perfect; we will notify you and the ODPC of a "
        "notifiable breach as required by law and by contract.",
    )
    heading(doc, "4.9 Children", 2)
    body(
        doc,
        "VRBT subscriptions are intended for the account holder. We do not knowingly profile children. Content "
        "is reviewed to prohibit sexualisation of minors and other child-harmful material (AA-VRBT-QM-2.4.1).",
    )
    heading(doc, "4.10 Changes to this statement", 2)
    body(
        doc,
        "If we make a material change (new purpose, new category of recipient, new cross-border destination, "
        "or a change that is less favourable to you), we will notify you through the service journey, by SMS "
        "to the MSISDN on the subscription, and by posting the new version with a new version number. We will "
        "ask you to accept again. If you do not accept, we will not apply the new purpose to you and we will "
        "stop the optional service where consent is the basis. Minor clarifications that do not change processing "
        "are posted with the version history and do not require re-consent.",
    )

    heading(doc, "5. How valid consent is obtained in practice")
    heading(doc, "5.1 USSD (primary VRBT channel)", 2)
    numbered(doc, 1, "Customer dials the published code (operator-allocated; currently designed as *860# or the Operator’s designated VRBT code).")
    numbered(doc, 2, "Menu shows service name, price (including frequency if subscription), and a one-screen privacy notice with a link/USSD path to the full statement.")
    numbered(doc, 3, "Customer selects a tune. A confirmation screen repeats price and “Personal data (your number, your choice of tune and time) will be processed as per the Privacy Statement v1.0. Reply 1 to ACCEPT or 2 to CANCEL.”")
    numbered(doc, 4, "Only an explicit ACCEPT creates a subscription. The consent manager stores MSISDN (or Operator token), timestamp, channel, statement version, tariff presented, and content ID.")
    numbered(doc, 5, "A confirmation message is sent. Unsubscribe is available on every journey (0 or STOP).")
    heading(doc, "5.2 App / web", 2)
    body(doc, "Unticked consent box, statement version displayed, ACCEPT button enabled only after scroll or expandable full text, same logging fields as USSD.")
    heading(doc, "5.3 Operator-collected consent", 2)
    body(doc, "Where the Operator is controller and sends Advanta a consent token, Advanta does not collect a second marketing consent but still presents Advanta’s processor notice at first Advanta-touch point where feasible, and will not process beyond the instruction.")
    heading(doc, "5.4 What is not valid consent", 2)
    bullet(doc, "Pre-ticked boxes, inactivity, payment of an unrelated service, or burying accept in general terms.")
    bullet(doc, "Consent obtained by misleading price or by omitting that a subscription recurs.")
    bullet(doc, "Consent from a child where the account holder has not authorised the service.")
    bullet(doc, "Continuing to process for a new purpose after a material statement change without a new ACCEPT.")

    heading(doc, "6. Update and re-consent procedure")
    numbered(doc, 1, "DPO drafts the new statement, records whether the change is material, and obtains QMRP/Legal/Huawei-contract check.")
    numbered(doc, 2, "Change raised under AA-VRBT-QM-2.4.2 (privacy class).")
    numbered(doc, 3, "Effective date set at least seven (7) days after first notification unless a regulator requires faster action.")
    numbered(doc, 4, "Effective means of notice: (a) SMS to all active VRBT MSISDNs; (b) blocking interstitial on USSD/app until ACCEPT or CANCEL; (c) website posting; (d) Operator care brief.")
    numbered(doc, 5, "Consent manager increments statement version. Old version IDs remain on historic logs.")
    numbered(doc, 6, "If the subscriber CANCELS or ignores a material-change interstitial beyond the grace period, optional processing stops; the Operator is instructed to cease charging the Advanta VRBT product.")
    numbered(doc, 7, "Evidence pack: copies of SMS, screenshots of interstitial, volume of ACCEPT/CANCEL, and Huawei notification if their processing description changed.")

    heading(doc, "7. Contract alignment (Huawei business requirements)")
    body(
        doc,
        "Advanta’s Huawei cooperation terms require that personal data be processed lawfully, fairly and "
        "transparently; that Advanta be able to demonstrate consent or other lawful basis; and that Huawei "
        "be informed of processing descriptions that affect the platform. This statement, the consent logs "
        "and the ROPA (AA-VRBT-PP-4.1.4) are the demonstration. Advanta will not enable a VRBT feature that "
        "collects additional personal data until this statement is updated and, if material, re-consented.",
    )

    heading(doc, "8. Specimen consent log (fields)")
    styled_table(
        doc,
        ["consent_id", "msisdn_token", "channel", "statement_ver", "tariff_shown", "action", "timestamp_eat"],
        [
            ["CN-2026-000441", "hash-a91c…", "USSD *860#", "1.0", "KES X / day", "ACCEPT", "2026-08-12 09:14:22"],
            ["CN-2026-000442", "hash-b22e…", "USSD *860#", "1.0", "KES X / day", "CANCEL", "2026-08-12 09:16:01"],
        ],
        [2.6, 2.4, 2.4, 2.2, 2.4, 1.8, 3.2],
    )
    body(doc, "Live MSISDNs are not reproduced in this audit file. On-site inspection may view the consent manager with minimised display.", italic=True)
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.1.1_Privacy_Statement_and_Consent.docx")


def doc_pp_412():
    doc = start_doc(
        "AA-VRBT-PP-4.1.2",
        "Personal Data Retention and Deletion",
        "Expiry mechanism, contractual alignment, and deletion records",
        "Privacy Protection — No. 4.1.2  ·  Business Management",
        "A mechanism for deletion of personal data upon expiration has been established. Personal data is deleted upon expiration in accordance with the contract or business requirements.",
        "PP 4.1.2",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "This management document establishes the retention schedule for VRBT personal data, the automated and "
        "manual deletion mechanism, verification, and the deletion-record log that Huawei reviewers and employee "
        "interviews can inspect. It implements Kenya Data Protection Act s. 25(e) (not keeping data longer than "
        "necessary), Huawei contractual deletion requirements, and Operator instructions.",
    )

    heading(doc, "2. Principles")
    bullet(doc, "Default to the shortest period that still meets service, dispute, tax, communications-law and contract needs.")
    bullet(doc, "Expiry is computed per record, not per database.")
    bullet(doc, "Deletion means irreversible destruction of personal identifiers or irreversible anonymisation that cannot be re-identified by Advanta.")
    bullet(doc, "Backups roll off according to the backup TTL; expired data is not restored into production except for a documented legal hold.")
    bullet(doc, "Huawei-related personal data is not retained in unstructured stores (mail, chat, laptops) beyond the schedule; staff procedures in AA-VRBT-PP-4.2.1 apply.")
    bullet(doc, "Legal hold (litigation, regulator, Huawei audit exception in writing) suspends deletion of named records until released by the DPO.")

    heading(doc, "3. Retention schedule (VRBT)")
    styled_table(
        doc,
        ["Record class", "Retention", "Trigger for expiry", "Deletion method"],
        [
            ["USSD session logs (raw signalling)", "90 days", "Session end + 90 days", "Automated job; overwrite"],
            ["Consent ACCEPT/CANCEL logs", "Duration of subscription + 24 months (dispute / CA billing evidence)", "Unsubscribe or last activity + 24 months", "Automated job; cryptographic erase of identifiers"],
            ["Active subscription profile (MSISDN token, content ID, status)", "Life of subscription", "Successful unsubscribe or Operator cease instruction", "Delete from production within 24 hours; billing CDR per row below"],
            ["Charging / truncated CDR needed for Operator reconciliation", "13 months", "Event date + 13 months", "Automated job"],
            ["Complaint tickets containing MSISDN", "3 years", "Ticket close + 3 years", "Quarterly supervised delete"],
            ["Major-incident files", "6 years", "Incident close + 6 years", "Supervised; DPO + QMRP"],
            ["Content-partner contracts and KYC", "Term + 6 years", "Contract end + 6 years", "Supervised"],
            ["Employee access logs to VRBT PII", "18 months", "Log date + 18 months", "Automated"],
            ["Huawei audit evidence containing personal data", "6 years after cooperation ends, or as contract requires", "Contractual end date", "Supervised"],
            ["Marketing suppression / STOP list", "Until the person is known deceased or 7 years after last contact, whichever is needed to honour STOP", "DPO review annually", "Do not delete if deletion would cause unwanted marketing"],
            ["Backups of the above", "Not longer than production TTL + 35 days", "Backup expiry", "Media rotation / cloud object TTL"],
        ],
        [4.4, 3.6, 4.4, 4.6],
    )
    callout(
        doc,
        "Contract override",
        "If the Huawei or Operator contract requires a shorter period, the shorter period wins. If Kenya law "
        "requires a longer period (for example a tax record), the legal period wins and the DPO records the conflict "
        "in the ROPA. Advanta does not keep VRBT personal data “just in case” beyond this schedule.",
    )

    heading(doc, "4. Deletion mechanism")
    heading(doc, "4.1 Automated expiry", 2)
    numbered(doc, 1, "Each personal-data store has a retention_class and expires_at column (or equivalent object TTL) populated at write time from this schedule.")
    numbered(doc, 2, "A daily job (01:30 EAT) selects records where expires_at < now and legal_hold = false.")
    numbered(doc, 3, "The job deletes or anonymises in accordance with the method column, then writes a success/fail line to the deletion log (Section 6).")
    numbered(doc, 4, "Failures page the DPO and Privacy Operations. Repeat failure for more than 24 hours is a Sev 2 quality/privacy incident.")
    numbered(doc, 5, "Change RFC-2026-033 enabled the 13-month CDR job (see AA-VRBT-QM-2.4.2).")
    heading(doc, "4.2 Unsubscription and right to erasure", 2)
    body(
        doc,
        "When a subscriber unsubscribes, the active profile is deleted from production within twenty-four (24) hours. "
        "Consent and CDR records continue only until their own expiry, unless a valid erasure request requires earlier "
        "deletion and no overriding legal duty applies. Erasure requests are handled as DSARs (30 days or shorter if "
        "the Operator instructs).",
    )
    heading(doc, "4.3 Media and unstructured data", 2)
    bullet(doc, "Exports to CSV/Excel require DPO approval and an expires_at; the file is tracked.")
    bullet(doc, "Email containing subscriber MSISDNs must use tickets, not personal mailboxes, and is covered by the ticket retention row.")
    bullet(doc, "Laptops: full-disk encryption; leavers’ accounts collected within 24 hours (AA-VRBT-PP-4.2.1).")

    heading(doc, "5. Verification and interviews")
    body(
        doc,
        "Huawei may inspect the deletion-job scheduler, a sample of expires_at values, and the log. Employees in "
        "Privacy Operations can explain the daily job, the legal-hold flag, and what they do on failure. Mystery "
        "deletion tests (insert a dummy record with expires_at yesterday) are run monthly; results are in the log.",
    )

    heading(doc, "6. Deletion records")
    heading(doc, "6.1 Log fields", 2)
    body(doc, "job_id, run_time_eat, store, retention_class, records_selected, records_deleted, records_held, records_failed, operator, checksum.")
    heading(doc, "6.2 Extract (specimen)", 2)
    styled_table(
        doc,
        ["job_id", "run_time", "store", "class", "selected", "deleted", "held", "failed"],
        [
            ["DEL-2026-08-12-A", "2026-08-12 01:30", "ussd_session", "90d", "1,204", "1,204", "0", "0"],
            ["DEL-2026-08-12-B", "2026-08-12 01:35", "cdr_trunc", "13m", "0", "0", "0", "0"],
            ["DEL-2026-08-12-C", "2026-08-12 01:40", "consent_log", "sub+24m", "0", "0", "0", "0"],
            ["DEL-2026-08-01-M", "2026-08-01 11:00", "mystery_dummy", "test", "1", "1", "0", "0"],
        ],
        [3.2, 2.6, 2.6, 2.2, 1.6, 1.6, 1.4, 1.8],
    )
    heading(doc, "6.3 Certificate of destruction (supervised classes)", 2)
    body(
        doc,
        "For partner KYC and major-incident files, the DPO issues a certificate stating the record class, period, "
        "method (shred / crypto-erase / certified cloud delete), witnesses, and date. Certificates are retained "
        "six (6) years. None have yet fallen due for VRBT partner KYC (contracts still in term).",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.1.2_Data_Retention_and_Deletion.docx")


def doc_pp_413():
    doc = start_doc(
        "AA-VRBT-PP-4.1.3",
        "Prohibition on Third-Party Sharing and Public Disclosure",
        "Without Huawei’s consent, personal data shall not be shared with third parties or disclosed publicly",
        "Privacy Protection — No. 4.1.3  ·  Business Management",
        "Without Huawei’s consent, it is prohibited to share personal data with third parties or to disclose personal data publicly. Evidence: management documents, on-site inspections, employee interviews.",
        "PP 4.1.3",
    )
    revision_history(doc)
    heading(doc, "1. Binding rule")
    callout(
        doc,
        "Mandatory control — Huawei consent gate",
        "Advanta Africa Ltd shall not share with any third party, and shall not disclose publicly, any personal data "
        "that is processed in the course of cooperation with Huawei (including VRBT platform data, Huawei staff data, "
        "and subscriber data present on Huawei systems or logs to which Advanta has access), unless Huawei has given "
        "prior written consent or a compulsory legal duty applies under the procedure in Section 5. Breach is a "
        "gross-misconduct offence (AA-VRBT-PP-4.2.1) and a Sev 1 privacy incident.",
    )
    body(
        doc,
        "This rule is additional to Kenya Data Protection Act duties. Even if Kenya law would allow a share, Huawei "
        "written consent is still required before Advanta shares Huawei-cooperation personal data, except where a "
        "court order, warrant or ODPC/CA statutory notice forbids delay and Section 5 is followed.",
    )

    heading(doc, "2. What counts as sharing or public disclosure")
    bullet(doc, "Providing personal data to a vendor, sub-processor, affiliate, journalist, researcher, marketer or other Huawei customer.")
    bullet(doc, "Publishing personal data on a website, app store listing, social media, press release, conference talk or marketing case study.")
    bullet(doc, "Placing personal data in a generative-AI tool, public ticket system or unapproved cloud folder.")
    bullet(doc, "Showing live subscriber data on a wallboard visible to visitors.")
    bullet(doc, "Handing a laptop, USB or export to anyone outside the authorised VRBT access group.")
    body(doc, "Sharing with the Operator pursuant to the Operator processing instructions, and with Huawei pursuant to the cooperation contract, is not a “third-party share” for this rule; it is in-contract processing. New sub-processors still need Huawei consent if they will see Huawei-cooperation personal data.")

    heading(doc, "3. Allowed processing without extra Huawei consent")
    numbered(doc, 1, "Processing inside Advanta by authorised, trained staff on a need-to-know basis.")
    numbered(doc, 2, "Processing by Huawei under the existing cooperation agreement.")
    numbered(doc, 3, "Processing by the Operator as controller/recipient under the Operator agreement.")
    numbered(doc, 4, "Disclosure compelled by Kenya law after Section 5.")

    heading(doc, "4. How Huawei consent is obtained")
    numbered(doc, 1, "Originator raises a written request (Form AA-PRV-SHR-001) stating data categories, recipients, purpose, location, period, and whether public disclosure is proposed.")
    numbered(doc, 2, "DPO reviews necessity, minimisation, contract and Kenya law.")
    numbered(doc, 3, "QMRP confirms quality/audit impact.")
    numbered(doc, 4, "Request is sent to the Huawei Account / nominated privacy contact.")
    numbered(doc, 5, "Only written consent (email from a Huawei authorised address or signed letter) is accepted. Silence is refusal.")
    numbered(doc, 6, "If granted, a time-bound instruction is logged in the ROPA and technical controls are limited to that recipient.")
    numbered(doc, 7, "Public disclosure additionally requires CEO approval and legal review of the text.")

    heading(doc, "5. Compulsory legal disclosure")
    body(
        doc,
        "If Advanta receives a court order, police warrant, CA or ODPC notice requiring disclosure of Huawei-cooperation "
        "personal data: (a) Legal and DPO are notified immediately; (b) Huawei is notified before disclosure unless the "
        "instrument prohibits notice, in which case notice is given as soon as lawful; (c) only the data specified is "
        "produced; (d) the production pack is logged; (e) no public comment is made.",
    )

    heading(doc, "6. Technical and organisational measures (inspectable on site)")
    bullet(doc, "Access groups: VRBT-PII-NEED-TO-KNOW; joiner/mover/leaver within 24 hours.")
    bullet(doc, "DLP / export control on production databases; mass export requires DPO token.")
    bullet(doc, "No public Git, no personal WhatsApp of subscriber lists, no screenshot of PII in chat.")
    bullet(doc, "Visitor badges; production screens not oriented to public areas.")
    bullet(doc, "Press and marketing staff are on a written ban list for VRBT personal data and Huawei staff data.")
    bullet(doc, "Sub-processor register; no new sub-processor until Huawei consent if they will access the data.")

    heading(doc, "7. Register of third-party share requests")
    styled_table(
        doc,
        ["ID", "Date", "Request", "Huawei consent", "Outcome"],
        [
            ["SHR-2026-000", "—", "None received for VRBT / Huawei-cooperation personal data in 2026 YTD", "—", "No shares; no public disclosures"],
        ],
        [2.4, 2.2, 6.4, 2.8, 3.2],
    )
    body(
        doc,
        "Employee interviews: staff are trained that the correct answer to “can we put a subscriber story in a case study?” "
        "is “not without Huawei written consent and the subscriber’s consent”. Training records: AA-VRBT-PP-4.2.2.",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.1.3_Third_Party_Sharing_Prohibition.docx")


def doc_pp_414():
    doc = start_doc(
        "AA-VRBT-PP-4.1.4",
        "Records of Processing Activities",
        "Accountable inventory of all VRBT personal-data processing",
        "Privacy Protection — No. 4.1.4  ·  Business Management",
        "Records of all data processing activities must be provided to ensure the accountability of data processing. Evidence: on-site inspections, employee interviews.",
        "PP 4.1.4",
    )
    revision_history(doc)
    heading(doc, "1. Accountability statement")
    body(
        doc,
        "Advanta Africa Ltd maintains a Record of Processing Activities (ROPA) for VRBT and related Huawei "
        "cooperation. The ROPA is owned by the DPO, reviewed quarterly, and updated whenever a change under "
        "AA-VRBT-QM-2.4.2 affects personal data. It is available for Huawei on-site inspection and employees "
        "who process personal data can explain the activities they perform. This document is the ROPA extract "
        "for audit; the live register is AA-PRV-ROPA-VRBT in the DPO repository.",
    )

    heading(doc, "2. Controller / processor map")
    styled_table(
        doc,
        ["Activity", "Advanta role", "Other parties"],
        [
            ["Operator subscriber VRBT subscription, charging, care", "Processor", "Operator = controller; Huawei = platform processor/sub-processor as per contract"],
            ["Content-partner onboarding and royalties", "Controller", "Partner as controller of their own employee data"],
            ["Employee HR, access, training", "Controller", "HR processors (payroll) under contract"],
            ["Huawei staff contact details for project delivery", "Controller of Advanta’s business-contact file; no onward share without Huawei consent", "Huawei"],
        ],
        [5.5, 5.0, 6.5],
    )

    heading(doc, "3. Processing activities (VRBT)")
    def act(rows):
        styled_table(
            doc,
            ["Field", "Record"],
            rows,
            [4.2, 12.8],
        )

    heading(doc, "3.1 Activity P-VRBT-01 — Subscription fulfilment", 2)
    act([
        ["Name / purpose", "Create, change and cease VRBT subscriptions the subscriber requested"],
        ["Categories of data subjects", "Operator subscribers"],
        ["Categories of personal data", "MSISDN or Operator token; content ID; channel; timestamps; coarse device class"],
        ["Lawful basis / instruction", "Operator instruction + subscriber consent logged in consent manager"],
        ["Recipients", "Operator billing; Huawei platform (in contract); Advanta authorised ops — no other third party"],
        ["International transfer", "See P-VRBT-05 / AA-VRBT-PP-4.1.5 if platform admin is outside Kenya"],
        ["Retention", "Profile: life of subscription; consent: subscription + 24 months"],
        ["Security", "IAM, encryption in transit, environment segregation, DLP on export"],
        ["DPO / owner", "DPO accountability; VRBT Technical Lead operational owner"],
    ])
    heading(doc, "3.2 Activity P-VRBT-02 — Consent capture and versioning", 2)
    act([
        ["Name / purpose", "Demonstrate valid consent and re-consent on statement updates"],
        ["Categories of data subjects", "Subscribers who see the VRBT journey"],
        ["Categories of personal data", "Tokenised MSISDN; statement version; ACCEPT/CANCEL; tariff shown; time"],
        ["Lawful basis / instruction", "Legal obligation (accountability) and consent process itself"],
        ["Recipients", "None outside Advanta, Operator (if they require a copy), Huawei audit on request"],
        ["Retention", "Subscription + 24 months"],
        ["Security", "Append-only log; restricted access"],
    ])
    heading(doc, "3.3 Activity P-VRBT-03 — Charging reconciliation", 2)
    act([
        ["Name / purpose", "Reconcile VRBT charges with the Operator"],
        ["Categories of personal data", "Truncated CDR: token, product code, amount, time — no content payload"],
        ["Lawful basis / instruction", "Operator contract; legal obligation to keep accurate billing evidence"],
        ["Recipients", "Operator finance; internal finance — not public; not other Huawei customers"],
        ["Retention", "13 months unless law requires longer"],
    ])
    heading(doc, "3.4 Activity P-VRBT-04 — Complaints and incidents", 2)
    act([
        ["Name / purpose", "Handle complaints, quality problems and privacy incidents"],
        ["Categories of personal data", "Contact number/email as provided; ticket narrative; minimised logs"],
        ["Lawful basis", "Legitimate interests in service quality; legal obligation for incidents; Operator instruction"],
        ["Recipients", "Huawei / Operator under AA-VRBT-QM-2.3.1 notices (minimised); regulators if required"],
        ["Retention", "3 years tickets; 6 years major incidents"],
    ])
    heading(doc, "3.5 Activity P-VRBT-05 — Platform operations with Huawei", 2)
    act([
        ["Name / purpose", "Operate VRBT on the Huawei platform (ingest, playback, monitoring)"],
        ["Categories of personal data", "As in P-VRBT-01 plus technical identifiers required by the platform"],
        ["Lawful basis / instruction", "Huawei cooperation contract; Operator instruction"],
        ["Recipients", "Huawei only, as platform provider — onward third-party share prohibited without Huawei consent"],
        ["International transfer", "Possible platform support outside Kenya under AA-VRBT-PP-4.1.5"],
        ["Retention", "Aligned to P-VRBT-01 and Huawei instruction, whichever is shorter"],
    ])
    heading(doc, "3.6 Activity C-VRBT-01 — Content-partner management", 2)
    act([
        ["Name / purpose", "License content, pay royalties, conduct IP due diligence"],
        ["Advanta role", "Controller"],
        ["Categories of data subjects", "Partner staff, talent whose likeness is licensed"],
        ["Categories of personal data", "Name, ID (KYC), payment details, contract, optional likeness"],
        ["Lawful basis", "Contract; legal obligation (tax, AML as applicable)"],
        ["Recipients", "Banks, tax authorities; not Huawei subscriber data"],
        ["Retention", "Term + 6 years"],
    ])
    heading(doc, "3.7 Activity C-EMP-01 — Employee access and training", 2)
    act([
        ["Name / purpose", "Authorise and train staff who may see VRBT personal data"],
        ["Categories of personal data", "Name, role, training scores, access logs"],
        ["Lawful basis", "Employment contract; legal obligation; legitimate interests in security"],
        ["Recipients", "None public; Huawei may inspect training records on site without copying extra PII"],
        ["Retention", "Employment + 6 years for training acknowledgements; 18 months for detailed access logs"],
    ])

    heading(doc, "4. Systems inventory (on-site inspection list)")
    styled_table(
        doc,
        ["System", "Personal data", "Location of serving copy", "Owner"],
        [
            ["Consent manager", "Consent logs", "Kenya", "DPO / Tech Lead"],
            ["VRBT catalogue & subscription store", "Tokens, content ID, status", "Kenya (+ Huawei platform as contracted)", "Tech Lead"],
            ["USSD gateway", "Session logs", "Kenya", "Tech Lead"],
            ["Care desk", "Tickets", "Kenya", "Customer Care Lead"],
            ["Deletion-job scheduler", "Job logs (not content of deleted PII)", "Kenya", "Privacy Operations"],
            ["Training register", "Staff competence", "Kenya", "Training Coordinator"],
        ],
        [4.2, 4.2, 4.6, 4.0],
    )

    heading(doc, "5. Keeping the ROPA accurate")
    bullet(doc, "Quarterly DPO attestation to the Quality Committee.")
    bullet(doc, "Mandatory ROPA update field on privacy-class RFCs.")
    bullet(doc, "New processing is prohibited until the ROPA row exists and, if high risk, a DPIA is completed.")
    heading(doc, "6. Interview guidance (for Huawei employee interviews)")
    body(
        doc,
        "A VRBT operator should be able to say: what data they see, why they see it, that they must not export it, "
        "that Huawei consent is required before any third-party share or public post, how long it is kept, and whom "
        "they call (DPO) if something goes wrong. Those answers are trained in AA-VRBT-PP-4.2.2.",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Data Protection Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "02_Privacy_Protection/AA-VRBT-PP-4.1.4_Records_of_Processing_Activities.docx")
