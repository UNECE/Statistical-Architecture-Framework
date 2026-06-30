# SAF Business Layer Documentation

This folder contains the business-layer documentation of the Statistical Architecture Framework (SAF): how a National Statistical Office (NSO) turns externally-held data into trusted statistics, described as ten value streams. The documents are a **canvas** — NSOs are expected to instantiate them for their own context, not to adopt them verbatim.

## Reading order

1. **`SAF-Business-Layer.qmd`** — the consolidated overview. Read this first: it explains once the shared scaffolding (the data value chain and its steady states, the four-process governance pattern, the principles), then summarises all ten streams.
2. **`VS-01.0` … `VS-06.0`** — the six **primary** value streams forming the production chain (acquisition → standardization → editing → estimation → product composition → dissemination). Each follows the same template:
   - Introduction and Strategic Context (position, steady-state transition, governance pattern, principles, capabilities, metadata perspective)
   - Business Roles and Actors
   - Design / Implementation / Execution / Management processes (the four-process governance pattern)
   - Business Services and Interfaces · Business Objects and Data Flow · Business Events
   - Applying This to Your NSO (maturity checklist + end-to-end scenarios)
3. **`VS-07.0` … `VS-10.0`** — the four **supporting** value streams (governance, innovation, infrastructure, engagement). They run horizontally and continuously, align to GAMSO rather than GSBPM, and are documented in a leaner continuous-capability format (plan → build → operate → improve).

Shared text blocks used by several documents live in `_includes/`.

## Rendering

The folder is a Quarto website project (`_quarto.yml`); `index.qmd` is the landing page.

```sh
quarto preview docs/business-layer         # live HTML site with sidebar + search
quarto render docs/business-layer         # full HTML site into _site/ (gitignored)
```

HTML rendering needs no extra dependencies — mermaid diagrams render client-side.

PDFs are produced with the `pdf` profile (`_quarto-pdf.yml`, typst):

```sh
quarto render docs/business-layer --profile pdf --to typst                # all documents
quarto render docs/business-layer/VS-01.0-Data-Acquisition-and-Ingestion.qmd --profile pdf --to typst
```

PDF output also lands in `_site/`. Mermaid diagrams in PDFs need Chromium (`quarto install chromium`, or point `QUARTO_CHROMIUM` at a chrome-headless-shell binary).

Requirements: [Quarto](https://quarto.org) ≥ 1.4 (typst is bundled).

The PDFs committed alongside the sources are point-in-time deliverables; copy them out of `_site/` after a PDF render to refresh them. Note: a PDF render also deletes the committed in-tree PDF of the rendered document (Quarto cleans it up as a stale output) — restore it with `git checkout` or replace it with the fresh copy from `_site/`.
