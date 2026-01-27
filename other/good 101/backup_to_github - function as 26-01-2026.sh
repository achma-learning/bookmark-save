#!/bin/bash

# Define the backup directory (C:\Users\tool\chrome_bookmarks_backup)
BACKUP_DIR="C:/Users/tool/chrome_bookmarks_backup"
REPO_DIR="C:/Users/tool/chrome_bookmarks_backup/bookmark-save"  # Correct path to the cloned GitHub repo


# Navigate to the Git repository
cd $REPO_DIR

# Pull the latest changes from GitHub
git pull origin main

# Copy the backup files from the backup directory to the repo directory
cp $BACKUP_DIR/* $REPO_DIR/

# Add and commit changes
git add .
git commit -m "Backup Chrome and Chrome Canary Bookmarks: $(date +'%Y-%m-%d %H:%M:%S')"

# Push the changes to GitHub
git push origin main

echo "Backup uploaded to GitHub."
