<#
.SYNOPSIS
    Deploy 47 new ICP Skill Factory Skills to Claude Cowork .skills/ directory.
.DESCRIPTION
    This script copies SKILL.md files from 05-cowork-skills/ to the Claude .skills/skills/ directory
    and updates manifest.json to register all new skills.
.NOTES
    Run from PowerShell as: .\deploy-skills.ps1
    Run from the directory containing this script (05-cowork-skills/)
#>

param(
    [switch]$DryRun,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

# ===== Find Claude .skills directory =====
$possiblePaths = @(
    "$env:APPDATA\Claude\.skills",
    "$env:USERPROFILE\.claude\.skills",
    "$env:LOCALAPPDATA\Claude\.skills",
    "$env:USERPROFILE\AppData\Local\AnthropicClaude\.skills"
)

# Also check OneDrive paths
$oneDrivePaths = @(
    "$env:OneDrive\文件\Claude\.skills",
    "$env:OneDriveCommercial\文件\Claude\.skills",
    "$env:USERPROFILE\OneDrive - Intelligent Cloud Plus Corp\文件\Claude\.skills"
)

$allPaths = $possiblePaths + $oneDrivePaths
$skillsDir = $null

foreach ($p in $allPaths) {
    if (Test-Path $p) {
        $skillsDir = $p
        break
    }
}

if (-not $skillsDir) {
    Write-Host "Cannot auto-detect .skills directory." -ForegroundColor Yellow
    Write-Host "Known search paths:"
    $allPaths | ForEach-Object { Write-Host "  $_" }
    $skillsDir = Read-Host "Please enter the full path to your Claude .skills directory"
    if (-not (Test-Path $skillsDir)) {
        Write-Error "Path does not exist: $skillsDir"
        exit 1
    }
}

Write-Host "Found .skills directory: $skillsDir" -ForegroundColor Green

# ===== Read existing manifest =====
$manifestPath = Join-Path $skillsDir "manifest.json"
if (-not (Test-Path $manifestPath)) {
    Write-Error "manifest.json not found at $manifestPath"
    exit 1
}

$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
$existingNames = $manifest.skills | ForEach-Object { $_.name }
Write-Host "Existing skills: $($existingNames.Count)" -ForegroundColor Cyan

# ===== Identify skills to deploy =====
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillDirs = Get-ChildItem -Path $scriptDir -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "SKILL.md")
}

# Separate into new vs update
$toCreate = @()
$toUpdate = @()
foreach ($dir in $skillDirs) {
    if ($existingNames -contains $dir.Name) {
        $toUpdate += $dir
    } else {
        $toCreate += $dir
    }
}

Write-Host "`nSkills to CREATE: $($toCreate.Count)" -ForegroundColor Green
Write-Host "Skills to UPDATE: $($toUpdate.Count)" -ForegroundColor Yellow

if ($DryRun) {
    Write-Host "`n[DRY RUN] Would create:" -ForegroundColor Magenta
    $toCreate | ForEach-Object { Write-Host "  + $($_.Name)" }
    Write-Host "`n[DRY RUN] Would update:" -ForegroundColor Magenta
    $toUpdate | ForEach-Object { Write-Host "  ~ $($_.Name)" }
    exit 0
}

# ===== Deploy SKILL.md files =====
$deployed = 0

# Create new skills
foreach ($dir in $toCreate) {
    $targetDir = Join-Path $skillsDir "skills" $dir.Name
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    $src = Join-Path $dir.FullName "SKILL.md"
    $dst = Join-Path $targetDir "SKILL.md"
    Copy-Item -Path $src -Destination $dst -Force
    Write-Host "  + $($dir.Name)" -ForegroundColor Green
    $deployed++
}

# Update existing skills (only if -Force or file is newer)
foreach ($dir in $toUpdate) {
    $targetDir = Join-Path $skillsDir "skills" $dir.Name
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    $src = Join-Path $dir.FullName "SKILL.md"
    $dst = Join-Path $targetDir "SKILL.md"

    if ($Force -or -not (Test-Path $dst)) {
        Copy-Item -Path $src -Destination $dst -Force
        Write-Host "  ~ $($dir.Name) (updated)" -ForegroundColor Yellow
        $deployed++
    } else {
        $srcTime = (Get-Item $src).LastWriteTime
        $dstTime = (Get-Item $dst).LastWriteTime
        if ($srcTime -gt $dstTime) {
            Copy-Item -Path $src -Destination $dst -Force
            Write-Host "  ~ $($dir.Name) (newer)" -ForegroundColor Yellow
            $deployed++
        } else {
            Write-Host "  = $($dir.Name) (skip, up to date)" -ForegroundColor DarkGray
        }
    }
}

# ===== Update manifest.json =====
Write-Host "`nUpdating manifest.json..." -ForegroundColor Cyan

# Backup manifest
$backupPath = "$manifestPath.bak.$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Copy-Item $manifestPath $backupPath
Write-Host "  Backup: $backupPath" -ForegroundColor DarkGray

$now = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.ffffffZ")

foreach ($dir in $toCreate) {
    $skillMdPath = Join-Path $dir.FullName "SKILL.md"
    $content = Get-Content $skillMdPath -Raw

    # Extract name and description from YAML frontmatter
    $name = $dir.Name
    $desc = ""
    if ($content -match '(?s)---\s*\n(.*?)\n---') {
        $yaml = $Matches[1]
        if ($yaml -match 'description:\s*>\s*\n((?:\s+.+\n)+)') {
            $desc = ($Matches[1] -replace '\s+', ' ').Trim()
        } elseif ($yaml -match 'description:\s*(.+)') {
            $desc = $Matches[1].Trim()
        }
    }

    # Generate a skill ID
    $bytes = [System.Text.Encoding]::UTF8.GetBytes("$name-$now")
    $hash = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    $skillId = "skill_" + [Convert]::ToBase64String($hash).Substring(0, 24).Replace("+","A").Replace("/","B").Replace("=","")

    $newSkill = [PSCustomObject]@{
        skillId = $skillId
        name = $name
        description = $desc.Substring(0, [Math]::Min($desc.Length, 500))
        creatorType = "user"
        updatedAt = $now
        enabled = $true
    }

    $manifest.skills += $newSkill
}

# Update lastUpdated
$manifest.lastUpdated = [long]([DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds())

# Write manifest
$manifest | ConvertTo-Json -Depth 10 | Set-Content $manifestPath -Encoding UTF8
Write-Host "  manifest.json updated with $($toCreate.Count) new entries" -ForegroundColor Green

# ===== Summary =====
Write-Host "`n===== Deployment Complete =====" -ForegroundColor Green
Write-Host "  Created: $($toCreate.Count) new skills"
Write-Host "  Updated: $($toUpdate.Count) existing skills"
Write-Host "  Total deployed: $deployed files"
Write-Host "`nPlease restart Claude Desktop to load the new skills." -ForegroundColor Yellow
