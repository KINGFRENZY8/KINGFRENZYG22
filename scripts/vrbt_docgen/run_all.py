#!/usr/bin/env python3
"""Generate the full Advanta Africa VRBT Huawei audit evidence pack."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vrbt_docgen.org_chart import generate_all as make_charts
from vrbt_docgen.generate_part1 import doc_index, doc_qm_211, doc_qm_221
from vrbt_docgen.generate_part2 import doc_qm_231, doc_qm_241, doc_qm_242
from vrbt_docgen.generate_part3 import doc_pp_411, doc_pp_412, doc_pp_413, doc_pp_414
from vrbt_docgen.generate_part3b import doc_pp_415, doc_pp_421, doc_pp_422
from vrbt_docgen.generate_part4 import doc_av_01, doc_av_02, doc_av_03, doc_av_04

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "VRBT_Audit_Evidence"
ASSETS = OUT / "assets"


def main():
    print("Drawing organisation charts...")
    internal, customer = make_charts(ASSETS)
    print("  ", internal)
    print("  ", customer)

    steps = [
        ("Index", doc_index),
        ("QM 2.1.1", lambda: doc_qm_211(internal, customer)),
        ("QM 2.2.1", doc_qm_221),
        ("QM 2.3.1", doc_qm_231),
        ("QM 2.4.1", doc_qm_241),
        ("QM 2.4.2", doc_qm_242),
        ("PP 4.1.1", doc_pp_411),
        ("PP 4.1.2", doc_pp_412),
        ("PP 4.1.3", doc_pp_413),
        ("PP 4.1.4", doc_pp_414),
        ("PP 4.1.5", doc_pp_415),
        ("PP 4.2.1", doc_pp_421),
        ("PP 4.2.2", doc_pp_422),
        ("AV-01", doc_av_01),
        ("AV-02", doc_av_02),
        ("AV-03", doc_av_03),
        ("AV-04", doc_av_04),
    ]
    for name, fn in steps:
        print(f"Writing {name}...")
        fn()
    print("Done. Files:")
    for p in sorted(OUT.rglob("*.docx")):
        print(f"  {p.relative_to(ROOT)}  ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
