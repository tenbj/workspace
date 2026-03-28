$ErrorActionPreference = "Continue"
$dest = "D:\Program Files\QClaw\resources\openclaw\node_modules\openclaw"
$cacheDir = "D:\temp\npm-cache"
[void][System.IO.Directory]::CreateDirectory($cacheDir)
Write-Host "Cache dir: $cacheDir"
npm install sharp --save --prefix $dest --cache $cacheDir --prefer-offline 2>&1
Write-Host "Exit code: $LASTEXITCODE"
