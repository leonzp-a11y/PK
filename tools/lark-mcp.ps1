param(
  [string[]]$ExtraArgs
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($env:LARK_APP_ID)) {
  Write-Error "Missing environment variable LARK_APP_ID. Set it to your Feishu/Lark app_id before starting Codex."
  exit 1
}

if ([string]::IsNullOrWhiteSpace($env:LARK_APP_SECRET)) {
  Write-Error "Missing environment variable LARK_APP_SECRET. Set it to your Feishu/Lark app_secret before starting Codex."
  exit 1
}

$npx = (Get-Command npx.cmd -ErrorAction SilentlyContinue)
if (-not $npx) {
  $npx = (Get-Command npx -ErrorAction SilentlyContinue)
}
if (-not $npx) {
  Write-Error "npx was not found on PATH. Install Node.js or add npx to PATH."
  exit 1
}

$argsList = @(
  "-y",
  "@larksuiteoapi/lark-mcp",
  "mcp",
  "-a",
  $env:LARK_APP_ID,
  "-s",
  $env:LARK_APP_SECRET,
  "-l",
  "zh",
  "--oauth",
  "--token-mode",
  "user_access_token"
)

if ($ExtraArgs) {
  $argsList += $ExtraArgs
}

& $npx.Source @argsList
exit $LASTEXITCODE
