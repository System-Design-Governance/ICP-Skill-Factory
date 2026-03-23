#!/usr/bin/env python3
"""
gen_pdf.py — F6 ONS OT System Architecture PDF Proposal Generator
Strategy: reportlab for text pages + d2 CLI for diagram PDFs + pypdf merger
"""

import os
import sys
import subprocess
from pathlib import Path
from reportlab.lib.pagesizes import A3, landscape, A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle
)
from pypdf import PdfWriter, PdfReader

NAVY = HexColor("#0C3467")
SKY = HexColor("#008EC3")
GRAY = HexColor("#9B9B9B")
LIGHT_BG = HexColor("#f8f9fa")

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR.parent / "05_release"
TMP_DIR = BASE_DIR / "_tmp_pdf"

CHAPTERS = [
    ("f6_overview", "System Overview",
     "Inter-diagram map showing all 8 subsystem relationships. "
     "OT PRP Network (IEC 62439-3) + IT/Safety Network (Fortinet)."),
    ("f6_prot", "Protection Relay System",
     "7SL86 x8 | 7UT86 x20 | 7SJ82 x32 | 7SS85 x6 | 7SJ85 x2 | "
     "SICAM P850 x28 | 6MD85 BCU x27 | RCP Panel x28"),
    ("f6_scada", "SCADA + Network + Cybersecurity",
     "WinCC OA 100K I/O | FortiSwitch 448E x5 | FortiSwitch 124F x22 | "
     "FortiGate 80F x3 | FortiAP x16 | FortiNDR + FortiAnalyzer | RTU x4"),
    ("f6_cctv", "CCTV Surveillance System",
     "IP Camera x20 | NVR x2 (64ch H.265) | Video Wall 9x3 | Milestone VMS"),
    ("f6_acs", "Access Control + Intrusion Detection",
     "ACS Panel x5 | Card Reader x15 | EM Lock x20 | PIR Sensor x30 | Alarm x8"),
    ("f6_telecom", "Telecom System (VoIP + WiFi + Radio)",
     "IP-PBX 30-ext | IP Phone x30 | Outdoor Phone x3 | Radio x10 | FortiAP x16"),
    ("f6_power", "Power Supply System (DC / UPS / EDG)",
     "SCADA UPS 48hr | RCP DC/UPS x2 | RTU UPS x4 | DC 125V | EDG x2"),
    ("f6_tpc", "TPC Extension + SPS Curtailment",
     "TPC PCC Bay x2 | SPS Curtailment Controller | Revenue Meter x3"),
]


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('CoverTitle', fontSize=28, leading=34,
        textColor=white, alignment=1, spaceAfter=20, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle('CoverSub', fontSize=14, leading=18,
        textColor=HexColor("#93c5fd"), alignment=1, spaceAfter=8))
    styles.add(ParagraphStyle('CoverInfo', fontSize=11, leading=14,
        textColor=HexColor("#94a3b8"), alignment=1, spaceAfter=4))
    styles.add(ParagraphStyle('ChTitle', fontSize=22, leading=28,
        textColor=NAVY, spaceAfter=12, spaceBefore=20, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle('SecTitle', fontSize=14, leading=18,
        textColor=SKY, spaceAfter=8, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle('Body2', fontSize=10, leading=14, spaceAfter=6))
    return styles


def draw_cover_bg(canvas, doc):
    w, h = landscape(A3)
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(SKY)
    canvas.rect(0, 0, 8*mm, h, fill=1, stroke=0)
    canvas.rect(0, 0, w, 3*mm, fill=1, stroke=0)
    canvas.restoreState()


def draw_header(canvas, doc):
    w, h = landscape(A3)
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 12*mm, w, 12*mm, fill=1, stroke=0)
    canvas.setFillColor(SKY)
    canvas.rect(0, h - 12*mm, 4*mm, 12*mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(10*mm, h - 8.5*mm,
        "F6 ONS — OT System Architecture  |  Rev 1.0  |  2026-03-23")
    canvas.drawRightString(w - 10*mm, h - 8.5*mm, f"Page {doc.page}")
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.5)
    canvas.line(10*mm, 8*mm, w - 10*mm, 8*mm)
    canvas.setFillColor(GRAY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(10*mm, 4*mm, "Confidential — Formosa 6 Offshore Wind Farm")
    canvas.restoreState()


def gen_text_pdf():
    """Generate text-only pages (cover + TOC + chapter headers + appendices)."""
    path = TMP_DIR / "_text.pdf"
    styles = build_styles()
    doc = SimpleDocTemplate(str(path), pagesize=landscape(A3),
        leftMargin=15*mm, rightMargin=15*mm, topMargin=18*mm, bottomMargin=12*mm)

    elements = []

    # Cover
    elements.append(Spacer(1, 60*mm))
    elements.append(Paragraph("Formosa 6 Offshore Wind Farm", styles['CoverTitle']))
    elements.append(Spacer(1, 5*mm))
    elements.append(Paragraph("ONS OT System Architecture", styles['CoverTitle']))
    elements.append(Spacer(1, 15*mm))
    elements.append(Paragraph("Technical Proposal — Architecture Diagrams", styles['CoverSub']))
    elements.append(Spacer(1, 8*mm))
    elements.append(Paragraph("Onshore Substation (ONS) + Onshore Switching Station (OnSWST)", styles['CoverSub']))
    elements.append(Spacer(1, 20*mm))
    for line in ["Document No: F6-ICP-ONS-ARCH-001", "Revision: 1.0", "Date: 2026-03-23",
                  "Classification: Confidential", "",
                  "Standards: IEC 62443 / IEC 61850 / IEC 62439-3 PRP / Purdue Model",
                  "", "CBOM Reference: F6 CBOM v1.1"]:
        elements.append(Paragraph(line, styles['CoverInfo']))
    elements.append(PageBreak())

    # TOC
    elements.append(Paragraph("Table of Contents", styles['ChTitle']))
    elements.append(Spacer(1, 10*mm))
    toc = [["Ch", "Title", "Key Equipment"]]
    for i, (_, title, summary) in enumerate(CHAPTERS):
        toc.append([str(i+1), title, summary[:70] + "..."])
    toc.append(["A", "Applicable Standards", "IEC 62443, IEC 61850, DNP3, PRP..."])
    toc.append(["B", "CBOM Cross-Reference", "CBOM v1.1 item mapping"])
    toc.append(["C", "Revision History", "Document changelog"])
    t = Table(toc, colWidths=[40, 200, 400])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t)
    elements.append(PageBreak())

    # Legend page (shared, before all chapters)
    elements.append(Paragraph("Legend — Diagram Symbols", styles['ChTitle']))
    elements.append(Spacer(1, 8*mm))

    # Components table
    elements.append(Paragraph("Equipment Symbols", styles['SecTitle']))
    comp_data = [["Symbol", "Description"],
        ["Rectangle (Navy border)", "SCADA Server / Historian"],
        ["Rectangle (Sky Blue border)", "HMI / NTP Server"],
        ["Diamond (Red border)", "Firewall"],
        ["Hexagon (Sky Blue border)", "Switch PRP"],
        ["Hexagon (Amber border)", "Protocol Gateway"],
        ["Rectangle (Amber border)", "BCU / RTU / IED"],
        ["Rectangle (Gray border)", "Field IED / Engineering WS"],
        ["Hexagon (Navy border)", "DANP (PRP Dual-NIC Interface)"],
        ["Rectangle (Gray dashed)", "External System"],
    ]
    t2 = Table(comp_data, colWidths=[180, 300])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(t2)
    elements.append(Spacer(1, 8*mm))

    # Connections table
    elements.append(Paragraph("Connection Types", styles['SecTitle']))
    conn_data = [["Line Style", "Protocol"],
        ["Solid Navy thick", "IEC 61850 GOOSE Fiber"],
        ["Solid Sky Blue", "PRP LAN-A / OPC-UA A"],
        ["Dashed Navy", "PRP LAN-B / OPC-UA B"],
        ["Dashed Gray thin", "RS-485 / IT Ethernet"],
        ["Dashed Amber", "VPN / RF Wireless"],
        ["Solid Sky Blue thin", "Modbus TCP"],
        ["Solid Navy", "IRIG-B / IEEE 1588 PTP"],
    ]
    t3 = Table(conn_data, colWidths=[180, 300])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(t3)
    elements.append(Spacer(1, 8*mm))

    elements.append(Paragraph(
        "Note: All architecture diagrams follow the Purdue Model / ISA-95 layered structure "
        "(Level 4: External → DMZ → Level 3: SCADA → Level 2: Network → Level 1: Bay Control → Level 0: Field Devices).",
        styles['Body2']))
    elements.append(PageBreak())

    # Chapter title pages (one per chapter)
    for i, (_, title, summary) in enumerate(CHAPTERS):
        elements.append(Paragraph(f"Chapter {i+1}: {title}", styles['ChTitle']))
        elements.append(Spacer(1, 5*mm))
        elements.append(Paragraph("Equipment Summary", styles['SecTitle']))
        elements.append(Paragraph(summary, styles['Body2']))
        elements.append(Spacer(1, 5*mm))
        elements.append(Paragraph("See architecture diagram on next page.", styles['Body2']))
        elements.append(PageBreak())

    # Appendices
    elements.append(Paragraph("Appendix A: Applicable Standards", styles['ChTitle']))
    elements.append(Spacer(1, 5*mm))
    std_data = [["Standard", "Scope"],
        ["IEC 61850", "Communication networks for power utility automation"],
        ["IEC 62443", "Industrial automation and control systems security"],
        ["IEC 62439-3", "Parallel Redundancy Protocol (PRP)"],
        ["DNP3", "Distributed Network Protocol (TPC dispatch)"],
        ["IEEE 1588 PTP", "Precision Time Protocol"],
        ["ISO/IEC 27001", "Information security management"],
    ]
    t = Table(std_data, colWidths=[120, 490])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t)
    elements.append(PageBreak())

    elements.append(Paragraph("Appendix B: CBOM v1.1 Cross-Reference", styles['ChTitle']))
    elements.append(Spacer(1, 5*mm))
    cbom = [["Diagram", "CBOM Groups", "Key Items"],
        ["DWG-PROT", "1.1, 1.1a, 1.1b", "H101-H107, H14a/b, H_RCPUPS"],
        ["DWG-SCADA", "1.2, 1.3, 1.4", "S201-S217, H_SRV1, H301, H401-H408"],
        ["DWG-CCTV", "1.7", "H601-H603, S601"],
        ["DWG-ACS", "1.8", "H701-H705, S701"],
        ["DWG-TEL", "1.5, 1.6, 1.9", "H450-H453, H500-H502, H801-H805"],
        ["DWG-PWR", "1.1b, 1.2 HW", "H_UPS1, H_RCPUPS, H_RTUUPS"],
        ["DWG-TPC", "1.10, 1.11", "H901-H903, H1101-H1102"],
    ]
    t = Table(cbom, colWidths=[100, 120, 390])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t)
    elements.append(PageBreak())

    elements.append(Paragraph("Appendix C: Revision History", styles['ChTitle']))
    elements.append(Spacer(1, 5*mm))
    rev = [["Rev", "Date", "Description"],
        ["1.0", "2026-03-23", "Initial release — 8 architecture diagrams aligned with CBOM v1.1"],
    ]
    t = Table(rev, colWidths=[60, 100, 450])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY), ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t)

    doc.build(elements, onFirstPage=draw_cover_bg, onLaterPages=draw_header)
    print(f"[OK] Text PDF: {path}")
    return path


def gen_diagram_pdfs():
    """Use d2 CLI to generate vector PDF for each diagram (clean, no overflow)."""
    paths = []
    for name, title, _ in CHAPTERS:
        d2_file = BASE_DIR / f"{name}.d2"
        pdf_file = TMP_DIR / f"{name}.pdf"
        if d2_file.exists():
            print(f"[INFO] Rendering {name}.d2 → PDF (d2 CLI)...")
            result = subprocess.run(
                ["d2", str(d2_file), str(pdf_file)],
                capture_output=True, timeout=60
            )
            if pdf_file.exists() and pdf_file.stat().st_size > 0:
                print(f"[OK] {pdf_file.name} ({pdf_file.stat().st_size:,} bytes)")
                paths.append(pdf_file)
            else:
                print(f"[WARN] Failed: {name}")
        else:
            print(f"[SKIP] {d2_file} not found")
    return paths


def create_title_overlay(title, page_width, page_height, tmp_dir):
    """Create a PDF overlay with Title Bar + Legend for a diagram page."""
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib.colors import Color
    from io import BytesIO

    buf = BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=(page_width, page_height))

    # ── Title Bar (top) ──
    bar_h = 36
    c.setFillColor(NAVY)
    c.rect(0, page_height - bar_h, page_width, bar_h, fill=1, stroke=0)
    c.setFillColor(SKY)
    c.rect(0, page_height - bar_h, 4, bar_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(12, page_height - bar_h + 14, title)
    c.setFont("Helvetica", 7)
    c.drawRightString(page_width - 10, page_height - bar_h + 14,
                      "F6 ONS OT Architecture  |  Rev 1.0  |  2026-03-23")

    # Legend 不疊加在架構圖上——改為獨立頁面
    c.save()
    buf.seek(0)
    return buf

    # ── 以下 Legend 代碼不再執行（保留作為參考）──
    LEGEND_COMPONENTS = [
        ("rect",    "SCADA / Historian",  "#0C3467", "#e0f4fb"),
        ("rect",    "HMI / NTP Server",   "#008EC3", "#e0f4fb"),
        ("diamond", "Firewall",           "#c0392b", "#fdecea"),
        ("hex",     "Switch PRP",         "#008EC3", "#e0f4fb"),
        ("hex",     "Protocol Gateway",   "#F5A623", "#fff8e1"),
        ("rect",    "BCU / RTU / IED",    "#F5A623", "#fff8e1"),
        ("rect",    "Field IED / ENG WS", "#9B9B9B", "#f5f5f5"),
        ("hex",     "DANP (PRP Dual-NIC)","#0C3467", "#e0f4fb"),
        ("rect",    "External System",    "#9B9B9B", "#ffffff"),
    ]
    LEGEND_CONNECTIONS = [
        ("IEC 61850 GOOSE Fiber",  "#0C3467", False, 2),
        ("PRP LAN-A / OPC-UA A",   "#008EC3", False, 2),
        ("PRP LAN-B / OPC-UA B",   "#0C3467", True,  2),
        ("RS-485 / IT Ethernet",   "#9B9B9B", True,  1),
        ("VPN / RF Wireless",      "#F5A623", True,  1),
        ("Modbus TCP",             "#008EC3", False, 1),
        ("IRIG-B / IEEE 1588",     "#0C3467", False, 2),
    ]

    rows = max(len(LEGEND_COMPONENTS), len(LEGEND_CONNECTIONS))
    row_h = 16
    header_h = 18
    leg_w = 340
    leg_h = header_h + rows * row_h + 10
    col_sep = 170  # left column width

    # Position: right side, below Title Bar
    lx = page_width - leg_w - 15
    ly = page_height - bar_h - leg_h - 10

    # Background
    c.setFillColor(Color(1, 1, 1, 0.95))
    c.setStrokeColor(NAVY)
    c.setLineWidth(1)
    c.roundRect(lx, ly, leg_w, leg_h, 4, fill=1, stroke=1)

    # Header bar
    c.setFillColor(NAVY)
    c.roundRect(lx, ly + leg_h - header_h, leg_w, header_h, 4, fill=1, stroke=0)
    c.rect(lx, ly + leg_h - header_h, leg_w, header_h // 2, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(lx + leg_w / 2, ly + leg_h - header_h + 5, "Legend")

    # Column separator
    c.setStrokeColor(HexColor("#cccccc"))
    c.setLineWidth(0.5)
    c.line(lx + col_sep, ly + 5, lx + col_sep, ly + leg_h - header_h - 2)

    # Left column: Components
    for i, (shape, label, stroke_c, fill_c) in enumerate(LEGEND_COMPONENTS):
        cx = lx + 10
        cy = ly + leg_h - header_h - 12 - i * row_h
        sw = 14
        sh = 10

        c.setStrokeColor(HexColor(stroke_c))
        c.setFillColor(HexColor(fill_c))
        c.setLineWidth(1)

        if shape == "diamond":
            p = c.beginPath()
            p.moveTo(cx + sw/2, cy + sh)
            p.lineTo(cx + sw, cy + sh/2)
            p.lineTo(cx + sw/2, cy)
            p.lineTo(cx, cy + sh/2)
            p.close()
            c.drawPath(p, fill=1, stroke=1)
        elif shape == "hex":
            p = c.beginPath()
            p.moveTo(cx + 3, cy)
            p.lineTo(cx + sw - 3, cy)
            p.lineTo(cx + sw, cy + sh/2)
            p.lineTo(cx + sw - 3, cy + sh)
            p.lineTo(cx + 3, cy + sh)
            p.lineTo(cx, cy + sh/2)
            p.close()
            c.drawPath(p, fill=1, stroke=1)
        else:
            c.rect(cx, cy, sw, sh, fill=1, stroke=1)

        c.setFillColor(HexColor("#1a1a1a"))
        c.setFont("Helvetica", 7)
        c.drawString(cx + sw + 4, cy + 2, label)

    # Right column: Connections
    for i, (label, color, dashed, width) in enumerate(LEGEND_CONNECTIONS):
        cx = lx + col_sep + 8
        cy = ly + leg_h - header_h - 8 - i * row_h

        c.setStrokeColor(HexColor(color))
        c.setLineWidth(width * 0.7)
        if dashed:
            c.setDash(4, 2)
        else:
            c.setDash()
        c.line(cx, cy, cx + 18, cy)
        c.setDash()  # reset

        c.setFillColor(HexColor("#1a1a1a"))
        c.setFont("Helvetica", 7)
        c.drawString(cx + 22, cy - 3, label)

    c.save()
    buf.seek(0)
    return buf


def merge_pdfs(text_pdf, diagram_pdfs, output_path):
    """Merge text pages + diagram PDFs with Title Bar overlay."""
    writer = PdfWriter()

    text_reader = PdfReader(str(text_pdf))
    total_text = len(text_reader.pages)
    print(f"[INFO] Text PDF: {total_text} pages")

    # Cover
    writer.add_page(text_reader.pages[0])
    # TOC
    writer.add_page(text_reader.pages[1])

    # Interleave chapter pages with diagrams
    for i, diagram_pdf in enumerate(diagram_pdfs):
        # Chapter title page
        text_page_idx = 2 + i
        if text_page_idx < total_text:
            writer.add_page(text_reader.pages[text_page_idx])

        # Diagram page(s) with Title Bar overlay
        title = CHAPTERS[i][1] if i < len(CHAPTERS) else ""
        diag_reader = PdfReader(str(diagram_pdf))
        for page in diag_reader.pages:
            # Create overlay matching page size
            pw = float(page.mediabox.width)
            ph = float(page.mediabox.height)
            overlay_buf = create_title_overlay(
                f"Chapter {i+1}: {title}", pw, ph, TMP_DIR)
            overlay_reader = PdfReader(overlay_buf)
            page.merge_page(overlay_reader.pages[0])
            writer.add_page(page)

    # Appendix pages
    appendix_start = 2 + len(diagram_pdfs)
    for i in range(appendix_start, total_text):
        writer.add_page(text_reader.pages[i])

    with open(str(output_path), 'wb') as f:
        writer.write(f)

    size = output_path.stat().st_size
    pages = len(writer.pages)
    print(f"[OK] Final PDF: {output_path} ({size:,} bytes, {pages} pages)")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    output_path = OUTPUT_DIR / "F6_ONS_OT_Architecture_v1.0.pdf"

    print("=" * 60)
    print("  F6 ONS OT System Architecture — PDF Generator")
    print("=" * 60)

    # Step 1: Generate text pages
    print("\n--- Step 1: Text Pages ---")
    text_pdf = gen_text_pdf()

    # Step 2: Generate diagram PDFs
    print("\n--- Step 2: Diagram PDFs ---")
    diagram_pdfs = gen_diagram_pdfs()

    # Step 3: Merge
    print("\n--- Step 3: Merge ---")
    merge_pdfs(text_pdf, diagram_pdfs, output_path)

    # Cleanup
    import shutil
    shutil.rmtree(str(TMP_DIR), ignore_errors=True)

    print("\n" + "=" * 60)
    print(f"  Output: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
