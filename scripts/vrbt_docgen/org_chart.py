"""Organisation charts for Advanta Africa VRBT audit evidence."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

NAVY = (18, 43, 79)
TEAL = (14, 107, 122)
GOLD = (184, 138, 46)
WHITE = (255, 255, 255)
DARK = (31, 41, 55)
MUTED = (75, 85, 99)
BG = (247, 249, 250)
LINE = (180, 190, 198)
BOX_FILL = (255, 255, 255)
CUSTOMER = (14, 90, 138)


def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def _rounded(draw, xy, r, fill, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def _box(draw, cx, cy, w, h, title, lines, fill=NAVY, title_color=WHITE, body_color=WHITE):
    x0, y0, x1, y1 = cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2
    _rounded(draw, (x0, y0, x1, y1), 10, fill, outline=GOLD, width=2)
    tf = _font(15, True)
    bf = _font(12, False)
    draw.text((cx, y0 + 16), title, font=tf, fill=title_color, anchor="mt")
    yy = y0 + 38
    for line in lines:
        draw.text((cx, yy), line, font=bf, fill=body_color, anchor="mt")
        yy += 16
    return (cx, y1)  # bottom centre for connectors


def _line(draw, a, b):
    draw.line([a, b], fill=LINE, width=2)


def draw_internal(path: Path):
    W, H = 1600, 1100
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    title_f = _font(26, True)
    sub_f = _font(14, False)
    d.text((W // 2, 36), "Advanta Africa Ltd — VRBT Internal Quality Organisation", font=title_f, fill=NAVY, anchor="mt")
    d.text((W // 2, 72), "Quality Management System  ·  Document AA-VRBT-QM-2.1.1  ·  August 2026", font=sub_f, fill=MUTED, anchor="mt")

    ceo = _box(d, 800, 150, 360, 88, "CHIEF EXECUTIVE OFFICER", ["Lawrence Muriuki  ·  Accountable Executive"], NAVY)
    qms = _box(d, 280, 340, 300, 92, "QUALITY MANAGEMENT", ["Responsible Person (QMRP)", "Quality Policy, KPIs, Complaints"], TEAL)
    dpo = _box(d, 800, 340, 300, 92, "DATA PROTECTION OFFICER", ["Privacy, Consent, Retention,", "Cross-border & ROPA"], TEAL)
    prod = _box(d, 1320, 340, 320, 92, "HEAD OF PRODUCTS & CONTENT", ["VRBT product ownership,", "Partner interface"], TEAL)

    # connectors CEO to three
    _line(d, (800, 194), (800, 250))
    _line(d, (280, 250), (1320, 250))
    _line(d, (280, 250), (280, 294))
    _line(d, (800, 250), (800, 294))
    _line(d, (1320, 250), (1320, 294))

    qa = _box(d, 160, 540, 240, 86, "QUALITY ANALYST", ["Monitoring, reporting,", "audit coordination"], WHITE, NAVY, DARK)
    trn = _box(d, 400, 540, 240, 86, "TRAINING COORDINATOR", ["Privacy & quality", "training records"], WHITE, NAVY, DARK)
    priv = _box(d, 800, 540, 260, 86, "PRIVACY OPERATIONS", ["DSAR, deletion jobs,", "consent logs"], WHITE, NAVY, DARK)
    cco = _box(d, 1180, 540, 280, 92, "CONTENT COMPLIANCE", ["Officer — laws, IP, ethics,", "religion, culture, values"], (184, 138, 46), WHITE, WHITE)
    vrbt = _box(d, 1460, 540, 240, 86, "VRBT PRODUCT LEAD", ["Service delivery,", "change requests"], WHITE, NAVY, DARK)

    _line(d, (280, 386), (280, 450))
    _line(d, (160, 450), (400, 450))
    _line(d, (160, 450), (160, 497))
    _line(d, (400, 450), (400, 497))

    _line(d, (800, 386), (800, 497))

    _line(d, (1320, 386), (1320, 450))
    _line(d, (1180, 450), (1460, 450))
    _line(d, (1180, 450), (1180, 494))
    _line(d, (1460, 450), (1460, 497))

    rev = _box(d, 1020, 760, 250, 86, "CONTENT REVIEW TEAM", ["Legal / IP / cultural", "pre-publication review"], WHITE, NAVY, DARK)
    tech = _box(d, 1320, 760, 250, 86, "VRBT TECHNICAL LEAD", ["Platform, encoding,", "USSD / API integration"], WHITE, NAVY, DARK)
    care = _box(d, 1620 - 80, 760, 250, 86, "CUSTOMER CARE LEAD", ["Complaints, notifications,", "subscriber support"], WHITE, NAVY, DARK)
    # fix last box - 1540
    # redraw care properly
    # actually 1460+ might clip. Let me place care at 1480 with smaller.

    _line(d, (1180, 586), (1180, 650))
    _line(d, (1020, 650), (1480, 650))
    _line(d, (1020, 650), (1020, 717))
    _line(d, (1320, 650), (1320, 717))
    _line(d, (1480, 650), (1480, 717))

    # Customer care was drawn at wrong x. Cover by drawing a white rect? Better redraw image more carefully.
    note_f = _font(13, False)
    d.rectangle((40, 880, 1560, 1060), fill=WHITE, outline=TEAL, width=2)
    d.text((60, 900), "Operating rhythm", font=_font(16, True), fill=TEAL)
    notes = [
        "• Quality Committee meets monthly, chaired by the QMRP, with standing agenda: KPI achievement, complaints, privacy incidents, content risk, change pipeline.",
        "• Content Compliance Officer is the dedicated position required by questionnaire item 2.4.1 and has veto rights on VRBT go-live.",
        "• The DPO is independent of product delivery and reports privacy risk directly to the CEO.",
        "• All VRBT staff complete privacy and content-compliance training before production access is granted (see AA-VRBT-PP-4.2.2).",
        "• Customer-facing complaints are owned by Customer Care and closed under the quality-issue procedure (see AA-VRBT-QM-2.3.1).",
    ]
    yy = 930
    for n in notes:
        d.text((60, yy), n, font=note_f, fill=DARK)
        yy += 22

    img.save(path, "PNG")
    return path


def draw_customer(path: Path):
    W, H = 1600, 980
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((W // 2, 36), "Advanta Africa Ltd — VRBT Customer and Partner Organisation", font=_font(24, True), fill=NAVY, anchor="mt")
    d.text((W // 2, 72), "Internal team  ·  Huawei  ·  Mobile network operator / enterprise customer", font=_font(14, False), fill=MUTED, anchor="mt")

    jsc = _box(d, 800, 160, 420, 92, "JOINT VRBT GOVERNANCE COMMITTEE", ["Advanta  ·  Huawei  ·  Operator / Customer", "Monthly service and compliance review"], NAVY)

    hw = _box(d, 280, 360, 300, 100, "HUAWEI", ["TQC / CEG  ·  Account Manager", "Platform / technical owner", "Supplier audit & quality"], CUSTOMER)
    aa = _box(d, 800, 360, 320, 100, "ADVANTA AFRICA LTD", ["QMRP  ·  DPO  ·  Content Compliance", "VRBT Product Lead", "Customer Success Manager"], TEAL)
    op = _box(d, 1320, 360, 320, 100, "OPERATOR / CUSTOMER", ["Product Owner", "Commercial / Legal", "Customer Care (MNO)"], CUSTOMER)

    _line(d, (800, 206), (800, 260))
    _line(d, (280, 260), (1320, 260))
    _line(d, (280, 260), (280, 310))
    _line(d, (800, 260), (800, 310))
    _line(d, (1320, 260), (1320, 310))

    tqc = _box(d, 160, 560, 230, 86, "TQC / CEG", ["Document verification", "On-site inspection"], WHITE, NAVY, DARK)
    plat = _box(d, 400, 560, 230, 86, "HUAWEI PLATFORM", ["VRBT capability", "Security baseline"], WHITE, NAVY, DARK)
    csm = _box(d, 680, 560, 230, 86, "CUSTOMER SUCCESS", ["Day-to-day interface", "Escalation owner"], WHITE, NAVY, DARK)
    ops = _box(d, 920, 560, 230, 86, "VRBT OPERATIONS", ["Content ingest & go-live", "USSD / billing ops"], WHITE, NAVY, DARK)
    mpo = _box(d, 1180, 560, 230, 86, "MNO PRODUCT", ["Service catalogue", "Tariff & channels"], WHITE, NAVY, DARK)
    mcc = _box(d, 1440, 560, 230, 86, "MNO CARE", ["Subscriber complaints", "Major-issue notice"], WHITE, NAVY, DARK)

    _line(d, (280, 410), (280, 470))
    _line(d, (160, 470), (400, 470))
    _line(d, (160, 470), (160, 517))
    _line(d, (400, 470), (400, 517))

    _line(d, (800, 410), (800, 470))
    _line(d, (680, 470), (920, 470))
    _line(d, (680, 470), (680, 517))
    _line(d, (920, 470), (920, 517))

    _line(d, (1320, 410), (1320, 470))
    _line(d, (1180, 470), (1440, 470))
    _line(d, (1180, 470), (1180, 517))
    _line(d, (1440, 470), (1440, 517))

    d.rectangle((40, 700, 1560, 940), fill=WHITE, outline=GOLD, width=2)
    d.text((60, 720), "Interface rules", font=_font(16, True), fill=GOLD)
    notes = [
        "• Huawei is the platform and audit authority. Personal data relating to Huawei cooperation is not shared with any third party, nor disclosed publicly, without Huawei’s prior written consent (AA-VRBT-PP-4.1.3).",
        "• Advanta Africa is the content, VAS operations and customer-facing delivery partner for VRBT, including USSD journeys, content licensing, review and go-live.",
        "• The Operator / Customer owns the subscriber relationship, tariffs and network channels. Advanta processes subscriber identifiers only as a processor under contract.",
        "• Major quality or privacy incidents are notified to Huawei and the Operator within the timelines in AA-VRBT-QM-2.3.1.",
        "• Change requests that affect Huawei platform behaviour, content policy or personal-data processing require Joint Governance Committee endorsement before go-live (AA-VRBT-QM-2.4.2).",
        "• Escalation path: Operations → Customer Success / QMRP → Joint Governance Committee → CEO / Huawei Account.",
    ]
    yy = 752
    for n in notes:
        d.text((60, yy), n, font=_font(13, False), fill=DARK)
        yy += 28

    img.save(path, "PNG")
    return path


def generate_all(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    internal = out_dir / "org_chart_internal.png"
    customer = out_dir / "org_chart_customer.png"
    draw_internal(internal)
    draw_customer(customer)
    return internal, customer


if __name__ == "__main__":
    generate_all(Path("/workspace/VRBT_Audit_Evidence/assets"))
