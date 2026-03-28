$ErrorActionPreference = "Stop"
$dest = "D:\Program Files\QClaw\resources\openclaw\node_modules\openclaw"
Write-Host "Installing sharp in: $dest"
npm install sharp --save --prefix $dest 2>&1
Write-Host "Done. Exit code: $LASTEXITCODE"
