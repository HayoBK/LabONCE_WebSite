# ============================================================
# LAB ONCE — Script de inicialización de git + primer push
# Uso: en PowerShell, desde E:\Git_Use_LabOnce
#   .\setup-git.ps1 -Usuario "tu-usuario-github" -Repo "Web"
# Requiere estar autenticado en la cuenta correcta (gh auth login o credential manager).
# ============================================================

param(
  [Parameter(Mandatory=$true)][string]$Usuario,
  [Parameter(Mandatory=$true)][string]$Repo,
  [switch]$FijarBaseURL  # si se pasa, escribe el baseURL real en hugo.yaml
)

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

if ($FijarBaseURL) {
  $cfg = "config\_default\hugo.yaml"
  $base = "https://$Usuario.github.io/$Repo/"
  (Get-Content $cfg -Raw) -replace 'baseURL:\s*".*?"', "baseURL: `"$base`"" | Set-Content $cfg -Encoding UTF8
  Write-Host "baseURL fijado a $base"
}

if (-not (Test-Path ".git")) {
  git init
  git branch -M main
}

git add -A
git commit -m "LAB ONCE: primera version del sitio (Hugo autocontenido)"

if (-not (git remote | Select-String -Quiet "origin")) {
  git remote add origin "https://github.com/$Usuario/$Repo.git"
}

git push -u origin main

Write-Host "`n=== LISTO ===" -ForegroundColor Green
Write-Host "Ahora ve a GitHub -> repo $Usuario/$Repo -> Settings -> Pages -> Source: GitHub Actions."
Write-Host "El sitio quedara en https://$Usuario.github.io/$Repo/"
