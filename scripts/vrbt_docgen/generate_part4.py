"""Audio and Video evidence documents (Advanta working notes)."""

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


def doc_av_01():
    doc = start_doc(
        "AA-VRBT-AV-01",
        "Audio and Video Content Licensing — Contract Snippet",
        "Mandatory licensing terms for VRBT use of audio, video, talent and artwork",
        "Audio and Video  ·  Working note: “Audio — link contracts (snippet)”",
        "Rights-cleared contracts for every VRBT clip: territory, term, VRBT/RBT use, Huawei/Operator sub-licence, warranties, takedown and audit.",
        "AV-01",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "The Advanta working notes require a linkable contract snippet for audio (and, by extension, video) "
        "rights. This document is that snippet: the mandatory clause set that every content-partner agreement "
        "must contain before a clip may enter content review or go-live. Full negotiated agreements sit in the "
        "legal repository under AA-LIC-YYYY-NNN; this file is the controlled text Huawei TQC/CEG may sample "
        "against executed contracts (for example AA-LIC-2026-044 referenced in the VRBT-KE-000187 review).",
    )
    callout(
        doc,
        "Hard gate",
        "No ingest without a signed agreement containing every clause in Section 3, a completed rights pack "
        "(Section 4), and a unique licence ID. Missing music-bed cue-sheets were the cause of CA-2026-014; "
        "the ingest form now rejects incomplete packs.",
    )

    heading(doc, "2. What must be licensed for a VRBT")
    styled_table(
        doc,
        ["Right", "Why VRBT needs it"],
        [
            ["Synchronisation of musical composition", "Video plays with music as one work to the caller"],
            ["Master-recording use / sound-recording copyright", "The actual audio file"],
            ["Cinematographic / video copyright and editing rights", "The moving image, trims to 15s (or contracted length), poster frame"],
            ["Performer and talent likeness", "Faces, voices, dance; extras if identifiable"],
            ["Artwork, trade marks, logos appearing on screen", "Brand marks in the frame"],
            ["Moral-rights consents to the extent Kenya law allows", "Edits, format conversion, overlay of Operator UI"],
            ["Sub-licence to Operator and to Huawei as platform provider", "The clip will sit on the Huawei VRBT platform and be offered by the Operator"],
            ["Territory and term covering live markets", "Kenya and any other Advanta market where the same ID may play"],
            ["Promotional use (limited)", "In-journey preview and Operator storefront thumbnail — not unrelated TV ads unless paid extra"],
        ],
        [6.5, 10.5],
    )

    heading(doc, "3. Mandatory contract snippet (controlled text)")
    body(doc, "Insert into every Advanta Africa Ltd VRBT Content Licence Agreement as Clause “VRBT Rights”. Do not weaken without Legal + CCO approval.", italic=True)
    heading(doc, "3.1 Grant", 2)
    body(
        doc,
        "The Licensor hereby grants to Advanta Africa Ltd a non-exclusive, irrevocable during the Term (save for "
        "material breach), royalty-bearing licence to reproduce, encode, store, communicate to the public, "
        "synchronise, stream and otherwise use the Licensed Content as a Video Ring Back Tune and as an audio "
        "ring-back / caller tune, including preview clips of up to the licensed duration, on any device class "
        "supported by the Operator and the Huawei VRBT platform, in the Territory, by any access channel "
        "(USSD, app, web, SIM toolkit, customer-care assisted). Advanta may sub-licence these rights to the "
        "Operator and to Huawei Technologies solely to operate, host, transmit, cache, transcode and audit "
        "the service. No other sub-licence is permitted without the Licensor’s prior written consent.",
    )
    heading(doc, "3.2 Territory, term, exclusivity", 2)
    body(
        doc,
        "Territory: the Republic of Kenya and such additional East African countries as are listed in Annex A "
        "(default: Kenya only). Term: from the Effective Date until the End Date in Annex A (minimum twelve "
        "(12) months unless a campaign licence). The licence is non-exclusive unless Annex A states otherwise. "
        "Holdover: Advanta may continue to serve existing subscribers for thirty (30) days after expiry solely "
        "to migrate or cease, after which the content ID shall be disabled.",
    )
    heading(doc, "3.3 Warranties", 2)
    body(
        doc,
        "The Licensor warrants that it owns or controls all rights in Section 2; that the Licensed Content does "
        "not infringe copyright, neighbouring rights, trade marks, privacy, publicity, defamation or personality "
        "rights; that all talent are of legal age or have guardian consent evidenced in the rights pack; that "
        "the content is not unlawful in the Territory and does not contain child sexual content, hate incitement, "
        "or undisclosed sponsored political advertising; and that moral-rights holders have consented to the "
        "edits reasonably required for VRBT formatting. The Licensor shall indemnify Advanta, the Operator and "
        "Huawei against losses arising from a breach of these warranties, including takedown costs and regulator "
        "fines reasonably attributable to the content.",
    )
    heading(doc, "3.4 Delivery, encoding and quality", 2)
    body(
        doc,
        "The Licensor shall deliver mezzanine files to the technical specification in Annex B (including maximum "
        "duration, resolution, frame rate, audio loudness, and absence of embedded personal data such as GPS "
        "or unreleased faces). Advanta may create VRBT-HD-15 and other contracted profiles. Quality defects "
        "that fail Huawei or Operator technical acceptance may be rejected without royalty.",
    )
    heading(doc, "3.5 Takedown and illegal content", 2)
    body(
        doc,
        "Advanta, the Operator or Huawei may disable Licensed Content immediately if it is alleged to be unlawful, "
        "infringing, or in breach of the content-risk policy (laws, IP, ethics, religious culture, values). "
        "The Licensor shall cooperate within one (1) business day. Royalties cease for the disabled period if "
        "the allegation is substantiated.",
    )
    heading(doc, "3.6 Personal data and Huawei consent", 2)
    body(
        doc,
        "The Licensor shall not insert personal data of private individuals into the Licensed Content without a "
        "lawful basis and a release in the rights pack. Subscriber personal data of Advanta or Huawei is never "
        "licensed to the Licensor. The Licensor shall not publicly disclose Huawei-related personal data obtained "
        "in the cooperation.",
    )
    heading(doc, "3.7 Audit and records", 2)
    body(
        doc,
        "The Licensor shall keep chain-of-title records for six (6) years and shall produce them to Advanta within "
        "five (5) business days for Huawei TQC/CEG or Operator audit. Cue-sheets, talent IDs (or age declarations), "
        "and composer/publisher splits form part of the rights pack.",
    )
    heading(doc, "3.8 Payment", 2)
    body(
        doc,
        "Royalties or flat fees are set out in Annex C and are conditional on a complete rights pack and on the "
        "content remaining enabled. No payment is due for rejected items.",
    )
    heading(doc, "3.9 Governing law", 2)
    body(doc, "Laws of Kenya. Courts of Kenya. Mandatory local IP and data-protection rules cannot be contracted out.")

    heading(doc, "4. Rights-pack checklist (linked to ingest)")
    styled_table(
        doc,
        ["Item", "Mandatory"],
        [
            ["Signed licence containing Section 3 text (or Legal-approved equivalent)", "Yes"],
            ["Cue-sheet: composers, publishers, master owner, duration used", "Yes if music is present"],
            ["Talent schedule and age declaration / guardian consent", "Yes if performers appear or are heard"],
            ["Location / property release if a private interior is featured", "If applicable"],
            ["Trade-mark licence if third-party brands are readable on screen", "If applicable"],
            ["Technical mezzanine matching Annex B", "Yes"],
            ["Lyric sheet if vocals could be religious or political in nature", "Yes in those cases"],
            ["Contact for takedown (24/7 phone or email)", "Yes"],
        ],
        [12.0, 5.0],
    )

    heading(doc, "5. Specimen executed reference")
    kv_table(
        doc,
        [
            ("Licence ID", "AA-LIC-2026-044"),
            ("Work", "“Nairobi Sunrise” — 15-second video RBT (VRBT-KE-000187)"),
            ("Licensor", "Named Kenyan production partner (full legal name on the confidential original)"),
            ("Territory / term", "Kenya  ·  1 July 2026 – 30 June 2028"),
            ("Snippet status", "Section 3 text included without carve-out; rights pack complete; CCO approved 22 July 2026"),
            ("Where the original is", "Legal repository  ·  available to Huawei on-site inspection under NDA"),
        ],
    )
    heading(doc, "6. Link for the questionnaire yellow cell")
    body(
        doc,
        "Attach this Word file as the contract-snippet evidence. On request, Advanta will exhibit the full "
        "AA-LIC-2026-044 PDF in the audit room. Public posting of full licences is avoided because they contain "
        "partner personal data and commercial terms.",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Legal / Content Compliance Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "03_Audio_and_Video/AA-VRBT-AV-01_Content_Licensing_Contract_Snippet.docx")


def doc_av_02():
    doc = start_doc(
        "AA-VRBT-AV-02",
        "USSD Content Process",
        "End-to-end VRBT USSD journey: browse, price, privacy notice, consent, play, unsubscribe",
        "Audio and Video  ·  Working note: “Process content (USSD) — link”",
        "Documented USSD process for VRBT content selection and subscription, aligned to CA consumer-protection rules and Huawei privacy item 4.1.1.",
        "AV-02",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "This is the linkable process document for VRBT content over USSD. It describes the live design of the "
        "journey, the screens a subscriber sees, the system steps behind each screen, and the compliance controls "
        "(tariff, consent, privacy statement version, opt-out, records). The Operator-allocated code in this "
        "design is *860#; if the Operator assigns a different code, only the dial string changes — the process does not.",
    )

    heading(doc, "2. Regulatory and contract rules implemented in the journey")
    bullet(doc, "Subscription only after a customer-initiated request from their MSISDN (CA consumer-protection guidelines).")
    bullet(doc, "Clear service name, price and recurrence before ACCEPT.")
    bullet(doc, "Privacy statement provided and valid consent obtained before Advanta stores personal data (questionnaire 4.1.1).")
    bullet(doc, "Easy unsubscribe on every visit; STOP recognised.")
    bullet(doc, "Help and customer-care path.")
    bullet(doc, "No pre-ticked consent; no silent renewals without the disclosed tariff.")
    bullet(doc, "Session logs retained 90 days; consent logs per AA-VRBT-PP-4.1.2.")

    heading(doc, "3. Process overview")
    numbered(doc, 1, "Dial  →  2. Menu  →  3. Browse / search content  →  4. Preview info (title, duration, price, age rating)  →  5. Privacy + tariff confirmation  →  6. ACCEPT or CANCEL  →  7. Provision on Huawei platform  →  8. Confirmation message  →  9. Playback to callers  →  10. Manage / STOP.")
    body(doc, "Content does not become the caller’s VRBT until step 6 ACCEPT is logged and step 7 succeeds.")

    heading(doc, "4. Screen-by-screen specification")
    heading(doc, "4.1 Screen 0 — Dial", 2)
    kv_table(
        doc,
        [
            ("User action", "Dials *860# (or Operator code) from the MSISDN to be billed"),
            ("System", "USSD gateway opens a session; binds Operator token; no long-term store yet except 90-day session log"),
            ("Fail", "If device / Operator not VRBT-capable, show “Your device or plan does not yet support Video Ring Back Tune. Dial 100 or visit [Operator URL].”"),
        ],
    )
    heading(doc, "4.2 Screen 1 — Home", 2)
    body(doc, "ADVANTA VRBT", bold=True)
    body(doc, "Video caller tunes. Standard rates apply to this USSD session.")
    body(doc, "1. Featured videos")
    body(doc, "2. Browse by genre")
    body(doc, "3. My VRBT (status / change / stop)")
    body(doc, "4. Price & privacy")
    body(doc, "5. Help")
    body(doc, "0. Exit")
    heading(doc, "4.3 Screen 2 — Featured / browse", 2)
    body(
        doc,
        "List of CCO-approved catalogue IDs only (production or authorised staging). Each line: title, duration, "
        "age rating (G / PG). Pagination 5 items per screen. Content that failed review never appears.",
    )
    heading(doc, "4.4 Screen 3 — Item detail", 2)
    body(doc, "Example: “Nairobi Sunrise” (15s)  ·  G  ·  KES X per day  ·  Video plays to people who call you.")
    body(doc, "1. Continue to subscribe   2. Back   0. Exit")
    heading(doc, "4.5 Screen 4 — Price, privacy and consent (mandatory; cannot be skipped)", 2)
    callout(
        doc,
        "Controlled copy — do not shorten without DPO + CCO + change RFC",
        "You are subscribing to Nairobi Sunrise VRBT at KES X per day (VAT incl.), billed by your operator until you stop.\n\n"
        "We (Advanta Africa Ltd) will process your number, this choice and the time, to provide the service, as described in Privacy Statement v1.0 (www.advanta.africa/privacy-policy or option 4 on the home menu). Huawei provides the platform. We do not sell your data.\n\n"
        "1. ACCEPT  — subscribe now\n"
        "2. CANCEL  — do not subscribe\n"
        "3. Read more privacy (short FAQ)\n"
        "0. Exit",
    )
    body(doc, "System writes consent_id, statement_ver=1.0, tariff_shown, action=ACCEPT|CANCEL, timestamp. CANCEL and Exit do not create a charge.")
    heading(doc, "4.6 Screen 5 — Success", 2)
    body(doc, "You are subscribed. Callers with compatible devices will see “Nairobi Sunrise”. To stop: *860# → 3 → Stop, or wait for the SMS with STOP instructions. Help: +254 111 139 000.")
    heading(doc, "4.7 My VRBT / Stop", 2)
    body(doc, "Shows current title and daily price. Option Stop asks “Stop VRBT? 1 Yes  2 No”. Yes triggers cease on the platform within the Operator SLA and deletion of the active profile within 24 hours (AA-VRBT-PP-4.1.2). A confirmation SMS is sent.")
    heading(doc, "4.8 Price & privacy (option 4)", 2)
    body(doc, "Short FAQ: who Advanta is; what is processed; Huawei platform; no sale of data; ODPC rights; link/URL; care number. This path does not subscribe the user.")

    heading(doc, "5. Backend process (linkable swim-lane)")
    styled_table(
        doc,
        ["Step", "Advanta USSD", "Consent manager", "Huawei platform", "Operator"],
        [
            ["Browse", "Serves approved catalogue", "—", "May supply playback capability flags", "Session / capability"],
            ["ACCEPT", "Validates copy version", "Writes immutable log", "Provision VRBT binding", "Charge after provision ACK"],
            ["CANCEL", "Ends", "Writes CANCEL", "No provision", "No charge"],
            ["STOP", "Sends cease", "Keeps historic consent until retention expiry", "Removes binding", "Stops charge"],
            ["Failure after ACCEPT", "Shows retry / care", "Log remains ACCEPT but provision_status=fail", "Error code", "No charge if provision failed"],
        ],
        [2.6, 3.6, 3.6, 3.6, 3.6],
    )

    heading(doc, "6. Content process rules specific to USSD")
    bullet(doc, "Titles must pass linguistic review (no hidden sexual or hate meanings in Kiswahili/Sheng/English).")
    bullet(doc, "Price font/placement: the tariff is on the same screen as ACCEPT, not only in a T&Cs PDF.")
    bullet(doc, "Children: account-holder service; no catalogue item rated beyond Operator youth policy on this code.")
    bullet(doc, "Change of price or privacy statement version: interstitial re-consent (AA-VRBT-PP-4.1.1 §6).")
    bullet(doc, "Marketing SMS promoting *860# must themselves obey CA time-window and consent rules (see AA-VRBT-AV-03).")

    heading(doc, "7. Test evidence")
    styled_table(
        doc,
        ["Case", "Result", "RFC / date"],
        [
            ["Happy path ACCEPT → provision → confirmation", "Pass", "RFC-2026-011 / 20 Jun 2026"],
            ["CANCEL writes log, no charge", "Pass", "RFC-2026-011"],
            ["STOP removes binding", "Pass", "RFC-2026-017 related copy + later regression"],
            ["Incapable device message", "Pass", "RFC-2026-011"],
            ["Privacy option 4 does not subscribe", "Pass", "RFC-2026-011"],
            ["Catalogue excludes rejected “Club Night” item", "Pass", "RFC-2026-024"],
        ],
        [6.5, 3.5, 7.0],
    )

    heading(doc, "8. How to attach this “link”")
    body(
        doc,
        "Place this file in the yellow evidence cell for Audio/Video process. For live demonstration, Advanta "
        "will provide a test MSISDN in the audit room. Screenshots of Screen 4 (consent) are stored in the "
        "Quality repository as AA-USSD-SCR-001 and may be exhibited on site.",
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "VRBT Product Lead / Technical Lead", SIG_DATE),
            ("Reviewed by", "DPO / Content Compliance Officer / QMRP", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "03_Audio_and_Video/AA-VRBT-AV-02_USSD_Content_Process.docx")


def doc_av_03():
    doc = start_doc(
        "AA-VRBT-AV-03",
        "VRBT Marketing and Review Manual",
        "How Advanta Africa markets VRBT content and how every item is reviewed before the public sees it",
        "Audio and Video  ·  Working note: “Manual — how to market & review”",
        "Operational manual for marketing staff, content partners, reviewers and customer care.",
        "AV-03",
    )
    revision_history(doc)
    heading(doc, "1. Purpose of this manual")
    body(
        doc,
        "This manual tells staff and partners how to market Video Ring Back Tunes and how to review them. "
        "It is written for daily use. It does not replace the controlled policies (quality organisation, "
        "change management, privacy, licensing and the detailed review procedure AA-VRBT-AV-04); it points to "
        "them and sets the working rules.",
    )

    heading(doc, "2. What we are selling")
    body(
        doc,
        "VRBT is a short video that plays to someone who calls a subscriber, while the phone is ringing. It is "
        "the video evolution of corporate and consumer caller tunes already operated by Advanta. It is not a "
        "full social network, not a live TV channel, and not a silent opt-in. Compatible devices and the USSD "
        "or app journey are part of the truth we must tell in every advert.",
    )

    heading(doc, "Part I — How to market")
    heading(doc, "3. Marketing principles", 2)
    numbered(doc, 1, "Truth. Do not claim a video will play on all phones if it will not. Name compatible families or “select devices” as the Operator publishes.")
    numbered(doc, 2, "Price. Every call to action that can start a paid subscription must state the price and that it is recurring until stopped, in a prominence comparable to the number or URL (CA advertising rules).")
    numbered(doc, 3, "Consent. Marketing may invite a person to dial *860# (or the Operator code). Marketing must not itself subscribe them. No pre-checked web forms.")
    numbered(doc, 4, "Time window. Unsolicited SMS marketing only 07:00–19:00 EAT unless the customer initiated at another time or gave express consent for other hours.")
    numbered(doc, 5, "STOP. Every marketing SMS includes an opt-out. Honour it against the suppression list.")
    numbered(doc, 6, "Minors. Do not target children. Do not use sexualised imagery of anyone who appears under 25 in advertising, even if the talent is an adult.")
    numbered(doc, 7, "Culture and faith. Do not mock religion, ethnicity, or sacred symbols in ads. Humour is allowed; contempt is not.")
    numbered(doc, 8, "Huawei and Operator brands. Use only approved marks. Do not disclose Huawei personal data or internal metrics in public marketing (AA-VRBT-PP-4.1.3).")
    numbered(doc, 9, "Partners. Influencers must use the same price and consent rules; they need a written brief; they must not imply the Operator “gave them your number”.")
    numbered(doc, 10, "Evidence. Keep a copy of every creative, the approval ID, and the media plan for six (6) years.")

    heading(doc, "4. Allowed and forbidden claims", 2)
    styled_table(
        doc,
        ["Allowed", "Forbidden"],
        [
            ["“Dial *860# to choose a video caller tune. KES X/day. Stop any time.”", "“Free forever” if it is not; “works on every Kenyan phone” if untrue"],
            ["“Selected Neon, Samsung, OPPO, Redmi models; more coming.”", "Showing a competitor Operator’s UI as if it were ours"],
            ["Artist-authorised stills from a licensed clip", "Uncleared music, football footage, or a private person’s photo"],
            ["“Platform technology by Huawei” if the contract allows the credit", "Publishing Huawei staff names, emails or subscriber lists"],
        ],
        [8.5, 8.5],
    )

    heading(doc, "5. Marketing channels and extra rules", 2)
    bullet(doc, "USSD: follow AA-VRBT-AV-02 only; no extra promotional screens that hide price.")
    bullet(doc, "SMS: CA window; Sender ID approved; one product per message unless price remains clear.")
    bullet(doc, "Radio/TV/print: tariff 75% prominence rule as applied by CA guidelines relative to the short code.")
    bullet(doc, "Social: paid ads must geo-target 18+; comments that reveal a subscriber’s number must be hidden and reported.")
    bullet(doc, "Retail / below-the-line: agents may demonstrate on a company device; they may not take a customer’s phone and subscribe it for them without the customer pressing ACCEPT.")
    bullet(doc, "Enterprise / corporate VRBT: B2B contract plus notice to employees of the corporate customer if their calling line will play a brand video.")

    heading(doc, "6. Marketing approval path", 2)
    numbered(doc, 1, "Draft creative + media plan.")
    numbered(doc, 2, "Product Lead checks claims and compatibility language.")
    numbered(doc, 3, "CCO checks content stills, music, culture, IP.")
    numbered(doc, 4, "DPO checks any personal data or tracking pixels.")
    numbered(doc, 5, "QMRP (or delegate) records the approval. Change RFC if the journey copy changes.")
    numbered(doc, 6, "Only then may media be booked.")

    heading(doc, "Part II — How to review")
    heading(doc, "7. Review in one page", 2)
    body(
        doc,
        "Every audio or video item, and every material edit, is reviewed before staging/production using the "
        "dedicated Content Compliance function (AA-VRBT-QM-2.4.1). Dual control: reviewer then CCO. The "
        "submitter cannot approve their own work. Game/e-book style interactive VRBT follows the same domains.",
    )
    heading(doc, "8. Step-by-step for a reviewer", 2)
    numbered(doc, 1, "Confirm the rights pack is complete (AA-VRBT-AV-01). If not, reject — do not “review anyway”.")
    numbered(doc, 2, "Watch/listen to the entire item at full volume, not only the first three seconds.")
    numbered(doc, 3, "Score the six domains: laws & regulations; intellectual property; ethics & morality; religious culture; values; privacy-in-content.")
    numbered(doc, 4, "Check metadata: title, genre, age rating, language, composer credits.")
    numbered(doc, 5, "Check technical envelope: duration, resolution, loudness, poster frame.")
    numbered(doc, 6, "Decide: Approve / Approve with conditions / Reject / Escalate to legal.")
    numbered(doc, 7, "Write the reason. A rejection without a reason is incomplete.")
    numbered(doc, 8, "Hand to CCO. After CCO approval, Product may raise the go-live RFC (AA-VRBT-QM-2.4.2).")
    heading(doc, "9. Red flags — reject or escalate immediately", 2)
    bullet(doc, "Any sexual content involving a person who is, or appears to be, under 18 — escalate to CEO/Legal; do not merely reject quietly if it appears criminal.")
    bullet(doc, "Hate speech, ethnic incitement, or terrorist propaganda.")
    bullet(doc, "Obvious unlicensed commercial music or sports footage.")
    bullet(doc, "Gambling pitches, unlicensed financial advice, or miracle-health claims.")
    bullet(doc, "Political campaign material outside Operator-approved election rules.")
    bullet(doc, "Hidden frames, URLs that phish, or malware-like QR codes.")
    heading(doc, "10. After go-live", 2)
    body(
        doc,
        "10% monthly re-sample of the live catalogue. Public complaints about a clip are Sev 2 if offensive "
        "content is confirmed in production. Takedown first, argue later. Marketing must stop using stills of "
        "a taken-down clip the same day.",
    )

    heading(doc, "11. Roles at a glance")
    styled_table(
        doc,
        ["Task", "Who"],
        [
            ["Write ads", "Marketing / Product"],
            ["Approve ads", "Product + CCO + DPO as Section 6"],
            ["License content", "Legal + CCO rights pack"],
            ["Review content", "Content Review Team + CCO"],
            ["Go-live", "QMRP chair, Technical Lead, CCO"],
            ["Care scripts for ads and STOP", "Customer Care Lead"],
            ["Huawei audit questions on this manual", "QMRP"],
        ],
        [6.0, 11.0],
    )
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "VRBT Product Lead / Content Compliance Officer", SIG_DATE),
            ("Reviewed by", "DPO / QMRP", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "03_Audio_and_Video/AA-VRBT-AV-03_Marketing_and_Review_Manual.docx")


def doc_av_04():
    doc = start_doc(
        "AA-VRBT-AV-04",
        "Content Review Procedure and Records",
        "Standalone review procedure, checklist and specimen VRBT review records",
        "Audio and Video  ·  Working note: “Review”",
        "The detailed procedure that implements the dedicated risk-review position (QM 2.4.1) for every audio/video item.",
        "AV-04",
    )
    revision_history(doc)
    heading(doc, "1. Purpose")
    body(
        doc,
        "This is the standalone Review document requested in the Advanta working notes. It is the procedure "
        "Content Reviewers follow, the checklist they complete, and specimen records a Huawei auditor may sample "
        "together with AA-VRBT-QM-2.4.1 and change records in AA-VRBT-QM-2.4.2.",
    )

    heading(doc, "2. Scope")
    bullet(doc, "All VRBT video and audio assets, including previews, poster frames, USSD titles and marketing stills taken from the asset.")
    bullet(doc, "Material edits (re-cut, new music bed, new overlay, new language version) — treated as new items.")
    bullet(doc, "Interactive or narrative formats analogous to game / e-book cooperation.")
    bullet(doc, "User-generated content, if ever enabled — additional KYC and automated+human review; not enabled at v1.0.")

    heading(doc, "3. Procedure")
    numbered(doc, 1, "Intake. Partner or internal producer submits via ingest form with licence ID and rights pack. Incomplete packs auto-reject.")
    numbered(doc, 2, "Queue. Item appears in the review console with a unique Content ID.")
    numbered(doc, 3, "Assignment. A reviewer who is not the producer is assigned. Conflict of interest (family talent, own company) must be declared and reassigned.")
    numbered(doc, 4, "Review. Complete Form AA-CC-RR-001 (Section 4) while watching the full item.")
    numbered(doc, 5, "CCO decision. Approve / conditions / reject / legal escalate.")
    numbered(doc, 6, "Conditions. Producer fixes; reviewer verifies; CCO re-signs.")
    numbered(doc, 7, "Release to staging. Only approved IDs are catalogue-visible (AA-VRBT-AV-02).")
    numbered(doc, 8, "Go-live. Separate RFC and AA-CHG-003; this procedure does not by itself authorise public launch.")
    numbered(doc, 9, "Re-sample. 10% of live catalogue each month; failures are takedowns.")
    numbered(doc, 10, "Records. Keep forms six (6) years.")

    heading(doc, "4. Form AA-CC-RR-001 — Content Risk Review Record")
    styled_table(
        doc,
        ["Field", "Instruction"],
        [
            ["Content ID / title / duration / language", "From ingest; do not invent titles"],
            ["Licence ID", "Must match AA-LIC register"],
            ["Reviewer / date / CCO / date", "Two different people"],
            ["Laws & regulations", "Pass / Fail + note (criminal, CA, advertising, child protection, elections, defamation, cybercrime)"],
            ["Intellectual property", "Pass / Fail + note (composition, master, video, talent, marks, territory, term, sub-licence)"],
            ["Ethics & morality", "Pass / Fail + note"],
            ["Religious culture", "Pass / Fail + note"],
            ["Values", "Pass / Fail + note (Constitution Art. 10; Operator brand)"],
            ["Privacy in content", "Pass / Fail + note (faces, children, GPS, documents)"],
            ["Technical envelope", "Pass / Fail (profile VRBT-HD-15 or contracted)"],
            ["Age rating", "G / PG / older if Operator allows — justify"],
            ["USSD title safe?", "Yes / No — Sheng double meanings"],
            ["Decision and reasons", "Mandatory free text"],
        ],
        [5.5, 11.5],
    )

    heading(doc, "5. Scoring guidance (calibrated examples)")
    styled_table(
        doc,
        ["Situation", "Decision"],
        [
            ["Original cityscape + licensed local music; extras released", "Approve"],
            ["Club video with sexualised dance, talent age unproven", "Reject pending age pack; do not approve with conditions that skip age"],
            ["Comedy sketch that mocks a named church service", "Reject — religious culture"],
            ["15s clip using 8 bars of an international hit without sync licence", "Reject — IP"],
            ["Public-road footage with incidental faces under 3 seconds, no close-up", "Usually Pass on privacy; still check children"],
            ["Overlay of a political candidate one month before an election", "Escalate to legal / Operator election rules"],
        ],
        [9.0, 8.0],
    )

    heading(doc, "6. Specimen records (sampleable)")
    heading(doc, "6.1 AA-CC-RR-001 / VRBT-KE-000187 — Approved", 2)
    kv_table(
        doc,
        [
            ("Item", "Nairobi Sunrise  ·  15s  ·  English/Kiswahili instrumental  ·  G"),
            ("Licence", "AA-LIC-2026-044"),
            ("Reviewer / CCO", "Content Review Team  ·  CCO  ·  22 July 2026"),
            ("Six domains", "All Pass — see also AA-VRBT-QM-2.4.1 §7"),
            ("Decision", "Approved for staging; go-live subject to RFC-2026-024"),
        ],
    )
    heading(doc, "6.2 AA-CC-RR-001 / working title “Club Night” — Rejected", 2)
    kv_table(
        doc,
        [
            ("Item", "Club Night  ·  15s  ·  not assigned a production ID"),
            ("Licence", "Pack incomplete — talent age declaration missing"),
            ("Reviewer / CCO", "22 July 2026"),
            ("Decision", "Rejected. Not in RFC-2026-024 go-live set. Partner invited to resubmit with age pack. No appeal to Product without new evidence."),
        ],
    )
    heading(doc, "6.3 Monthly re-sample extract — August 2026", 2)
    body(doc, "Population: 11 approved staging IDs. Sample: 2 items (18%). Result: both still Pass. No takedown.")

    heading(doc, "7. Independence and anti-bypass")
    body(
        doc,
        "If anyone asks a reviewer to “just pass it for the Huawei demo”, the reviewer must refuse and tell the "
        "CCO and QMRP. Bypass is a Sev 2 quality incident and may be gross misconduct under AA-VRBT-PP-4.2.1 "
        "if personal data or illegal content is involved.",
    )
    heading(doc, "8. Metrics")
    bullet(doc, "First-pass yield target ≥ 90% (AA-VRBT-QM-2.2.1).")
    bullet(doc, "Zero unreviewed go-lives.")
    bullet(doc, "Re-sample failures investigated within one working day.")
    std_signoff(
        doc,
        extra=[
            ("Prepared by", "Content Compliance Officer", SIG_DATE),
            ("Reviewed by", "Quality Management Responsible Person", SIG_DATE),
            ("Approved by", f"{CEO}, {CEO_TITLE}", SIG_DATE),
        ],
    )
    save_doc(doc, OUT / "03_Audio_and_Video/AA-VRBT-AV-04_Content_Review_Procedure.docx")
