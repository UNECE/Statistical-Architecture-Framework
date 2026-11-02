# `site/scripts/`

This folder has one script, `split-framework.py`. It builds the Framework chapter pages of the website from the single source document `docs/SAF Framework.md`.

- [Purpose](#purpose)
- [How it runs](#how-it-runs)
- [Inputs and outputs](#inputs-and-outputs)
- [How it works, step by step](#how-it-works-step-by-step)
- [Editing the source document safely](#editing-the-source-document-safely)
- [Changing how the document is split](#changing-how-the-document-is-split)
- [Troubleshooting](#troubleshooting)
- [Known limitations](#known-limitations)

## Purpose

The Framework is written and reviewed as one long Markdown file, `docs/SAF Framework.md`. That is convenient for authors, but a single page with several thousand lines is hard to read on a website. The script cuts the file into one Quarto page per chapter and per value stream. While doing that, it fixes the links and image paths that the cut would otherwise break.

Rules that follow from this:

- **`docs/SAF Framework.md` is the single source of truth.** Edit only that file.
- **Never edit the generated `site/framework/*.qmd` pages.** They are overwritten on every render, and each one starts with a reminder:
  `<!-- GENERATED from docs/SAF Framework.md by scripts/split-framework.py - do not edit -->`
- **`site/framework/index.qmd` is the exception.** It is written by hand (the chapter overview), and the script never touches it. Its "About this document" box pulls in one generated file, `_document-info.md`, with `{{< include _document-info.md >}}`. That file holds the version, workgroup, creation date and version table, taken from the top of the source document.

## How it runs

### Automatically, through Quarto

`site/_quarto.yml` declares the script as a project pre-render step:

```yaml
project:
  pre-render: python3 scripts/split-framework.py
```

So Quarto runs it before every `quarto render` or `quarto preview` of the `site/` project. That covers your machine and both GitHub workflows (`.github/workflows/deploy-pages.yml` for production and `.github/workflows/pr-preview.yml` for pull-request previews). If the script exits with an error, the render stops, and so does the deployment.

### Manually

```sh
python3 site/scripts/split-framework.py
```

You can run this from any directory, because every path is resolved from the script's own location (`SITE = Path(__file__).resolve().parent.parent`). It needs Python 3 and nothing else; it uses only the standard library (`re`, `sys`, `unicodedata`, `pathlib`).

Running it by hand is the quickest way to check your edits to the source document before a full Quarto render.

### Generated files are not committed

The 14 generated pages and the `site/images/` folder (copied from `docs/images/`) are listed in the repository's root `.gitignore`. They exist only in working copies and CI runners, and never appear in commits or diffs.

`_document-info.md` is the exception: it is committed as an **empty placeholder**. Quarto expands `{{< include >}}` while it first scans the project, *before* the pre-render script runs. Without the placeholder, a fresh checkout (as in CI) fails with `Include directive failed ... could not find file .../_document-info.md`. The script then overwrites the placeholder, and the render uses the real content. After a local render, git shows the file as modified. Don't commit that change; discard it with `git restore site/framework/_document-info.md`, or hide it once with `git update-index --skip-worktree site/framework/_document-info.md`.

## Inputs and outputs

| Constant | Value | Meaning |
|---|---|---|
| `SITE` | `site/` | The Quarto project folder |
| `SOURCE` | `docs/SAF Framework.md` | The single source document |
| `OUT_DIR` | `site/framework/` | Where the pages are written |
| `IMAGES_SRC` | `docs/images/` | The images used by the source document |
| `IMAGES_OUT` | `site/images/` | Where those images are copied for the site |

The `PAGES` list defines what gets generated. Each entry is `(file name, page title, regex for the heading that starts the page)`:

| Output file | Page title | Starts at the line matching |
|---|---|---|
| `introduction.qmd` | Introduction and Scope | `^# Preface\s*$` |
| `motivation.qmd` | Motivation | `^# Motivation\s*$` |
| `strategy.qmd` | Strategy | `^# Strategy\s*$` |
| `business-architecture.qmd` | Business Architecture | `^# Business Architecture\s*$` |
| `vs-01.qmd` | VS-01 Data Acquisition and Ingestion | `^## VS-01\.0 (?!—)` |
| `vs-02.qmd` | VS-02 Data Standardization and Integration | `^## VS-02\.0 (?!—)` |
| `vs-03.qmd` | VS-03 Data Editing and Enrichment | `^## VS-03\.0 (?!—)` |
| `vs-04.qmd` | VS-04 Estimation, Analysis, and Statistical Modeling | `^## VS-04\.0 (?!—)` |
| `vs-05.qmd` | VS-05 Statistical Product Composition | `^## VS-05\.0 (?!—)` |
| `vs-06.qmd` | VS-06 Dissemination and Service Delivery | `^## VS-06\.0 (?!—)` |
| `vs-07.qmd` | VS-07 Governance and Compliance | `^## VS-07\.0 (?!—)` |
| `vs-08.qmd` | VS-08 Innovation and Methodological Development | `^## VS-08\.0 (?!—)` |
| `vs-09.qmd` | VS-09 Infrastructure and Platform Enablement | `^## VS-09\.0 (?!—)` |
| `vs-10.qmd` | VS-10 Customer and Stakeholder Engagement | `^## VS-10\.0 (?!—)` |

The "Introduction and Scope" page starts at `# Preface`, so it holds the Preface, Acknowledgements and Introduction chapters together.

The script also writes **`site/framework/_document-info.md`** (constant `DOC_INFO`), which `index.qmd` includes. Quarto does not turn files whose names start with `_` into pages of their own.

## How it works, step by step

The whole job happens in `main()`, which relies on a few small helpers.

### 0. Copy the images (`copy_images`)

Everything in `docs/images/`, subfolders included, is copied to `site/images/`. Existing files are overwritten, so an edited image always reaches the site. Nothing is ever deleted (see [Known limitations](#known-limitations)). This makes `docs/images/` the single source for images, just as `docs/SAF Framework.md` is for text. An image referenced as `images/<file>` therefore displays both when the Markdown is viewed on GitHub and on the website.

### 1. Read the source

`SOURCE` is read as UTF-8 and split into a list of lines. All later steps work with line indexes.

### 2. Find where each page starts (`find_starts`)

For each entry in `PAGES`, in order, the script looks for the first line matching that entry's regex. The search starts just **after** the previous page's start line (`cursor`), which has two effects:

- Pages always come out in the order of `PAGES`, and that order must match the order in the document.
- A pattern can only match below the previous page's heading, so an identical heading earlier in the file (in the manual table of contents, for example) is never picked by mistake.

If a pattern matches nothing, the script stops at once with `no heading matching ... for page '...'` (see [Troubleshooting](#troubleshooting)).

**Why the VS patterns end with `(?!—)`.** The document mentions each value stream heading twice:

- In the Business Architecture chapter, a summary section per stream, written with an em dash: `## VS-02.0 — Data Standardization and Integration`
- Further down, the full chapter for each stream, without a dash: `## VS-02.0 Data Standardization and Integration`

The negative lookahead `(?!—)` refuses a match when an em dash follows `VS-NN.0 `. As a result, the summaries stay inside the Business Architecture page and only the full chapters start new pages. **This difference in punctuation carries meaning: don't "harmonise" those headings.**

### 3. Cut the document into page bodies

Each page runs from its start line up to the line before the next page's start, and the last page (`vs-10`) runs to the end of the file:

```python
ends = starts[1:] + [len(lines)]
bodies = {name: lines[s:e] ...}
```

Everything **above** `# Preface` goes on no chapter page. Part of it feeds the document information (step 3b), and the rest (the title and the hand-written "Content" list of links) is dropped, because Quarto's sidebar and table of contents replace it.

### 3b. Build the document information (`document_info`)

From the lines above `# Preface`, the script reads:

| In the source | Becomes |
|---|---|
| `Current version: 0.5` | `**Version 0.5.**` |
| `Workgroup SAF: <names>` | `Prepared by the SAF workgroup: <names>.` |
| `Created on: 07-07-2025` | `Created 07-07-2025.` |
| the first block of consecutive lines starting with `\|` | the version table, copied unchanged |

Each label is matched at the start of a line, and the rest of the line is taken as the value (without a trailing full stop). The result, with the usual GENERATED comment on top, is written to `site/framework/_document-info.md`. If a label or the table is missing, the script stops with an error, so the box on the website can never quietly go stale.

### 4. Collect the anchors on each page (`headings`, `page_anchors`, `slugify`)

Fixing links later requires knowing which page each heading anchor ended up on. For every page, `page_anchors` builds the set of anchors of its headings:

- `headings(lines)` yields every Markdown heading (`#` to `######`) that is **not** inside a fenced code block. A line starting with ```` ``` ```` or `~~~` switches the "inside fence" state on or off. Without this, comment lines that begin with `#` inside code blocks or mermaid diagrams would count as headings.
- If a heading has an explicit identifier, as in `## Drivers {#drivers}`, that identifier is used.
- Otherwise the anchor is computed by `slugify`, which imitates the automatic identifiers Pandoc and Quarto give headings:
  1. Replace links `[text](url)` with their text.
  2. Remove the emphasis and code markers `` ` ``, `*` and `_`.
  3. Normalise the Unicode (NFKC) and convert to lowercase.
  4. Remove every character that is not a letter, a digit, whitespace, `.`, `-` or `_`.
  5. Replace runs of whitespace with `-`.
  6. Strip leading digits and the characters `.`, `-` and `_`. If nothing is left, use `section`.

  For example, `## Value Streams **[T1]**` becomes `value-streams-t1`.

The result is `anchors`, a dictionary `{page name: set of anchors on that page}`.

### 5. Rewrite each page

Every line of every page is processed. Lines inside fenced code blocks are copied unchanged. All other lines get two rewrites.

**a. Image paths.** Generated pages sit in `site/framework/`, one level below the site root, so image paths get one `../` more. All three forms are handled: `](images/` becomes `](../images/`, `](<images/` becomes `](<../images/` (the angle-bracket form Markdown needs for file names with spaces), and `src="images/` becomes `src="../images/` (raw HTML `<img>`). Images therefore resolve to `site/images/`, where step 0 copied them.

**b. Internal links.** The source document uses links within the same file, such as `[Drivers](#drivers)`. After the split, the target heading may be on a different page. The regex `ANCHOR_LINK` finds each `[text](#target)`, and `relink` decides what to do with it:

1. **The target is on the current page:** leave the link unchanged.
2. **Exactly one other page has the target:** rewrite it to `[text](other-page.qmd#target)`. Quarto turns `.qmd` links into `.html` links when it renders.
3. **No page has the target.** This usually means a heading was renamed or lost its `{#id}`. The script then computes `slugify(text)` from the **link text** and checks whether exactly one page has a heading with that anchor. If so, it uses that heading and prints a warning, because the source document should still be fixed.
4. **Still nothing, or several pages have the target:** the link stays as it is and the problem is recorded.

Links to external URLs, and links like `page.qmd#x` that already name a file, never match `ANCHOR_LINK`, so they are left alone.

### 6. Write the pages

Each page is written to `site/framework/<name>.qmd` as:

```
---
title: "<title from PAGES>"
---
<!-- GENERATED from docs/SAF Framework.md by scripts/split-framework.py - do not edit -->

<page body, trailing blank lines removed>
```

### 7. Report

- If any link could not be resolved, the script exits with a non-zero status and lists all of them. Quarto then stops the render. Note that the pages have **already been written** by then, so a local preview may still show them.
- Otherwise it prints `split-framework: wrote 14 pages and _document-info.md to site/framework, copied N images to site/images`.

Warnings and errors go to stderr, and each starts with `split-framework:`.

## Editing the source document safely

Most edits to `docs/SAF Framework.md` need no thought about the script. The following do:

- **Keep the document information above `# Preface`:** the lines starting with `Created on:`, `Workgroup SAF:` and `Current version:`, and the version table. Update them there. They appear on the Framework index page.
- **Keep the four top-level headings exactly as they are:** `# Preface`, `# Motivation`, `# Strategy`, `# Business Architecture`. Each one must be alone on its line (trailing spaces are fine).
- **Keep the value stream chapter headings in the form `## VS-NN.0 Name`:** level 2, `VS-` followed by two digits, `.0`, a space, then the name with **no em dash**. Keep them in order, VS-01 to VS-10, and after `# Business Architecture`.
- **Keep the summary headings in Business Architecture in the form `## VS-NN.0 — Name`, with the em dash.** Otherwise a summary heading would be taken as the start of a page.
- **Internal links (`[text](#anchor)`) must point to a heading that exists, and each anchor must be unique across the whole document.** If two pages have a heading with the same anchor, a link to it is ambiguous and the build fails. When two headings have the same text, give one of them an explicit `{#unique-id}`.
- **Prefer explicit `{#id}`s on headings you link to.** The heading text can then change without breaking links.
- **Images:** put the file in **`docs/images/`** and reference it as `![Caption](images/<file>)`, or `![Caption](<images/<file with spaces>>)`, on a line of its own with blank lines around it. Quarto then renders it as a captioned figure, in the PDF as well. Avoid raw HTML `<img>` tags (the PDF drops them) and images hosted at GitHub `user-attachments` URLs (they live outside the repository).
- **Code fences:** close every ```` ``` ```` or `~~~` block you open. An unclosed fence makes the script treat the rest of the page as code, so its headings and links are skipped.

## Changing how the document is split

To add, remove or rename a generated page:

1. **Edit `PAGES`** in `split-framework.py`. Order matters: entries must be in the order their start headings appear in the document. Make the regex specific enough to match only the intended heading.
2. **Update the sidebar** in `site/_quarto.yml` (`website.sidebar ... contents`), so the page appears in navigation.
3. **Update the list of generated files** in the root `.gitignore`, so the new file is not committed by accident.
4. **Update the chapter table** in `site/framework/index.qmd`, which is written by hand.
5. Run `python3 site/scripts/split-framework.py` and then `quarto preview site` to check the result.

When you rename or remove a page, delete the old generated `.qmd` from your working copy. The script never removes files.

## Troubleshooting

### `split-framework: no heading matching '<regex>' for page '<name>' in SAF Framework.md`

The heading that starts page `<name>` was not found below the previous page's start. Typical causes:

- The heading was renamed, or its level changed (`#` versus `##`).
- An em dash was added to a VS chapter heading, or a regular hyphen or en dash replaced the em dash in a summary heading. Either way, the wrong heading now matches, or nothing does.
- Chapters were reordered, so the heading now comes *before* the previous page's start.

Fix the heading in the source document, or adjust the regex in `PAGES` if the change was intentional.

### `split-framework: no 'Current version:' line before '# Preface' in SAF Framework.md` (or `Workgroup SAF:`, `Created on:`, `no version table`)

The document information at the top of the source document was removed, renamed or moved below `# Preface`. Restore that line with its exact label, or restore the table.

### `split-framework: warning: <page>: #<target> not found, linked to #<slug> (heading '<text>') instead`

A link points to an anchor that no longer exists. The script guessed the right heading from the link text, so the site still works, but the guess may be wrong. Fix the link in the source, or put the explicit `{#<target>}` back on the heading. For example, this warning appeared after the `{#pragmatic-steady-states}` id was dropped from a heading. Adding the id back fixed it:

```
split-framework: warning: business-architecture: #pragmatic-steady-states not found,
linked to #applying-the-steady-states-pragmatically (heading 'Applying the steady states pragmatically') instead
```

### `split-framework: unresolved internal links:` followed by `<page>: link to #<target> has no target page` / `several target page`

- **"no target page"**: no heading anywhere has this anchor, and the link text did not lead to exactly one heading either. Fix the link target, or add `{#<target>}` to the intended heading.
- **"several target page"**: more than one page has a heading with this anchor. Give the intended heading a unique explicit `{#id}` and link to that.

### A link works but lands at the wrong place, or at the top of the page

`slugify` only approximates Pandoc's algorithm. For unusual headings (symbols, emoji, unusual punctuation) the two can disagree. The page is then right but the `#anchor` is not. Add an explicit `{#id}` to the heading and link to it.

## Known limitations

- **Fence detection is a simple toggle.** Any line that starts with ```` ``` ```` or `~~~` flips the state. Fences nested inside other fences, or fences of different lengths, are not handled.
- **Only inline anchor links `[text](#id)` are rewritten.** Reference-style links (`[text][ref]`), raw HTML anchors (`<a href="#id">`) and bare `#id` text are left unchanged, and will break if their target is on another page.
- **Images are copied, never deleted.** A file removed or renamed in `docs/images/` stays in your local `site/images/` until you delete it. CI always starts from a clean checkout, so the published site is not affected.
- **Page titles come from `PAGES`,** not from the document headings. When you rename a chapter in the source, update its title in the script too.
- **Generated pages are written even when the run fails,** and old pages are never deleted.
- **Only the first table before `# Preface` is used** as the version table. Any other table above `# Preface` is ignored.
- **`_document-info.md` is a tracked file that every render overwrites,** so it shows as modified after a local render (see [Generated files are not committed](#generated-files-are-not-committed)). Rendering `index.qmd` on its own, without the pre-render step, shows an empty box.
