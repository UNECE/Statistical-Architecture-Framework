#!/usr/bin/env python3
"""Generate site/framework/*.qmd from docs/SAF Framework.md.

The markdown file is the single source of truth for the Framework chapters.
Quarto runs this as a project pre-render step (see _quarto.yml); the generated
pages are git-ignored. framework/index.qmd is hand-written and left alone; it
includes framework/_document-info.md, which this script builds from the version
information above "# Preface". It also copies docs/images/ to site/images/
(git-ignored), so images referenced as images/... in the source reach the site.
"""
import re
import shutil
import sys
import unicodedata
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
SOURCE = SITE.parent / "docs" / "SAF Framework.md"
OUT_DIR = SITE / "framework"
IMAGES_SRC = SOURCE.parent / "images"
IMAGES_OUT = SITE / "images"

# page -> (title, start pattern). A page runs until the start of the next one.
# The value stream chapters are level-3 headings "### VS-NN Name", grouped under
# "## Primary value streams" and "## Supporting value streams" in the chapter
# "# Statistical Data Value Chain".
PAGES = [
    ("introduction", "Introduction and Scope", r"^# Preface\s*$"),
    ("motivation", "Motivation", r"^# Motivation\s*$"),
    ("strategy", "Strategy", r"^# Strategy\s*$"),
    ("business-architecture", "Business Architecture", r"^# Business Architecture\s*$"),
    ("steady-states", "Steady-State Architecture", r"^# Steady-State Architecture\s*$"),
    ("value-chain", "Statistical Data Value Chain", r"^# Statistical Data Value Chain\s*$"),
    ("vs-01", "VS-01 Data Acquisition and Ingestion", r"^### VS-01 "),
    ("vs-02", "VS-02 Data Standardization and Integration", r"^### VS-02 "),
    ("vs-03", "VS-03 Data Editing and Enrichment", r"^### VS-03 "),
    ("vs-04", "VS-04 Estimation, Analysis, and Statistical Modeling", r"^### VS-04 "),
    ("vs-05", "VS-05 Statistical Product Composition", r"^### VS-05 "),
    ("vs-06", "VS-06 Dissemination and Service Delivery", r"^### VS-06 "),
    ("vs-07", "VS-07 Governance and Compliance", r"^### VS-07 "),
    ("vs-08", "VS-08 Innovation and Methodological Development", r"^### VS-08 "),
    ("vs-09", "VS-09 Infrastructure and Platform Enablement", r"^### VS-09 "),
    ("vs-10", "VS-10 Customer and Stakeholder Engagement", r"^### VS-10 "),
    ("data-application-architecture", "Data and Application Architecture", r"^# Data and Application Architecture\s*$"),
    ("technology-architecture", "Technology Architecture", r"^# Technology Architecture\s*$"),
]

# Partial included by framework/index.qmd ("About this document" callout).
DOC_INFO = "_document-info.md"

HEADER ="<!-- GENERATED from docs/SAF Framework.md by scripts/split-framework.py - do not edit -->"
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{#([^}\s]+)[^}]*\})?\s*$")
ANCHOR_LINK = re.compile(r"\[([^\]]*)\]\(#([^)\s]+)\)")


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
    # The first line may be the "[]{#id}" span left in place of the title heading.
    anchors = set(re.findall(r"^\[\]\{#([^}\s]+)\}$", lines[0])) if lines else set()
    for _, line in headings(lines):
        m = HEADING.match(line)
        anchors.add(m.group(4) or slugify(m.group(2)))
    return anchors


def normalise(title, body):
    """Turn a slice of the source document into a stand-alone page body."""
    out = []
    # The page's opening heading usually repeats its title ("# Business
    # Architecture", "### VS-01 Data ..."). Quarto already shows the title,
    # so drop that heading and keep its anchor for links that point to it.
    m = HEADING.match(body[0]) if body else None
    if m and re.sub(r"\.0\b", "", m.group(2)) == title:
        out.append(f"[]{{#{m.group(4) or slugify(m.group(2))}}}")
        body = body[1:]
    else:
        body = list(body)

    # A heading at the very end of a page, with nothing below it, is the title of
    # the group of pages that follows ("## Supporting value streams" after VS-06).
    # The sidebar already shows those groups, so drop it.
    while True:
        while body and not body[-1].strip():
            body.pop()
        last = [i for i, _ in headings(body)][-1:]
        if not last or last[0] != len(body) - 1:
            break
        body.pop()

    # Raise the headings so that the shallowest one is level 2: the sections of a
    # value stream are level 4 in the source, but level 2 on their own page.
    levels = [len(HEADING.match(line).group(1)) for _, line in headings(body)]
    shift = min(levels) - 2 if levels else 0
    if shift > 0:
        for i, line in list(headings(body)):
            body[i] = line[shift:]
    return out + body


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


def document_info(preamble):
    """Build the 'About this document' content from the lines before # Preface."""
    def field(label):
        rx = re.compile(rf"^\s*{re.escape(label)}\s*(.+?)\s*$")
        value = next((m.group(1) for m in map(rx.match, preamble) if m), None)
        if value is None:
            sys.exit(f"split-framework: no '{label}' line before '# Preface' in {SOURCE.name}")
        return value.rstrip(".")

    version = field("Current version:")
    workgroup = field("Workgroup SAF:")
    created = field("Created on:")

    first = next((i for i, l in enumerate(preamble) if l.lstrip().startswith("|")), None)
    if first is None:
        sys.exit(f"split-framework: no version table before '# Preface' in {SOURCE.name}")
    table = []
    for line in preamble[first:]:
        if not line.lstrip().startswith("|"):
            break
        table.append(line.strip())

    return (f"{HEADER}\n\n"
            f"**Version {version}.** Prepared by the SAF workgroup: {workgroup}. "
            f"Created {created}.\n\n" + "\n".join(table) + "\n")


def copy_images():
    """Copy docs/images/ into site/images/ (overwriting, never deleting)."""
    if not IMAGES_SRC.is_dir():
        return 0
    shutil.copytree(IMAGES_SRC, IMAGES_OUT, dirs_exist_ok=True)
    return sum(1 for p in IMAGES_SRC.rglob("*") if p.is_file())


def main():
    n_images = copy_images()
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    starts = find_starts(lines)
    info = document_info(lines[:starts[0]])
    (OUT_DIR / DOC_INFO).write_text(info, encoding="utf-8")
    ends = starts[1:] + [len(lines)]
    bodies = {name: normalise(title, lines[s:e])
              for (name, title, _), s, e in zip(PAGES, starts, ends)}
    anchors = {name: page_anchors(body) for name, body in bodies.items()}

    problems = []
    for name, title, _ in PAGES:
        out = []
        in_fence = False
        for line in bodies[name]:
            if FENCE.match(line):
                in_fence = not in_fence
            if not in_fence:
                # Pages live one level down (site/framework/): markdown images,
                # including the <...> form used for names with spaces, and raw <img>.
                line = (line.replace("](images/", "](../images/")
                            .replace("](<images/", "](<../images/")
                            .replace('src="images/', 'src="../images/'))

                def relink(m, name=name):
                    text, target = m.group(1), m.group(2)
                    if target in anchors[name]:
                        return m.group(0)
                    owners = [p for p, a in anchors.items() if target in a]
                    if not owners:
                        # The explicit {#id} may have been dropped from the heading:
                        # fall back to the heading's auto id, derived from the link text.
                        slug = slugify(text)
                        slug_owners = [p for p, a in anchors.items() if slug in a]
                        if len(slug_owners) == 1:
                            print(f"split-framework: warning: {name}: #{target} not found, "
                                  f"linked to #{slug} (heading '{text}') instead",
                                  file=sys.stderr)
                            target, owners = slug, slug_owners
                    if len(owners) == 1:
                        if owners[0] == name:
                            return f"[{text}](#{target})"
                        return f"[{text}]({owners[0]}.qmd#{target})"
                    problems.append(f"{name}: link to #{target} has "
                                    f"{'no' if not owners else 'several'} target page")
                    return m.group(0)

                line = ANCHOR_LINK.sub(relink, line)
            out.append(line)
        text = f'---\ntitle: "{title}"\n---\n{HEADER}\n\n' + "\n".join(out).rstrip() + "\n"
        (OUT_DIR / f"{name}.qmd").write_text(text, encoding="utf-8")

    if problems:
        sys.exit("split-framework: unresolved internal links:\n  " + "\n  ".join(problems))
    print(f"split-framework: wrote {len(PAGES)} pages and {DOC_INFO} "
          f"to {OUT_DIR.relative_to(SITE.parent)}, "
          f"copied {n_images} images to {IMAGES_OUT.relative_to(SITE.parent)}")


if __name__ == "__main__":
    main()
