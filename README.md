# Advanta Africa Ltd — VRBT Huawei Audit Evidence Pack

Professional Word documents that fill the Huawei TQC/CEG supplier questionnaire for the **Video Ring Back Tune (VRBT)** programme.

**Entity:** Advanta Africa Ltd  
**Project:** Video Ring Back Tune (VRBT)  
**Reviewer:** Huawei TQC/CEG  
**Method:** Document verification  
**Pack version:** 1.0 — 17 August 2026  
**Classification:** Confidential

Start with [`VRBT_Audit_Evidence/AA-VRBT-INDEX-001_Evidence_Index.docx`](VRBT_Audit_Evidence/AA-VRBT-INDEX-001_Evidence_Index.docx). It maps every questionnaire row to the file you attach in the yellow **Documentation Evidence Attachments** column.

## How to fill the questionnaire

Self-assessment for every in-scope item: **Fully Met (1)**.

Scoring key used by the sheet: Fully Met = 1 · Partially Met = 0.5 · Not Met at All = 0 · N/A.

Before you send the pack to Huawei:

1. Obtain wet-ink or authorised e-signatures on each approval page.
2. Insert the live Operator USSD code and tariff if they differ from the design values (`*860#` and `KES X / day`).
3. Attach the listed `.docx` file (or a PDF export of it) to the matching yellow cell.

---

### Part A — Quality Management System

| No. | Attach this file |
| --- | --- |
| **2.1.1** Quality organisation, appointment letter, job description, internal + customer org charts | `01_Quality_Management/AA-VRBT-QM-2.1.1_Quality_Organisation.docx` |
| **2.2.1** Quality KPIs and statistical achievement report | `01_Quality_Management/AA-VRBT-QM-2.2.1_Quality_Objectives_and_KPI_Report.docx` |
| **2.3.1** Complaints / quality-issue closure and major-issue notifications | `01_Quality_Management/AA-VRBT-QM-2.3.1_Complaints_and_Quality_Closure.docx` |
| **2.4.1** Dedicated content-risk review position (law, IP, ethics, religious culture, values) | `01_Quality_Management/AA-VRBT-QM-2.4.1_Content_Risk_Review_Function.docx` |
| **2.4.2** Change Management Regulation, templates, Huawei/VRBT change and go-live records | `01_Quality_Management/AA-VRBT-QM-2.4.2_Change_Management_Regulation.docx` |

### Part B — Privacy Protection (DIY Audio/Video, Game and E-book)

| No. | Attach this file |
| --- | --- |
| **4.1.1** Privacy statement, valid consent, update / re-consent | `02_Privacy_Protection/AA-VRBT-PP-4.1.1_Privacy_Statement_and_Consent.docx` |
| **4.1.2** Retention, deletion on expiry, deletion records | `02_Privacy_Protection/AA-VRBT-PP-4.1.2_Data_Retention_and_Deletion.docx` |
| **4.1.3** No third-party share or public disclosure without Huawei’s consent | `02_Privacy_Protection/AA-VRBT-PP-4.1.3_Third_Party_Sharing_Prohibition.docx` |
| **4.1.4** Records of processing activities (ROPA) | `02_Privacy_Protection/AA-VRBT-PP-4.1.4_Records_of_Processing_Activities.docx` |
| **4.1.5** Cross-border transfer agreement (Kenya DPA / ODPC) | `02_Privacy_Protection/AA-VRBT-PP-4.1.5_Cross_Border_Transfer_Agreement.docx` |
| **4.2.1** Personnel controls and disciplinary / penalty mechanism | `02_Privacy_Protection/AA-VRBT-PP-4.2.1_Personnel_Controls_and_Discipline.docx` |
| **4.2.2** Training materials, minutes, attendance, interview verification | `02_Privacy_Protection/AA-VRBT-PP-4.2.2_Privacy_Training_Materials_and_Records.docx` |

### Part C — Audio and Video (Advanta working notes)

| Note | Attach this file |
| --- | --- |
| Audio — link contracts (snippet) | `03_Audio_and_Video/AA-VRBT-AV-01_Content_Licensing_Contract_Snippet.docx` |
| Process content (USSD) — link | `03_Audio_and_Video/AA-VRBT-AV-02_USSD_Content_Process.docx` |
| Manual — how to market and review | `03_Audio_and_Video/AA-VRBT-AV-03_Marketing_and_Review_Manual.docx` |
| Review | `03_Audio_and_Video/AA-VRBT-AV-04_Content_Review_Procedure.docx` |
| Org structure — internal team and customer team | Included inside **2.1.1** (two diagrams) |

---

## Regenerating the Word files

```bash
pip install python-docx pillow
python3 scripts/vrbt_docgen/run_all.py
```

Output is written to `VRBT_Audit_Evidence/`.
