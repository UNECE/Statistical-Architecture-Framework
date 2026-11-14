# AGENTS.md

## Project

UNECE SAF Reference Architecture: a reference architecture for National Statistics Organisations, modelled in ArchiMate with Archi. See [README.md](README.md) for the overview.

- `docs/` — documentation (the framework text lives in `docs/SAF Framework.md`) and the Archi model contents
- `site/` — website; framework chapters in `site/framework/` are generated from `docs/SAF Framework.md` by a script (see `site/scripts/README.md`)
- `release/` — release material

## Rules

- **Never change any markdown (`.md`) file without asking the user first.** This applies to every markdown file in the repository, including README.md, GettingStarted.md, `docs/`, and `site/`. Propose the change and wait for explicit approval before editing, creating, renaming or deleting one.
- Do not hand-edit generated chapter pages in `site/framework/`; changes belong in `docs/SAF Framework.md` (and still require asking first).
- Do not remove architecture artefacts without asking. The artefacts in the model should always be synchronized with the chapters in the `docs/SAF Framework.md` file.
