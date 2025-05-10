#!/usr/bin/zsh

SCRIPT_PATH=$(cd "$(dirname "$0")" && pwd)
cd "$SCRIPT_PATH" || { echo "cd failed"; exit 1 }

DATE=$(date +%Y-%m-%d)

git status
git add .
git commit -m "$DATE"

