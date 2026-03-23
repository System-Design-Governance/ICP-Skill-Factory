#!/usr/bin/env python3
"""
large-doc-search ingest.py
==========================
Parse a large PDF into a structured knowledge base:
  - Detect chapter boundaries (bookmarks → TOC → heading heuristics → fixed-page fallback)
  - Split into per-chapter Markdown files
  - Extract tables into separate Markdown files
  - Generate extractive summaries and keywords per chapter
  - Produce index.json for lightweight querying

Usage:
    python3 ingest.py <input.pdf> --output <kb_directory> [options]
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from math import log
from pathlib import Path

INGEST_VERSION = "1.0.0"

# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------

def _check_dependencies():
    """Verify required packages are installed and give helpful messages."""
    missing = []
    try:
        import pypdf  # noqa: F401
    except ImportError:
        missing.append("pypdf")
    try:
        import pdfplumber  # noqa: F401
    except ImportError:
        missing.append("pdfplumber")
    if missing:
        print(f"ERROR: Missing required packages: {', '.join(missing)}")
        print(f"Install with:  pip install {' '.join(missing)} --break-system-packages")
        sys.exit(1)

_check_dependencies()

import pypdf
import pdfplumber

# Optional: jieba for Chinese keyword extraction
try:
    import jieba
    HAS_JIEBA = True
except ImportError:
    HAS_JIEBA = False

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 40) -> str:
    """Convert a title string into a filesystem-safe slug."""
    text = unicodedata.normalize("NFKD", text)
    # Keep alphanumeric, CJK characters, hyphens, underscores
    text = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", text)
    text = re.sub(r"[\s_]+", "_", text).strip("_")
    return text[:max_len].rstrip("_").lower()


def detect_language(text: str) -> str:
    """Simple heuristic: if >20% of characters are CJK, treat as Chinese."""
    if not text:
        return "en"
    cjk_count = sum(1 for c in text if "\u4e00" <= c <= "\u9fff")
    ratio = cjk_count / max(len(text), 1)
    return "zh" if ratio > 0.2 else "en"


# ---------------------------------------------------------------------------
# Chapter detection strategies
# ---------------------------------------------------------------------------

def detect_via_bookmarks(reader: pypdf.PdfReader) -> list[dict] | None:
    """Strategy 1: Use PDF bookmarks / outlines (most reliable)."""
    try:
        outlines = reader.outline
        if not outlines:
            return None
    except Exception:
        return None

    chapters = []
    _flatten_outlines(reader, outlines, chapters, level=0)

    if len(chapters) < 2:
        return None

    # Only keep top-level (level 0) entries, or level 0+1 if few top-level
    top_level = [c for c in chapters if c["level"] == 0]
    if len(top_level) < 2:
        # Use level 0 and 1
        top_level = [c for c in chapters if c["level"] <= 1]

    if len(top_level) < 2:
        return None

    # Filter out entries with None start_page
    top_level = [c for c in top_level if c["start_page"] is not None]
    if len(top_level) < 2:
        return None

    # Resolve page ranges
    total_pages = len(reader.pages)
    resolved = []
    for i, ch in enumerate(top_level):
        start = ch["start_page"]
        if i + 1 < len(top_level):
            next_start = top_level[i + 1]["start_page"]
            end = next_start - 1 if next_start is not None else total_pages - 1
        else:
            end = total_pages - 1
        if end < start:
            end = start
        resolved.append({
            "title": ch["title"],
            "start_page": start,  # 0-indexed
            "end_page": end,
        })
    return resolved


def _flatten_outlines(reader, outlines, result, level):
    """Recursively flatten PDF outline tree."""
    for item in outlines:
        if isinstance(item, list):
            _flatten_outlines(reader, item, result, level + 1)
        else:
            try:
                page_num = reader.get_destination_page_number(item)
                title = item.title.strip() if item.title else f"Section {len(result)+1}"
                result.append({
                    "title": title,
                    "start_page": page_num,
                    "level": level,
                })
            except Exception:
                continue


def detect_via_toc(reader: pypdf.PdfReader, plumber) -> list[dict] | None:
    """Strategy 2: Find and parse a Table of Contents page."""
    total_pages = len(reader.pages)
    # Search first 20 pages (or 5% of document) for TOC
    search_range = min(20, max(5, total_pages // 20), total_pages)

    toc_patterns = [
        r"(?i)table\s+of\s+contents",
        r"(?i)contents",
        r"目\s*錄",
        r"目\s*次",
    ]

    toc_entries = []

    for page_idx in range(search_range):
        page = plumber.pages[page_idx]
        text = page.extract_text() or ""

        # Check if this page is a TOC page
        is_toc = any(re.search(pat, text) for pat in toc_patterns)
        if not is_toc:
            continue

        # Parse TOC entries: "Chapter Title ....... 42" or "1.2 Section Name 42"
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            # Match patterns like: "1 Introduction .... 5" or "Chapter 1 Overview 12"
            m = re.match(
                r"^((?:\d+(?:\.\d+)*\.?\s+|Chapter\s+\d+\s+)?.+?)"  # title part
                r"[\s.·…_]{2,}"  # dots / spaces separator
                r"(\d+)\s*$",  # page number
                line,
            )
            if m:
                title = m.group(1).strip()
                page_num = int(m.group(2)) - 1  # Convert to 0-indexed
                # Skip if page number is unreasonable
                if 0 <= page_num < total_pages and title:
                    # Skip the TOC header itself
                    if any(re.match(pat, title) for pat in toc_patterns):
                        continue
                    toc_entries.append({
                        "title": title,
                        "start_page": page_num,
                    })

    if len(toc_entries) < 2:
        return None

    # De-duplicate and sort
    toc_entries.sort(key=lambda x: x["start_page"])
    seen = set()
    unique = []
    for e in toc_entries:
        key = (e["title"], e["start_page"])
        if key not in seen:
            seen.add(key)
            unique.append(e)

    # Resolve page ranges
    resolved = []
    for i, ch in enumerate(unique):
        start = ch["start_page"]
        end = unique[i + 1]["start_page"] - 1 if i + 1 < len(unique) else total_pages - 1
        if end < start:
            end = start
        resolved.append({
            "title": ch["title"],
            "start_page": start,
            "end_page": end,
        })
    return resolved


def detect_via_headings(plumber) -> list[dict] | None:
    """Strategy 3: Heuristic based on font size and numbering patterns.

    Scans through the PDF looking for text that appears to be chapter headings
    based on: larger font size, numbered format (e.g., '1 Introduction',
    '2.1 Setup'), and position near the top of the page.
    """
    total_pages = len(plumber.pages)
    if total_pages < 3:
        return None

    # Sample pages to determine typical body font size
    sample_sizes = []
    sample_range = min(30, total_pages)
    for i in range(0, sample_range, max(1, sample_range // 10)):
        page = plumber.pages[i]
        chars = page.chars or []
        for c in chars:
            if c.get("size"):
                sample_sizes.append(round(float(c["size"]), 1))

    if not sample_sizes:
        return None

    # Most common size is likely the body text
    size_counter = Counter(sample_sizes)
    body_size = size_counter.most_common(1)[0][0]
    # Heading threshold: at least 1.3x body size
    heading_threshold = body_size * 1.3

    # Numbered heading pattern
    heading_pattern = re.compile(
        r"^(\d+(?:\.\d+)*\.?\s+\S)"  # "1 ", "1.2 ", "2.3.1 "
    )

    candidates = []
    for page_idx in range(total_pages):
        page = plumber.pages[page_idx]
        chars = page.chars or []
        if not chars:
            continue

        # Group chars into lines by y-position (top of page)
        lines_by_top = {}
        for c in chars:
            top = round(float(c.get("top", 0)), 0)
            lines_by_top.setdefault(top, []).append(c)

        for top_pos in sorted(lines_by_top.keys()):
            line_chars = sorted(lines_by_top[top_pos], key=lambda c: float(c.get("x0", 0)))
            if not line_chars:
                continue

            # Check font size
            avg_size = sum(float(c.get("size", 0)) for c in line_chars) / len(line_chars)
            if avg_size < heading_threshold:
                continue

            # Reconstruct text
            text = "".join(c.get("text", "") for c in line_chars).strip()
            if not text or len(text) < 3:
                continue

            # Check if it matches heading pattern
            if heading_pattern.match(text):
                candidates.append({
                    "title": text,
                    "start_page": page_idx,
                    "font_size": avg_size,
                })

    if len(candidates) < 2:
        return None

    # De-duplicate: if same page has multiple candidates, keep the largest font
    by_page = {}
    for c in candidates:
        p = c["start_page"]
        if p not in by_page or c["font_size"] > by_page[p]["font_size"]:
            by_page[p] = c

    sorted_candidates = sorted(by_page.values(), key=lambda x: x["start_page"])

    if len(sorted_candidates) < 2:
        return None

    # Resolve page ranges
    resolved = []
    for i, ch in enumerate(sorted_candidates):
        start = ch["start_page"]
        end = sorted_candidates[i + 1]["start_page"] - 1 if i + 1 < len(sorted_candidates) else total_pages - 1
        if end < start:
            end = start
        resolved.append({
            "title": ch["title"],
            "start_page": start,
            "end_page": end,
        })
    return resolved


def detect_fixed_pages(total_pages: int, pages_per_chunk: int = 30) -> list[dict]:
    """Strategy 4 (fallback): Split every N pages."""
    chapters = []
    for start in range(0, total_pages, pages_per_chunk):
        end = min(start + pages_per_chunk - 1, total_pages - 1)
        chapters.append({
            "title": f"Pages {start+1}-{end+1}",
            "start_page": start,
            "end_page": end,
        })
    return chapters


def detect_chapters(reader: pypdf.PdfReader, plumber, method: str = "auto") -> tuple[list[dict], str]:
    """Run chapter detection with the specified method.

    Returns (chapters, method_used) where method_used is which strategy succeeded.
    """
    total_pages = len(reader.pages)

    if method == "bookmark":
        result = detect_via_bookmarks(reader)
        if result:
            return result, "bookmark"
        print("WARNING: No bookmarks found. Falling back to fixed-page split.")
        return detect_fixed_pages(total_pages), "fixed"

    if method == "toc":
        result = detect_via_toc(reader, plumber)
        if result:
            return result, "toc"
        print("WARNING: No TOC found. Falling back to fixed-page split.")
        return detect_fixed_pages(total_pages), "fixed"

    if method == "heading":
        result = detect_via_headings(plumber)
        if result:
            return result, "heading"
        print("WARNING: No headings detected. Falling back to fixed-page split.")
        return detect_fixed_pages(total_pages), "fixed"

    # Auto: try all strategies in order
    for strategy_fn, name in [
        (lambda: detect_via_bookmarks(reader), "bookmark"),
        (lambda: detect_via_toc(reader, plumber), "toc"),
        (lambda: detect_via_headings(plumber), "heading"),
    ]:
        result = strategy_fn()
        if result:
            return result, name

    print("WARNING: No chapter structure detected. Using fixed-page split (every 30 pages).")
    return detect_fixed_pages(total_pages), "fixed"


# ---------------------------------------------------------------------------
# Text and table extraction
# ---------------------------------------------------------------------------

def extract_text_range(plumber, start_page: int, end_page: int) -> str:
    """Extract text from a range of pages using pdfplumber."""
    parts = []
    for i in range(start_page, min(end_page + 1, len(plumber.pages))):
        page = plumber.pages[i]
        text = page.extract_text() or ""
        if text.strip():
            parts.append(f"<!-- Page {i+1} -->\n{text}")
    return "\n\n".join(parts)


def extract_tables_range(plumber, start_page: int, end_page: int) -> list[dict]:
    """Extract tables from a range of pages.

    Returns list of {"page": int, "data": list[list[str]], "header": list[str]}
    """
    tables = []
    for i in range(start_page, min(end_page + 1, len(plumber.pages))):
        page = plumber.pages[i]
        try:
            page_tables = page.extract_tables() or []
        except Exception:
            continue
        for tbl in page_tables:
            if not tbl or len(tbl) < 2:
                continue
            # First row is header
            header = [str(c or "").strip() for c in tbl[0]]
            data = []
            for row in tbl[1:]:
                data.append([str(c or "").strip() for c in row])
            tables.append({
                "page": i + 1,  # 1-indexed for display
                "header": header,
                "data": data,
            })
    return tables


def table_to_markdown(header: list[str], data: list[list[str]]) -> str:
    """Convert a table to Markdown format."""
    if not header:
        return ""

    # Ensure all rows have same column count
    ncols = len(header)
    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * ncols) + " |")
    for row in data:
        # Pad or truncate row
        padded = (row + [""] * ncols)[:ncols]
        lines.append("| " + " | ".join(padded) + " |")
    return "\n".join(lines)


def merge_adjacent_tables(tables: list[dict]) -> list[dict]:
    """Merge tables on consecutive pages with the same header structure."""
    if not tables:
        return []

    merged = [tables[0]]
    for tbl in tables[1:]:
        prev = merged[-1]
        # Same header structure and consecutive pages
        if prev["header"] == tbl["header"] and tbl["page"] - prev["page"] <= 1:
            prev["data"].extend(tbl["data"])
            prev["page_end"] = tbl["page"]
        else:
            merged.append(tbl)
    return merged


# ---------------------------------------------------------------------------
# Summarization and keyword extraction (no LLM required)
# ---------------------------------------------------------------------------

def extractive_summary(text: str, max_chars: int = 150) -> str:
    """Generate an extractive summary by picking the most representative sentences.

    Uses a simple approach: score sentences by how many 'important' words they
    contain (words that appear multiple times but aren't too common).
    """
    # Split into sentences
    sentences = re.split(r"(?<=[.!?。！？])\s+", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    if not sentences:
        # Fallback: just take the first N characters
        return text[:max_chars].strip()

    # Word frequency
    words = re.findall(r"\b\w{2,}\b", text.lower())
    freq = Counter(words)
    total = len(words) or 1

    # Score each sentence
    scored = []
    for sent in sentences:
        sent_words = re.findall(r"\b\w{2,}\b", sent.lower())
        if not sent_words:
            continue
        # Prefer words that appear 2-10 times (not too rare, not too common)
        score = sum(1 for w in sent_words if 2 <= freq[w] <= total * 0.1)
        scored.append((score / len(sent_words), sent))

    scored.sort(reverse=True)

    # Build summary from top sentences
    summary_parts = []
    char_count = 0
    for _, sent in scored:
        if char_count + len(sent) > max_chars:
            break
        summary_parts.append(sent)
        char_count += len(sent)

    if not summary_parts:
        return sentences[0][:max_chars]

    return " ".join(summary_parts)


def extract_keywords(text: str, lang: str = "auto", top_n: int = 10) -> list[str]:
    """Extract keywords using TF-IDF-like scoring + regex for technical terms."""
    if lang == "auto":
        lang = detect_language(text)

    keywords = set()

    # 1. Technical term patterns (always run)
    tech_patterns = [
        r"\b\d{1,2}[A-Z]{2}\d{2,3}\b",              # Model numbers: 7UT85, 7SA87
        r"\b[A-Z][-\w]*(?:>|>>)\b",                   # Parameters: I-DIFF>, I-DIFF>>
        r"\bIEC\s*\d{4,5}(?:-\d+)*\b",               # Standards: IEC 61850
        r"\bIEEE\s*(?:C\d+|Std\s*)?\d+(?:\.\d+)*\b", # IEEE standards
        r"\b[A-Z]{2,6}[-/]\d{2,}\b",                  # Product codes
        r"\b(?:CT|PT|VT|CB|GOOSE|SV|MMS)\b",         # Common power system abbreviations
    ]
    for pat in tech_patterns:
        for m in re.finditer(pat, text):
            keywords.add(m.group().strip())

    # 2. TF-IDF-like scoring for English words
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    # Common stopwords to exclude
    stopwords = {
        "the", "and", "for", "are", "was", "were", "been", "have", "has",
        "had", "not", "but", "with", "this", "that", "from", "they", "will",
        "can", "which", "their", "also", "than", "into", "when", "each",
        "other", "more", "some", "such", "only", "its", "about", "after",
        "between", "through", "these", "those", "should", "would", "could",
        "being", "over", "any", "then", "does", "did", "may", "must",
        "shall", "page", "chapter", "section", "figure", "table", "see",
    }
    filtered = [w for w in words if w not in stopwords and len(w) >= 3]
    freq = Counter(filtered)
    total = len(filtered) or 1

    # Score: prefer medium-frequency terms
    scored = []
    for word, count in freq.items():
        if count < 2:
            continue
        tf = count / total
        # Pseudo-IDF: penalize very common words
        idf = log(total / (count + 1))
        scored.append((tf * idf, word))

    scored.sort(reverse=True)
    for _, word in scored[:top_n]:
        keywords.add(word)

    # 3. Chinese keywords (if applicable)
    if lang == "zh" and HAS_JIEBA:
        # Extract CJK text
        cjk_text = re.sub(r"[^\u4e00-\u9fff\s]", " ", text)
        if cjk_text.strip():
            seg_words = jieba.cut(cjk_text)
            zh_freq = Counter(w for w in seg_words if len(w) >= 2)
            for word, count in zh_freq.most_common(top_n):
                if count >= 2:
                    keywords.add(word)

    return sorted(keywords)[:top_n * 2]  # Allow a bit more for mixed-language docs


# ---------------------------------------------------------------------------
# Chapter splitting (handle oversized chapters)
# ---------------------------------------------------------------------------

def split_oversized_chapter(chapter: dict, text: str, max_chars: int) -> list[dict]:
    """If a chapter's text exceeds max_chars, split it into sub-chapters."""
    if len(text) <= max_chars:
        return [chapter]

    total_pages = chapter["end_page"] - chapter["start_page"] + 1
    # Estimate number of splits needed
    n_splits = (len(text) // max_chars) + 1
    pages_per_split = max(1, total_pages // n_splits)

    sub_chapters = []
    for i in range(n_splits):
        start = chapter["start_page"] + i * pages_per_split
        end = min(chapter["start_page"] + (i + 1) * pages_per_split - 1, chapter["end_page"])
        if start > chapter["end_page"]:
            break
        suffix = chr(ord("a") + i) if n_splits > 1 else ""
        sub_chapters.append({
            "title": f"{chapter['title']} (Part {suffix.upper() or 'A'})" if n_splits > 1 else chapter["title"],
            "start_page": start,
            "end_page": end,
            "parent_chapter": chapter.get("title"),
        })

    return sub_chapters


# ---------------------------------------------------------------------------
# Main ingest pipeline
# ---------------------------------------------------------------------------

def ingest(pdf_path: str, output_dir: str, options: argparse.Namespace):
    """Main ingest pipeline."""
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)

    if not pdf_path.exists():
        print(f"ERROR: PDF file not found: {pdf_path}")
        sys.exit(1)

    # Create output directories
    chapters_dir = output_dir / "chapters"
    tables_dir = output_dir / "tables"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)

    print(f"Opening PDF: {pdf_path}")
    print(f"Output directory: {output_dir}")

    # Open PDF with both libraries
    password = getattr(options, "password", None)
    try:
        reader = pypdf.PdfReader(str(pdf_path), password=password)
    except pypdf.errors.FileNotDecryptedError:
        print("ERROR: PDF is encrypted. Use --password to provide the password.")
        sys.exit(1)

    plumber = pdfplumber.open(str(pdf_path), password=password)

    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    # Detect language from first few pages
    sample_text = ""
    for i in range(min(5, total_pages)):
        sample_text += (plumber.pages[i].extract_text() or "")
    lang = options.lang if options.lang != "auto" else detect_language(sample_text)
    print(f"Detected language: {lang}")

    # Detect chapters
    print(f"Detecting chapters (method={options.method})...")
    chapters, method_used = detect_chapters(reader, plumber, options.method)
    print(f"Method used: {method_used}")
    print(f"Chapters detected: {len(chapters)}")

    # Process each chapter
    index_chapters = []
    table_counter = 0

    for ch_idx, ch in enumerate(chapters):
        ch_id = f"ch{ch_idx+1:02d}"
        ch_slug = slugify(ch["title"])
        ch_filename = f"{ch_id}_{ch_slug}.md"

        print(f"  Processing {ch_id}: {ch['title']} (p.{ch['start_page']+1}-{ch['end_page']+1})")

        # Extract text
        text = extract_text_range(plumber, ch["start_page"], ch["end_page"])

        # Handle oversized chapters
        if len(text) > options.max_chapter_chars:
            sub_chapters = split_oversized_chapter(ch, text, options.max_chapter_chars)
            if len(sub_chapters) > 1:
                print(f"    → Chapter too large ({len(text)} chars), splitting into {len(sub_chapters)} parts")
                # Re-process as sub-chapters
                for sub_idx, sub_ch in enumerate(sub_chapters):
                    sub_id = f"ch{ch_idx+1:02d}{chr(ord('a')+sub_idx)}"
                    sub_slug = slugify(sub_ch["title"])
                    sub_filename = f"{sub_id}_{sub_slug}.md"
                    sub_text = extract_text_range(plumber, sub_ch["start_page"], sub_ch["end_page"])

                    # Save chapter markdown
                    ch_content = f"# {sub_ch['title']}\n\n"
                    ch_content += f"> Source: pages {sub_ch['start_page']+1}-{sub_ch['end_page']+1}\n\n"
                    ch_content += sub_text
                    (chapters_dir / sub_filename).write_text(ch_content, encoding="utf-8")

                    # Tables
                    related_tables = []
                    if options.extract_tables:
                        tables = extract_tables_range(plumber, sub_ch["start_page"], sub_ch["end_page"])
                        tables = merge_adjacent_tables(tables)
                        for tbl in tables:
                            table_counter += 1
                            tbl_filename = f"tbl{table_counter:02d}_{sub_slug}.md"
                            tbl_md = f"# Table from {sub_ch['title']} (p.{tbl['page']})\n\n"
                            tbl_md += table_to_markdown(tbl["header"], tbl["data"])
                            (tables_dir / tbl_filename).write_text(tbl_md, encoding="utf-8")
                            related_tables.append(f"tables/{tbl_filename}")

                    # Summary and keywords
                    summary = extractive_summary(sub_text) if options.summary_method == "extractive" else ""
                    kw = extract_keywords(sub_text, lang=lang)

                    index_chapters.append({
                        "id": sub_id,
                        "title": sub_ch["title"],
                        "page_range": [sub_ch["start_page"] + 1, sub_ch["end_page"] + 1],
                        "file": f"chapters/{sub_filename}",
                        "char_count": len(sub_text),
                        "summary": summary,
                        "keywords": kw,
                        "has_tables": len(related_tables) > 0,
                        "related_tables": related_tables,
                        "parent_chapter": sub_ch.get("parent_chapter"),
                    })
                continue  # Skip normal processing for this chapter

        # Normal-sized chapter: save markdown
        ch_content = f"# {ch['title']}\n\n"
        ch_content += f"> Source: pages {ch['start_page']+1}-{ch['end_page']+1}\n\n"
        ch_content += text
        (chapters_dir / ch_filename).write_text(ch_content, encoding="utf-8")

        # Extract tables
        related_tables = []
        if options.extract_tables:
            tables = extract_tables_range(plumber, ch["start_page"], ch["end_page"])
            tables = merge_adjacent_tables(tables)
            for tbl in tables:
                table_counter += 1
                tbl_filename = f"tbl{table_counter:02d}_{ch_slug}.md"
                tbl_md = f"# Table from {ch['title']} (p.{tbl['page']})\n\n"
                tbl_md += table_to_markdown(tbl["header"], tbl["data"])
                (tables_dir / tbl_filename).write_text(tbl_md, encoding="utf-8")
                related_tables.append(f"tables/{tbl_filename}")

        # Summary and keywords
        summary = extractive_summary(text) if options.summary_method == "extractive" else ""
        kw = extract_keywords(text, lang=lang)

        index_chapters.append({
            "id": ch_id,
            "title": ch["title"],
            "page_range": [ch["start_page"] + 1, ch["end_page"] + 1],
            "file": f"chapters/{ch_filename}",
            "char_count": len(text),
            "summary": summary,
            "keywords": kw,
            "has_tables": len(related_tables) > 0,
            "related_tables": related_tables,
        })

    # Write index.json
    kb_name = output_dir.name
    index_data = {
        "kb_name": kb_name,
        "source_file": pdf_path.name,
        "total_pages": total_pages,
        "total_chapters": len(index_chapters),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "ingest_version": INGEST_VERSION,
        "chapters": index_chapters,
    }
    index_path = output_dir / "index.json"
    index_path.write_text(json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Write metadata.json
    metadata = {
        "source_file": pdf_path.name,
        "source_path": str(pdf_path.absolute()),
        "total_pages": total_pages,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "ingest_version": INGEST_VERSION,
        "detection_method": method_used,
        "language": lang,
        "options": {
            "method": options.method,
            "max_chapter_chars": options.max_chapter_chars,
            "extract_tables": options.extract_tables,
            "summary_method": options.summary_method,
        },
    }
    (output_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    plumber.close()

    # Summary output
    print(f"\n{'='*60}")
    print(f"Ingest complete!")
    print(f"  Knowledge base: {output_dir}")
    print(f"  Chapters: {len(index_chapters)}")
    print(f"  Tables: {table_counter}")
    print(f"  Detection method: {method_used}")
    print(f"  Index file: {index_path}")
    print(f"  Index size: {index_path.stat().st_size / 1024:.1f} KB")
    print(f"{'='*60}")

    return index_data


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Ingest a large PDF into a structured knowledge base."
    )
    parser.add_argument("pdf", help="Path to the input PDF file")
    parser.add_argument("--output", "-o", required=True, help="Output directory for the knowledge base")
    parser.add_argument(
        "--method",
        choices=["auto", "bookmark", "toc", "heading", "fixed"],
        default="auto",
        help="Chapter detection method (default: auto)",
    )
    parser.add_argument("--lang", default="auto", help="Document language: auto, en, zh (default: auto)")
    parser.add_argument(
        "--max-chapter-chars",
        type=int,
        default=80000,
        help="Max characters per chapter before splitting (default: 80000)",
    )
    parser.add_argument(
        "--extract-tables",
        type=lambda x: x.lower() in ("true", "1", "yes"),
        default=True,
        help="Extract tables into separate files (default: true)",
    )
    parser.add_argument(
        "--summary-method",
        choices=["extractive", "none"],
        default="extractive",
        help="Summary method (default: extractive)",
    )
    parser.add_argument("--password", default=None, help="PDF password if encrypted")

    args = parser.parse_args()
    ingest(args.pdf, args.output, args)


if __name__ == "__main__":
    main()
