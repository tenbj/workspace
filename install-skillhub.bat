@echo off
echo Installing SkillHub...
npm cache clean --force
npm install -g skillhub
echo.
echo Done. Press any key to close.
pause >nul
