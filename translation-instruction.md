# Translation Instructions (German ➜ English)

1. **Single Source of Truth**
   - The German content inside `/content` is authoritative.
   - Never edit German originals when preparing English text; copy the section into `/en/content` first.
2. **Workflow**
   - Copy the Markdown file or heading-level excerpt you translate into `/en/content` while preserving the folder hierarchy.
   - Add a YAML front matter block with `source:` (relative path to the German file) and `status:` (`draft`, `in-review`, `approved`).
   - Commit translations only after a second reviewer confirms terminology accuracy.
3. **Terminology & Style**
   - Use plain British English unless a German institution keeps its native name.
   - Translate political terms consistently; maintain a glossary at `/en/content/GLOSSARY.md` (create when needed).
   - Keep Markdown structure, anchors and cross references intact.
4. **Change Tracking**
   - Every translation commit must mention the originating German section and include `Signed-off-by` per repository rules.
   - Divergences from the source text must be explained in inline HTML comments (`<!-- note: ... -->`).
5. **Licensing**
   - All translated text inherits CC BY-SA 4.0. Ensure cited third-party material has compatible rights before translating.
