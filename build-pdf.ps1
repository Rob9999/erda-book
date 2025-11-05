#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Build ERDA PDF with correct Python environment
.DESCRIPTION
    Sets correct PYTHONPATH and runs the workflow orchestrator to build the PDF
.EXAMPLE
    .\build-pdf.ps1
#>

$ErrorActionPreference = "Stop"

# Get script directory (ERDA repository root)
$RepoRoot = $PSScriptRoot

# Set correct PYTHONPATH to avoid conflicts with other projects
$env:PYTHONPATH = Join-Path $RepoRoot ".github"

# Change to repository root
Set-Location $RepoRoot

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "ERDA PDF Build" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Repository Root: $RepoRoot" -ForegroundColor Green
Write-Host "PYTHONPATH:      $env:PYTHONPATH" -ForegroundColor Green
Write-Host ""

# Run workflow orchestrator
try {
    python -m gitbook_worker.tools.workflow_orchestrator
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "================================================" -ForegroundColor Green
        Write-Host "SUCCESS: PDF Build erfolgreich!" -ForegroundColor Green
        Write-Host "================================================" -ForegroundColor Green
        
        $pdfPath = Join-Path $RepoRoot "publish\das-erda-buch.pdf"
        if (Test-Path $pdfPath) {
            $pdfInfo = Get-Item $pdfPath
            Write-Host "PDF: $pdfPath" -ForegroundColor Green
            Write-Host "Groesse: $([math]::Round($pdfInfo.Length / 1MB, 2)) MB" -ForegroundColor Green
            Write-Host "Erstellt: $($pdfInfo.LastWriteTime)" -ForegroundColor Green
        }
    }
    else {
        Write-Host ""
        Write-Host "================================================" -ForegroundColor Red
        Write-Host "FEHLER: PDF Build fehlgeschlagen (Exit Code: $LASTEXITCODE)" -ForegroundColor Red
        Write-Host "================================================" -ForegroundColor Red
        Write-Host "Pruefe die Logs in: .github\logs\" -ForegroundColor Yellow
        exit $LASTEXITCODE
    }
}
catch {
    Write-Host ""
    Write-Host "================================================" -ForegroundColor Red
    Write-Host "✗ Fehler beim PDF Build" -ForegroundColor Red
    Write-Host "================================================" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}
