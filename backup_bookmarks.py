import shutil
import os
from datetime import datetime

# ------------------------
# Profile paths (update as needed)
# ------------------------
chrome_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'
chrome_canary_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome SxS\User Data\Default\Bookmarks'

# Additional profiles (examples)
profile_chrome_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome\User Data\Profile 1\Bookmarks'
profile_canary_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome SxS\User Data\Profile 1\Bookmarks'

# ------------------------
# Backup folders
# ------------------------
plain_backup_root = r'C:\Users\tool\chrome_bookmarks_backup\bookmark-save\exports'
commit_backup_folder = r'C:\Users\tool\chrome_bookmarks_backup\bookmark-save\commit-export+'

# Create commit-export+ folder if it doesn't exist
os.makedirs(commit_backup_folder, exist_ok=True)

# ------------------------
# Timestamp and date
# ------------------------
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
run_date = datetime.now().strftime('%d-%m-%Y')  # For plain backup folder name

# Create a folder for this run inside exports
plain_backup_folder = os.path.join(plain_backup_root, run_date)
os.makedirs(plain_backup_folder, exist_ok=True)

# ------------------------
# Function to back up bookmarks
# ------------------------
def backup_bookmarks(profile_path, profile_name):
    if os.path.exists(profile_path):
        # 1️⃣ Plain backup (unique folder per run)
        plain_filename = f'{profile_name}_{timestamp}.json'
        shutil.copy(profile_path, os.path.join(plain_backup_folder, plain_filename))
        print(f"Plain backup complete: {plain_filename} in {plain_backup_folder}")

        # 2️⃣ Commit backup (overwrite/update file)
        commit_filename = f'{profile_name}.json'
        shutil.copy(profile_path, os.path.join(commit_backup_folder, commit_filename))
        print(f"Commit backup updated: {commit_filename} in {commit_backup_folder}")
    else:
        print(f"{profile_name} bookmarks file not found!")

# ------------------------
# Backup all profiles
# ------------------------
backup_bookmarks(chrome_bookmarks_path, 'chrome')
backup_bookmarks(chrome_canary_bookmarks_path, 'chrome_canary')
backup_bookmarks(profile_chrome_bookmarks_path, 'profile-chrome')
backup_bookmarks(profile_canary_bookmarks_path, 'profile-canary')
