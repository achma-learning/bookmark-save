import shutil
import os
from datetime import datetime

# Define paths to the Chrome profile bookmarks (use 'tool' as username)
chrome_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'
chrome_canary_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome SxS\User Data\Default\Bookmarks'

# Additional profile (example: "profile-chrome" and "profile-canary")
profile_chrome_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome\User Data\Profile 1\Bookmarks'  # Example for another profile
profile_canary_bookmarks_path = r'C:\Users\tool\AppData\Local\Google\Chrome SxS\User Data\Profile 1\Bookmarks'  # Example for another Canary profile

# Define the backup folder (where the bookmarks will be saved)
backup_folder = r'C:\Users\tool\chrome_bookmarks_backup\bookmark-save'

# Create a unique backup directory based on the current date
backup_dir = os.path.join(backup_folder, datetime.now().strftime('%Y-%m-%d'))
os.makedirs(backup_dir, exist_ok=True)

# Define timestamp for unique file names
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Define backup file names based on the profiles and timestamp
chrome_backup_filename = f'chrome_{timestamp}.json'
chrome_canary_backup_filename = f'chrome_canary_{timestamp}.json'
profile_chrome_backup_filename = f'profile-chrome_{timestamp}.json'
profile_canary_backup_filename = f'profile-canary_{timestamp}.json'

# Function to back up a profile's bookmarks if the file exists
def backup_bookmarks(profile_path, backup_filename):
    if os.path.exists(profile_path):
        shutil.copy(profile_path, os.path.join(backup_dir, backup_filename))
        print(f"Backup complete for {backup_filename}: {os.path.join(backup_dir, backup_filename)}")
    else:
        print(f"{backup_filename} bookmarks file not found!")

# Back up Chrome bookmarks
backup_bookmarks(chrome_bookmarks_path, chrome_backup_filename)

# Back up Chrome Canary bookmarks
backup_bookmarks(chrome_canary_bookmarks_path, chrome_canary_backup_filename)

# Back up additional Chrome profile bookmarks (Profile 1 as an example)
backup_bookmarks(profile_chrome_bookmarks_path, profile_chrome_backup_filename)

# Back up additional Canary profile bookmarks (Profile 1 as an example)
backup_bookmarks(profile_canary_bookmarks_path, profile_canary_backup_filename)
