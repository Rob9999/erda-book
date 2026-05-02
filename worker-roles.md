# Worker Roles and Responsibilities

This file defines the working roles for the ERDA Book. It applies to book content, translations, release documentation, metadata, generated artifacts and publication work unless a more specific process file sets stricter rules.

The roles are process roles, not job titles. One person may hold several roles, but important approvals should name the role in which the person acted. AI assistance may draft, check, compare and propose changes, but it does not replace explicit human approval where this file or `AGENTS.md` requires approval.

## Core Principles

- All roles follow `AGENTS.md`, `translation-instruction.md`, `how-to-build.md` and the release process in `release-docs/`.
- Content work must remain source-transparent, license-compatible and consistent across DE and EN where applicable.
- No role should silently change the substantive meaning of a text without review by the role that owns that meaning.
- No role may mark a translation or release state as final without the required approvals.
- No role provides legal, tax, security, export-control or other professional advice on behalf of the project.

## Democratic Duty for All Roles

Every role requires a democratically sound working stance. This means observable project conduct must respect human dignity, constitutional democracy, the rule of law, pluralism, non-violence, factual honesty and transparent review.

No role may use ERDA work to normalise anti-democratic, authoritarian, dehumanising, extremist, manipulative or knowingly false claims. When democratic fitness is unclear, the affected work stays in `draft` or `in-review` until the Redakteur has clarified the issue.

This is a role-based publication and quality requirement. It governs project work, approvals and publication readiness; it is not a private thought-policing rule.

## Role Overview

| Role | Main focus | Typical decision level |
|---|---|---|
| Writer | Originating and owning substantive content intent | Meaning, claims, theses, source intent |
| Editor | Structural and conceptual improvement | Coherence, argument flow, scope, completeness |
| Lektor | Language and readability review | Grammar, style, terminology, typographic consistency |
| Redakteur | Editorial governance and acceptance | Review status, inclusion, synchronisation, release readiness |
| Publisher | Artifact and publication execution | Builds, release metadata, publishing gates, external deposits |

## Writer

### Rights

- Create new source text, propose new sections and revise existing source text.
- Decide whether edits preserve or change the intended meaning of a passage.
- Approve meaning-level changes, new theses, terminology choices and source-sensitive translations.
- Request Editor, Lektor or Redakteur review when a text needs structural, linguistic or formal acceptance.

### Duties

- State the intended argument clearly enough that later roles can preserve it.
- Provide sources, assumptions and open uncertainties where they matter.
- Respect licensing, attribution and DCO requirements for all contributions.
- Flag factual, political or ethical sensitivity instead of letting it be normalised invisibly.
- Review substantial rewrites and translations before they are treated as approved.

### Limits

- The Writer does not publish release artifacts alone.
- The Writer should not bypass editorial gates for release-bound content.

## Editor

### Rights

- Rework structure, sequence, headings, argument flow and conceptual clarity.
- Suggest additions, cuts, splits, merges and cross-reference improvements.
- Challenge unsupported claims, vague scope, duplicated content and inconsistent framing.
- Move a draft toward review readiness when the Writer's intent remains preserved.

### Duties

- Preserve the Writer's substantive intent unless a meaning change is explicitly agreed.
- Keep DE and EN structures aligned when editing translatable book content.
- Maintain Markdown structure, anchors, cross references and front matter awareness.
- Document non-trivial restructuring in commit messages, PR descriptions or review notes.

### Limits

- The Editor does not mark a translation as `approved` without the required Writer or Redakteur approval.
- The Editor does not introduce new factual claims without source or review.

## Lektor

### Rights

- Correct spelling, grammar, punctuation, typography and readability issues.
- Improve sentence rhythm, clarity and terminology consistency.
- Suggest glossary entries and detect inconsistent translation choices.
- Flag passages that are linguistically unclear or ambiguous.

### Duties

- Avoid changing substantive meaning while polishing language.
- Preserve citations, links, anchors, Markdown hierarchy and front matter.
- Keep tone consistent with the ERDA Book's democratic, analytical and non-polemical voice.
- Escalate unclear claims to the Writer, Editor or Redakteur instead of guessing.

### Limits

- The Lektor does not add new claims, new sources or new political conclusions alone.
- The Lektor does not make release or publication decisions.

## Redakteur

### Rights

- Accept, reject, defer or request revision of content for editorial reasons.
- Set or confirm review states such as `draft`, `in-review` and `approved`.
- Decide whether a chapter, translation or release note is ready for release candidate work.
- Coordinate Writer, Editor, Lektor and Publisher work where responsibilities overlap.

### Duties

- Enforce `AGENTS.md`, translation synchronisation, front matter rules and release documentation rules.
- Ensure `status: approved` is used only after explicit Writer or editorial approval.
- Check that `content_id`, `lang`, `source` and `status` remain coherent across DE and EN.
- Ensure release descriptions remain faithful to the versioned release notes.
- Document editorial decisions that affect scope, status, release readiness or public claims.

### Limits

- The Redakteur should not silently override the Writer's substantive intent.
- The Redakteur should not publish artifacts without the Publisher's metadata and artifact checks.

## Publisher

### Rights

- Run local, release and publish builds according to `how-to-build.md`.
- Regenerate Markdown, PDF and other publication artifacts when release gates are satisfied.
- Update release metadata files when the release process requires it.
- Prepare publication deposits such as Zenodo metadata after editorial release readiness is confirmed.

### Duties

- Run the metadata gate before release or publish builds.
- Verify README date, `book.json` dates, `publish.yml` versions, CFF files, `.zenodo.json`, release notes and release history consistency.
- Ensure local preview builds do not silently mutate release dates or release descriptions.
- Confirm generated artifacts correspond to the current content, navigation and release metadata.
- Stop publication when licensing, attribution, metadata or approval blockers are unresolved.

### Limits

- The Publisher does not decide substantive content meaning.
- The Publisher does not publish a release when editorial or metadata gates are incomplete.

## Approval Gates

| Gate | Required responsible role(s) | Minimum result |
|---|---|---|
| New substantive content | Writer + Editor or Redakteur | Draft is coherent and source-transparent |
| Meaning-changing edit | Writer + Editor or Redakteur | Meaning change is explicit and documented |
| Language polish | Lektor | Text is clearer without changed substance |
| Translation `approved` | Writer or Editor + Redakteur | Translation status may be set to `approved` |
| Release readiness | Redakteur + Publisher | Metadata, descriptions, translations and artifacts are ready |
| Publication | Publisher after Redakteur release readiness | Release or deposit may be published |

## Practical Change Classes

| Change class | Default owner | Required check |
|---|---|---|
| Typo, punctuation, small wording | Lektor | No meaning change |
| Structure, headings, cross references | Editor | Writer intent preserved, links still valid |
| New claim, thesis, scenario or concept | Writer | Source transparency and editorial review |
| Translation update | Editor or Lektor | `source`, `content_id`, `status` and DE source alignment |
| Translation approval | Redakteur | Explicit Writer or editorial approval exists |
| Release notes and release descriptions | Redakteur | Descriptions match versioned release notes |
| Build artifacts and publication metadata | Publisher | Metadata gate passed |
| Third-party asset, font, emoji or license change | Redakteur + Publisher | Attribution hierarchy and license files updated |

## Conflict Handling

- If roles disagree, keep the affected content in `draft` or `in-review` until the conflict is resolved.
- Prefer a short written note in the PR, commit message, issue or release status file over implicit decisions.
- When a change affects rights, licenses, attribution, safety or public claims, escalate to Redakteur before publication.
- When translation approval is uncertain, keep `status: in-review` and name the missing approval.
