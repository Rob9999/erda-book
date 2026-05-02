# How to Release (ERDA Book)

This document defines the **repo-level release checklist** and the **required release metadata** conventions.

## 0) Source of truth

- **Content source of truth:** German in `de/content/` (English in `en/content/` mirrors it per `translation-instruction.md`).
- **Translation mapping source of truth:** GitBook-compatible YAML front matter (`content_id`, `lang`, `source`, `status`) as defined in `translation-instruction.md`; file names are helpful but not sufficient.
- **Role responsibilities:** `worker-roles.md` defines Writer, Editor, Lektor, Redakteur and Publisher rights, duties and approval boundaries.
- **Release history:** `release-docs/Releases.md`.
- **Release narrative:** the versioned release notes in `release-docs/vX.Y.Z/` are the authoritative basis for release descriptions.
- **Release candidate work:** branch `release_candidate`.
- **Stable releases:** branch `main`.

## 1) Mandatory README release header

The root README (`README.md`) must start with a small header block where the following is **immediately visible**:

- **Current version** (e.g. `v1.0.2`)
- **As of (date)** (`YYYY-MM-DD`)
- **Channel** (`main` or `release_candidate`)
- **Codename / Release name**
  - On `release_candidate`: a **codename** (or explicitly `TBD` until set)
  - On `main`: the **release name** (typically the version tag)

Whenever any of these changes, update the README in the same commit as the corresponding release-doc updates.

Also keep the GitBook metadata dates in sync:

- `de/book.json` → `date` must match the README **As of (date)**
- `en/book.json` → `date` must match the README **As of (date)**

Do not bump release dates merely because a local preview PDF was rebuilt. Update dates when content or release metadata changed, then run the release/publish build from that synchronised state.

## 2) Release descriptions

The release notes are the editorial source of truth for what changed in a release:

- `release-docs/vX.Y.Z/release-notes-vX.Y.Z.md` (German)
- `release-docs/vX.Y.Z/release-notes-vX.Y.Z-en.md` (English)

The following files must be checked against those notes before a release/publish build:

- README release sections (DE + EN)
- `release-docs/Releases.md`
- `.zenodo.json` description, keywords and version metadata
- all CFF abstracts when the release scope changed

Shorter descriptions are allowed, but they must be faithful summaries of the release notes and must not introduce different claims, dates or scope.

## 3) Tooling: gitbook_worker is external

The build tooling (`gitbook_worker`) is maintained in a separate repository:

- https://github.com/Rob9999/gitbook-worker

This repo consumes it as a **pinned, vendored package artifact** (see `requirements.txt`).

Rules:

- Do not implement long-term tooling changes directly in this repo unless explicitly intended; prefer upstream changes.
- When the tooling version is updated, record the rationale in the relevant release docs.

## 4) Build and publish artifacts (MD/PDF)

This repository may include generated book artifacts under:

- `de/publish/` (e.g. `das-erda-buch.md`, `das-erda-buch.pdf`)
- `en/publish/` (e.g. `the-erda-book.md`, `the-erda-book.pdf`)

When committing regenerated artifacts:

- Prefer committing them together with the content/navigation changes they correspond to.
- Ensure both languages are consistent (especially `SUMMARY.md` navigation).
- Before release/publish builds, run a metadata gate: README date, `book.json` dates, `publish.yml` versions, CFF files, `.zenodo.json`, release notes and release history must agree.
- Local preview builds may validate metadata, but should not silently rewrite release dates or release descriptions.

## 5) Release candidate → main

> **Pflichtlektüre:** Vor jedem Versionswechsel die vollständige Checkliste in
> [`release-version-checklist.md`](release-version-checklist.md) abarbeiten.

Typical flow:

1. Work on `release_candidate`.
2. Keep DE↔EN changes synchronized, including front matter mapping (`content_id`, `source`, `status`).
3. Update or create the versioned release notes; use them as the basis for all release descriptions.
4. Confirm Redakteur release readiness and Publisher build responsibility per `worker-roles.md`.
5. Update the mandatory README release header.
6. Regenerate artifacts (MD/PDF) only after metadata and release descriptions are synchronized.
7. **Update all CITATION.cff files** (version, date-released, abstract, contributors):
      - `CITATION.cff` (root)
      - `de/CITATION.cff`
      - `en/CITATION.cff`
      - `de/publish/CITATION.cff`
      - `en/publish/CITATION.cff`
8. **Update `.zenodo.json`** (version, description, keywords, contributors).
9. Update or create the per-release status doc in `release-docs/vX.Y.Z/`.
10. Update `release-docs/Releases.md` for the release entry.
11. Create PR: `main` ← `release_candidate`.
12. After merge, tag `vX.Y.Z` and publish (e.g. Zenodo), following the per-release certification protocol.
