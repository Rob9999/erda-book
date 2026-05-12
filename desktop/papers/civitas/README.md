# CIVITAS Public — Concept Paper

**CIVITAS Public: Building a European Digital Agora — A Call to Action**

*Version 1.0 — 6 April 2026*

DOI: [10.5281/zenodo.19443256](https://doi.org/10.5281/zenodo.19443256)

Author: Robert Alexander Massinger
Affiliation: ERDA Initiative / Independent Concept Development, Munich, Germany
License: CC BY 4.0 (Text) | MIT (Code/Scripts) | CC BY 4.0 / MIT (Fonts)

---

## Contents

```
civitas/
├── content/
│   ├── civitas_public_v1_0_zenodo.md      ← Main paper (Zenodo-ready)
│   └── civitas_public_zenodo_ready_v_1_0.md  ← Original draft (archived)
├── publish/                                ← PDF output directory (generated)
├── .zenodo.json                            ← Zenodo deposit metadata
├── CITATION.cff                            ← Citation metadata (CFF format)
├── LICENSE                                 ← CC BY 4.0 (text/graphics)
├── LICENSE-CODE                            ← MIT (scripts/tooling)
├── LICENSE-FONTS                           ← Font licensing overview
├── publish.yml                             ← gitbook_worker build manifest
├── zenodo_upload.py                        ← Zenodo upload script
└── README.md                              ← This file
```

---

## How to Build the PDF

The paper is built using the **gitbook_worker** toolchain, which converts the
Markdown source to PDF via Pandoc and LaTeX.

### Prerequisites

1. **Python virtual environment** with `gitbook_worker` installed:
   ```powershell
   cd C:\RAMProjects\ERDA
   & .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **TeX Live** (or equivalent LaTeX distribution) with `xelatex` available on PATH.

3. **Fonts** installed or accessible:
   - DejaVu Serif / Sans / Sans Mono (system or `fonts-storage/dejavu/`)
   - Twemoji Mozilla (for colour emoji, `fonts-storage/twemoji-colr/`)
   - ERDA CC-BY CJK (`.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf`)

### Build via VS Code Launch Configuration

Open the workspace in VS Code and use the **Run and Debug** panel:

1. Select the launch configuration **"Orchestrator (local) - CIVITAS Paper"**
   (or create one — see below).
2. Press **F5** to start.

If no dedicated launch config exists yet, add this to `.vscode/launch.json`:

```json
{
    "name": "Orchestrator (local) - CIVITAS Paper",
    "type": "debugpy",
    "request": "launch",
    "python": "${workspaceFolder}/.venv/Scripts/python.exe",
    "module": "gitbook_worker.tools.workflow_orchestrator",
    "cwd": "${workspaceFolder}",
    "env": {
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUTF8": "1",
        "PYTHONNOUSERSITE": "1",
        "PYTHONPATH": ""
    },
    "args": [
        "run",
        "--root",
        "${workspaceFolder}",
        "--manifest",
        "desktop/papers/civitas/publish.yml",
        "--profile",
        "local"
    ],
    "console": "integratedTerminal",
    "envFile": "${workspaceFolder}/.env"
}
```

### Build via Command Line

```powershell
cd C:\RAMProjects\ERDA
& .venv\Scripts\Activate.ps1

python -m gitbook_worker.tools.workflow_orchestrator run `
    --root . `
    --manifest desktop/papers/civitas/publish.yml `
    --profile local
```

### Output

The built PDF appears at:

```
desktop/papers/civitas/publish/civitas-public-v1.0-zenodo.pdf
```

---

## How to Publish to Zenodo

### Option A: Using `zenodo_upload.py` (recommended)

The included upload script handles DOI reservation, metadata, file upload,
and optional publishing in one step.

#### 1. Get a Zenodo API Token

- **Sandbox (testing):** https://sandbox.zenodo.org/account/settings/applications/tokens/new/
- **Production:** https://zenodo.org/account/settings/applications/tokens/new/

Required scope: `deposit:write`

#### 2. Set the Token

```powershell
# For sandbox testing:
$env:ZENODO_SANDBOX_TOKEN = "your_sandbox_token_here"

# For production:
$env:ZENODO_TOKEN = "your_production_token_here"
```

#### 3. Test with Sandbox First

```powershell
cd C:\RAMProjects\ERDA
& .venv\Scripts\Activate.ps1

# Upload as draft to sandbox (review before publishing):
python desktop/papers/civitas/zenodo_upload.py --sandbox --draft

# Upload PDF + Markdown source:
python desktop/papers/civitas/zenodo_upload.py --sandbox --draft `
    --files publish/civitas-public-v1.0-zenodo.pdf `
           content/civitas_public_v1_0_zenodo.md
```

#### 4. Upload to Production

```powershell
# Draft mode (review on Zenodo before publishing):
python desktop/papers/civitas/zenodo_upload.py --draft `
    --files publish/civitas-public-v1.0-zenodo.pdf `
           content/civitas_public_v1_0_zenodo.md

# Publish immediately (permanent — DOI will be minted):
python desktop/papers/civitas/zenodo_upload.py --publish `
    --files publish/civitas-public-v1.0-zenodo.pdf `
           content/civitas_public_v1_0_zenodo.md
```

#### 5. After Upload

1. Note the reserved DOI from the upload output.
2. Insert the DOI into the paper's citation section and CITATION.cff.
3. Rebuild the PDF and re-upload if needed (Zenodo supports versioning).

### Option B: Manual Upload

1. Go to https://zenodo.org/deposit/new
2. Upload the PDF from `publish/civitas-public-v1.0-zenodo.pdf`
3. Copy-paste metadata from `.zenodo.json` into the Zenodo form
4. Set **Resource type:** Publication → Working Paper
5. Set **License:** Creative Commons Attribution 4.0 International
6. Click **Save** → review → **Publish**

### Metadata Files

| File | Purpose |
|------|---------|
| `.zenodo.json` | Machine-readable Zenodo metadata (auto-loaded by `zenodo_upload.py`) |
| `CITATION.cff` | Standard citation metadata (GitHub, Zotero, etc.) |

---

## Related Work

This paper is part of the **ERDA Initiative**:

- **The ERDA Book:** [DOI 10.5281/zenodo.18827190](https://doi.org/10.5281/zenodo.18827190)
- **Source Repository:** https://github.com/Rob9999/erda-book
- **CIVITAS Chapter:** `de/content/6.-das-civitas-konzept/` / `en/content/6.-das-civitas-konzept/`

---

## License

- **Paper text and graphics:** [CC BY 4.0](LICENSE)
- **Scripts and tooling:** [MIT](LICENSE-CODE)
- **Fonts:** [CC BY 4.0 / MIT dual licence](LICENSE-FONTS)
