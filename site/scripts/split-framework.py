#!/usr/bin/env python3
"""Generate site/framework/*.qmd from docs/SAF Framework.md.

The markdown file is the single source of truth for the Framework chapters.
Quarto runs this as a project pre-render step (see _quarto.yml); the generated
pages are git-ignored. framework/index.qmd is hand-written and left alone.
"""
import re
import sys
import unicodedata
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
SOURCE = SITE.parent / "docs" / "SAF Framework.md"
OUT_DIR = SITE / "framework"

# page -> (title, start pattern). A page runs until the start of the next one.
# Summary headings in Business Architecture use "VS-NN.0 — Name" (em dash);
# the per-stream chapters use "VS-NN.0 Name", which is what splits the vs pages.
PAGES = [
    ("introduction", "Introduction and Scope", r"^# Preface\s*$"),
    ("motivation", "Motivation", r"^# Motivation\s*$"),
    ("strategy", "Strategy", r"^# Strategy\s*$"),
    ("business-architecture", "Business Architecture", r"^# Business Architecture\s*$"),
    ("vs-01", "VS-01 Data Acquisition and Ingestion", r"^## VS-01\.0 (?!—)"),
    ("vs-02", "VS-02 Data Standardization and Integration", r"^## VS-02\.0 (?!—)"),
    ("vs-03", "VS-03 Data Editing and Enrichment", r"^## VS-03\.0 (?!—)"),
    ("vs-04", "VS-04 Estimation, Analysis, and Statistical Modeling", r"^## VS-04\.0 (?!—)"),
    ("vs-05", "VS-05 Statistical Product Composition", r"^## VS-05\.0 (?!—)"),
    ("vs-06", "VS-06 Dissemination and Service Delivery", r"^## VS-06\.0 (?!—)"),
    ("vs-07", "VS-07 Governance and Compliance", r"^## VS-07\.0 (?!—)"),
    ("vs-08", "VS-08 Innovation and Methodological Development", r"^## VS-08\.0 (?!—)"),
    ("vs-09", "VS-09 Infrastructure and Platform Enablement", r"^## VS-09\.0 (?!—)"),
    ("vs-10", "VS-10 Customer and Stakeholder Engagement", r"^## VS-10\.0 (?!—)"),
]

HEADER = "<!-- GENERATED from docs/SAF Framework.md by scripts/split-framework.py - do not edit -->"
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{#([^}\s]+)[^}]*\})?\s*$")
ANCHOR_LINK = re.compile(r"\]\(#([^)\s]+)\)")


def slugify(text):
    """Approximate Pandoc's auto_identifiers for a heading."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_]", "", text)
    text = unicodedata.normalize("NFKC", text).lower()
    text = re.sub(r"[^\w\s.\-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text.lstrip("0123456789.-_") or "section"


def headings(lines):
    """Yield (index, line) for markdown headings outside code fences."""
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and HEADING.match(line):
            yield i, line


def page_anchors(lines):
    anchors = set()
    for _, line in headings(lines):
        m = HEADING.match(line)
        anchors.add(m.group(4) or slugify(m.group(2)))
    return anchors


def find_starts(lines):
    starts = []
    cursor = 0
    for name, _, pattern in PAGES:
        rx = re.compile(pattern)
        idx = next((i for i in range(cursor, len(lines)) if rx.match(lines[i])), None)
        if idx is None:
            sys.exit(f"split-framework: no heading matching {pattern!r} for page '{name}' "
                     f"in {SOURCE.name}")
        starts.append(idx)
        cursor = idx + 1
    return starts


def main():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    starts = find_starts(lines)
    ends = starts[1:] + [len(lines)]
    bodies = {name: lines[s:e] for (name, _, _), s, e in zip(PAGES, starts, ends)}
    anchors = {name: page_anchors(body) for name, body in bodies.items()}

    problems = []
    for name, title, _ in PAGES:
        out = []
        in_fence = False
        for line in bodies[name]:
            if FENCE.match(line):
                in_fence = not in_fence
            if not in_fence:
                line = line.replace("](images/", "](../images/")

                def relink(m, name=name):
                    target = m.group(1)
                    if target in anchors[name]:
                        return m.group(0)
                    owners = [p for p, a in anchors.items() if target in a]
                    if len(owners) == 1:
                        return f"]({owners[0]}.qmd#{target})"
                    problems.append(f"{name}: link to #{target} has "
                                    f"{'no' if not owners else 'several'} target page")
                    return m.group(0)

                line = ANCHOR_LINK.sub(relink, line)
            out.append(line)
        text = f'---\ntitle: "{title}"\n---\n{HEADER}\n\n' + "\n".join(out).rstrip() + "\n"
        (OUT_DIR / f"{name}.qmd").write_text(text, encoding="utf-8")

    if problems:
        sys.exit("split-framework: unresolved internal links:\n  " + "\n  ".join(problems))
    print(f"split-framework: wrote {len(PAGES)} pages to {OUT_DIR.relative_to(SITE.parent)}")


if __name__ == "__main__":
    main()
