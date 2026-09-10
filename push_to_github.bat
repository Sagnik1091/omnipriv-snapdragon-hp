@echo off
echo =======================================================
echo   OmniPriv - Instant GitHub Deployment Script
echo =======================================================
echo.
set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/user/omnipriv.git): "

if "%REPO_URL%"=="" (
    echo Error: Repository URL cannot be empty!
    pause
    exit /b
)

echo.
echo [1/4] Initializing Git...
git init
git branch -M main

echo [2/4] Staging project files...
git add .

echo [3/4] Creating initial commit...
git commit -m "Initial commit: OmniPriv for Snapdragon-Powered HP PCs"

echo [4/4] Setting remote and pushing to main branch...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git push -u origin main

echo.
echo =======================================================
echo   Done! Your repository is now live on GitHub.
echo =======================================================
pause
