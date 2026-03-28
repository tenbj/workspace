# SkillHub Installation Script
Write-Host "Installing SkillHub..."

# Download tar.gz
$tarUrl = "https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/latest.tar.gz"
$tarPath = "$env:TEMP\skillhub.tar.gz"
$extractPath = "$env:TEMP\skillhub"

Write-Host "Downloading..."
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$webClient = New-Object System.Net.WebClient
$webClient.DownloadFile($tarUrl, $tarPath)

Write-Host "Extracting..."
# Use tar command (available in Windows 10+)
tar -xzf $tarPath -C $env:TEMP

# Find and run installer
$installScript = Get-ChildItem -Path $extractPath -Filter "install.sh" -Recurse | Select-Object -First 1
if ($installScript) {
    Write-Host "Running installer..."
    # Need bash for this
    bash $installScript.FullName
} else {
    Write-Host "No install.sh found, checking for Windows installer..."
    # Check for npm package
    npm install -g skillhub
}

Write-Host "Done."
