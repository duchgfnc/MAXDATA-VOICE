param(
    [ValidateSet("min", "all")][string]$Mode = "min",
    [string]$Token  = $env:GH_TOKEN,
    [string]$Owner  = "duchgfnc",
    [string]$Repo   = "MAXDATA-VOICE",
    [string]$Branch = "main"
)
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$Root = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($Token)) { "缺少 Token"; exit 1 }

$api = "https://api.github.com/repos/$Owner/$Repo/contents"
$h = @{ Authorization = "Bearer $Token"; Accept = "application/vnd.github+json"; "User-Agent" = "MAXDATA-VOICE"; "X-GitHub-Api-Version" = "2022-11-28" }

$me = Invoke-RestMethod -Uri "https://api.github.com/user" -Headers $h -TimeoutSec 30
$rp = Invoke-RestMethod -Uri "https://api.github.com/repos/$Owner/$Repo" -Headers $h -TimeoutSec 30
"login=$($me.login)  repo=$($rp.full_name)  private=$($rp.private)"

$files = if ($Mode -eq "min") {
    @("manifest.json", "manifest-v6.json", "talk/v6_talk_001.wav")
} else {
    Get-ChildItem -Path $Root -Recurse -File |
        Where-Object { $_.Extension -in ".wav", ".json", ".md" -and $_.Name -notlike "*.ps1" } |
        ForEach-Object { $_.FullName.Substring($Root.Length).TrimStart("\").Replace("\", "/") } |
        Sort-Object
}
"mode=$Mode  files=$($files.Count)"

$ok = 0; $fail = @(); $i = 0; $shaLocal = @{}
foreach ($rel in $files) {
    $i++
    $full = Join-Path $Root ($rel -replace "/", "\")
    if (-not (Test-Path $full)) { "MISS $rel"; $fail += $rel; continue }
    $shaLocal[$rel] = (Get-FileHash -Algorithm SHA256 -Path $full).Hash.ToLower()
    $b64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes($full))
    $old = $null
    try { $old = (Invoke-RestMethod -Uri "$api/$rel`?ref=$Branch" -Headers $h -TimeoutSec 30).sha } catch { $old = $null }
    $body = @{ message = "voice v6: $rel"; content = $b64; branch = $Branch }
    if ($old) { $body["sha"] = $old }
    $json = $body | ConvertTo-Json -Compress
    $done = $false
    for ($t = 1; $t -le 3 -and -not $done; $t++) {
        try {
            Invoke-RestMethod -Uri "$api/$rel" -Method Put -Headers $h -Body $json -ContentType "application/json; charset=utf-8" -TimeoutSec 180 | Out-Null
            $done = $true; $ok++
            if ($i % 20 -eq 0 -or $i -le 3 -or $i -eq $files.Count) { "[$i/$($files.Count)] $rel" }
        } catch {
            if ($t -eq 3) {
                $msg = if ($_.ErrorDetails) { $_.ErrorDetails.Message } else { $_.Exception.Message }
                $fail += "$rel :: $msg"
                "[$i] FAIL $rel"
            } else { Start-Sleep -Seconds (2 * $t) }
        }
    }
}
"OK=$ok  FAIL=$($fail.Count)"
$fail | Select-Object -First 3

if ($ok -gt 0) {
    "---- CDN 回读 ----"
    Start-Sleep -Seconds 3
    $mirrors = @("https://cdn.jsdmirror.com/gh/$Owner/$Repo@$Branch/", "https://jsd.onmicrosoft.cn/gh/$Owner/$Repo@$Branch/", "https://cdn.jsdelivr.net/gh/$Owner/$Repo@$Branch/")
    foreach ($m in $mirrors) {
        try {
            $doc = ((Invoke-WebRequest -Uri ($m + "manifest-v6.json") -TimeoutSec 25 -UseBasicParsing).Content) | ConvertFrom-Json
            "manifest: version=$($doc.version) clips=$($doc.clips.Count)"
            break
        } catch { "  $m 不可用" }
    }
}
