#!/bin/bash
echo "======================================================="
echo "  OmniPriv - Instant GitHub Deployment Script"
echo "======================================================="
echo ""
read -p "Enter your GitHub Repository URL (e.g. https://github.com/user/omnipriv.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "Error: Repository URL cannot be empty!"
    exit 1
fi

echo ""
echo "[1/4] Initializing Git..."
git init
git branch -M main

echo "[2/4] Staging files..."
git add .

echo "[3/4] Creating commit..."
git commit -m "Initial commit: OmniPriv for Snapdragon-Powered HP PCs"

echo "[4/4] Pushing to GitHub..."
git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"
git push -u origin main

echo ""
echo "Done! Your repository is now live on GitHub."
