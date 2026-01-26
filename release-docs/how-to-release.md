# How to Release (ERDA Book)

This document defines the **repo-level release checklist** and the **required release metadata** conventions.

## 0) Source of truth

- **Content source of truth:** German in `de/content/` (English in `en/content/` mirrors it per `translation-instruction.md`).
- **Release history:** `release-docs/Releases.md`.
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

## 2) Tooling: gitbook_worker is external

The build tooling (`gitbook_worker`) is maintained in a separate repository:

- https://github.com/Rob9999/gitbook-worker

This repo consumes it as a **pinned, vendored package artifact** (see `requirements.txt`).

Rules:

- Do not implement long-term tooling changes directly in this repo unless explicitly intended; prefer upstream changes.
- When the tooling version is updated, record the rationale in the relevant release docs.

## 3) Build and publish artifacts (MD/PDF)

This repository may include generated book artifacts under:

- `de/publish/` (e.g. `das-erda-buch.md`, `das-erda-buch.pdf`)
- `en/publish/` (e.g. `the-erda-book.md`, `the-erda-book.pdf`)

When committing regenerated artifacts:

- Prefer committing them together with the content/navigation changes they correspond to.
- Ensure both languages are consistent (especially `SUMMARY.md` navigation).

## 4) Release candidate → main

Typical flow:

1. Work on `release_candidate`.
2. Keep DE↔EN changes synchronized.
3. Regenerate artifacts (MD/PDF) as needed.
4. Update the mandatory README release header.
5. Update or create the per-release status doc in `release-docs/vX.Y.Z/`.
6. Update `release-docs/Releases.md` for the release entry.
7. Create PR: `main` ← `release_candidate`.
8. After merge, tag `vX.Y.Z` and publish (e.g. Zenodo), following the per-release certification protocol.
