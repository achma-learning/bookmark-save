#!/bin/bash

# ------------------------
# Paths
# ------------------------
# Local GitHub repository
REPO_DIR="C:/Users/tool/chrome_bookmarks_backup/bookmark-save"

# Folder containing the commit-ready backups
COMMIT_BACKUP_DIR="$REPO_DIR/commit-export+"

# ------------------------
# Navigate to GitHub repository
# ------------------------
cd "$REPO_DIR" || { echo "Repo directory not found!"; exit 1; }

# ------------------------
# Pull latest changes to avoid conflicts
# ------------------------
git pull origin main

# ------------------------
# Copy commit-ready bookmarks into repo folder (overwrite existing)
# ------------------------
cp -r "$COMMIT_BACKUP_DIR"/* "$REPO_DIR"/

# ------------------------
# Stage changes
# ------------------------
git add .

# ------------------------
# Commit changes if there are any
# ------------------------
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
else
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    git commit -m "Update commit-export+ bookmarks: $TIMESTAMP"
    echo "Committed changes."
fi

# ------------------------
# Push to GitHub
# ------------------------
git push origin main
echo "Push complete."
