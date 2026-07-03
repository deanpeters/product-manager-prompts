# Scripts

Repo tooling. Python 3 stdlib only; run from the repo root.

## generate-catalog.py

Walks the prompt directories, parses each file's metadata comment
block (or YAML frontmatter), and regenerates:

- `catalog/prompts-index.yaml` — machine-readable index
- `catalog/INDEX.md` — human-readable index grouped by directory

Run after adding or renaming prompts:

```bash
python3 scripts/generate-catalog.py
```

The metadata comment block is the source of truth — the catalog is
derived, never hand-edited.

## validate-prompts.py

Checks every prompt asset against the structural standards:

- required metadata fields (Description, Usage Note, Instructions,
  Attribution, Licensing, Date)
- Generative Guidance v2 fixtures, for files declaring the v2
  pattern (best-guess bypass, bulk drop, "Other" option, context
  collapse rule)
- `Companion:` references resolve to real files (repo-relative paths)
- no emojis in prompt bodies

Grandfathered files (predating the metadata standard) produce
warnings; broken v2 fixtures and dead companion links are errors.
Exit code 1 on errors — suitable for CI or a pre-commit check:

```bash
python3 scripts/validate-prompts.py
```

The warning list doubles as the migrate-on-touch worklist: when you
edit a grandfathered file for any reason, clear its warnings.
