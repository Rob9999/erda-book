# The ERDA Book – Release v2.5.0

**Date:** 2026-03-05 (updated: 2026-05-04)
**Tag:** `v2.5.0` (planned)
**Codename:** Democratic Knowledge
**Author:** Robert Alexander Massinger (with ChatGPT/OpenAI and GitHub Copilot/Anthropic)

---

## 📋 Summary

Version 2.5.0 deepens the **normative foundations** of the ERDA Book. At its centre is the document **"Democratic Knowledge"** – seven principles serving as a guide for democratic agency: on power, on dealing with non-democracy-willing states, on peace and security, on truth and deception, on democracy itself, on technology/AI, and on the inner condition of a democratic society.

In addition, this release integrates three conceptual papers as book content: a **guiding vision for child-rearing** (§11.3.7), a **strategic reflection on the Mosaic Principle** (§5.8.4), and the **Anti-Game-Over Principle** as **Appendix P.1** – a developmental-philosophical model of prosperative life. It also adds **Appendix M** as a measurable book-project yardstick for release criteria, source standards and open project decisions.

---

## ✨ Changes

### New content

- **"Democratic Knowledge" (Seven Principles):** Standalone reference document as desktop material (DE + EN) with clear, citable guiding principles on the core themes of democratic resilience.

- **§11.3.7 – Guiding vision: raising children in freedom and responsibility (DE + EN):**
  Twelve guiding principles for a democratic culture of education – from taking responsibility to freedom from fear to dealing with power and conscience. Inserted into chapter 11.3 "What do citizens need?".

- **§5.8.4 – Strategic reflection: Mosaic Principle and democratic DSN resilience (DE + EN):**
  Connecting the Mosaic Principle known from authoritarian warfare with the rule-of-law-bound DSN architecture. Inserted into chapter 5.8 "Defence Sovereignty Nodes".

- **Appendix M – Measure: Measurable Book-Project Decisions and Release Criteria (DE + EN):**
  New yardstick appendix: translates the book-project decisions into reviewable criteria for baselines, sources, scenarios, draft status, paper compliance and release residual risks.

- **Appendix P.1 – Paper: Childhood, Adulthood, and the Anti-Game-Over Principle (DE + EN):**
  Paper appendix: a developmental-philosophical model that understands childhood and adulthood as cyclically recurring basic forms of open life. Formulates anti-game-over principles and the ideal of a *prosperative life*. (DOI: 10.5281/zenodo.19244929; APA citation in the paper header)

- **Cross-references** in chapters 11.2, 11.3, 3.5, and 4.3.5 pointing to Appendix P.1.

### Editorial improvements

- **README "Contributions and quality":** DE and EN sections rewritten in a professional editorial voice – framing the ERDA Book as a living document of democratic resilience, with structured guidelines (quality standards, binding rules, peer-review principle).

- **Role and approval model:** Writer, Editor, Lektor, Redakteur and Publisher were defined with rights, duties, approval boundaries and a democratic role duty in `worker-roles.md` and anchored in the binding guides.

- **Ethics before strategy:** A worker-roles pass strengthens chapters 2, 3, 11, 12 and Appendix H ethically and morally, then strategically sharpens chapters 5, 13, 14 and Appendix D. New glossary terms include democracy of mature citizens, we are the state, democratic alliance reliability, the Ukraine-first principle and anti-veto.

- **Glossary and mini wording:** Core v2.5 terms were editorially added: Democratic Knowledge, Mosaic Principle, Anti-Game-Over Principle and prosperative life.

### Technical

- Version bump to v2.5.0-rc1
- Release documentation in `release-docs/v2.5.0/`
- Desktop materials in `desktop/misc/`
- `book.json` date updated to 2026-05-04 (DE + EN)
- SUMMARY.md updated (DE + EN) with Appendix M and Appendix P entries
- Root `ATTRIBUTION.md` added as primary source for third-party assets
- YAML front matter normalised with `content_id`, `content_lang`, `source` and `status` for DE/EN content files; Pandoc/Babel-adjacent keys such as `lang`, `language` and `lang-version` are avoided in content front matter to keep Twemoji/ERDA CJK PDF font fallback stable
- Release metadata gate applied: README date, `book.json`, CFF files and `.zenodo.json` synchronised
- English Appendix J/L file paths normalised to `appendix-j-license-and-openness.md` and `appendix-l-colophon.md`
- DE/EN cross-references to Appendix P.1 updated in chapters 3.5, 4.3.5, 11.2 and 11.3

---

## 📦 Multilingual versions in this release

- de (source of truth)
- en (synchronised, draft/review)

---

## 🔗 Related documents

- [Release plan](release-plan-v2.5.0.md)
- [Release status](RELEASE-2.5.0-STATUS.md)
