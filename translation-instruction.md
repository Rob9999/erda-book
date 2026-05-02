# Translation Instructions (German ➜ English)

1. **Single Source of Truth**
   - German content in `de/content/` is authoritative.
   - Never edit German originals when preparing English text; copy the section into `en/content/` first.

2. **Canonical Mapping**
   - File names and mirrored folders are useful for humans and GitBook navigation, but they are not the only mapping mechanism.
   - Every book content Markdown file must use GitBook-compatible YAML front matter, except special navigation files such as `SUMMARY.md` when the tooling treats them separately.
   - German source files should carry at least:
     ```yaml
     ---
     content_id: erda.example.stable-id
     lang: de
     ---
     ```
   - English translation files must carry at least:
     ```yaml
     ---
     content_id: erda.example.stable-id
     lang: en
     source: de/content/path/to/german-source.md
     status: draft
     ---
     ```
   - `content_id` is stable across languages and must not change when files are renamed.
   - `source` is repo-relative and should start with `de/content/` for English translations.
   - Existing legacy front matter may be normalised incrementally, but every newly created or substantively edited translation must follow this schema.

3. **Translation Status**
   - `status:` must be one of `draft`, `in-review`, or `approved`.
   - Use `draft` for first translations or unsynchronised updates.
   - Use `in-review` when terminology, factual claims or editorial tone require review.
   - Use `approved` only after explicit writer/editor approval.
   - Role responsibilities and approval boundaries are defined in `worker-roles.md`.
   - Recommended for approved translations: add `source_commit:` or `source_hash:` so later tooling can detect source drift.
4. **Workflow**
   - Copy the Markdown file or heading-level excerpt you translate into `en/content/` while preserving the folder hierarchy where practical.
   - Add or update the YAML front matter before translating body text.
   - Commit translations only after a second reviewer confirms terminology accuracy.

5. **Terminology & Style**
   - Use plain British English unless a German institution keeps its native name.
   - Translate political terms consistently; maintain a glossary at `/en/content/GLOSSARY.md` (create when needed).
   - Keep Markdown structure, anchors and cross references intact.
6. **Change Tracking**
   - Every translation commit must mention the originating German section and include `Signed-off-by` per repository rules.
   - Divergences from the source text must be explained in inline HTML comments (`<!-- note: ... -->`).
7. **Licensing**
   - All translated text inherits CC BY-SA 4.0. Ensure cited third-party material has compatible rights before translating.
