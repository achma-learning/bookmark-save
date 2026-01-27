import subprocess
import sys
import os

# ------------------------
# Function to check if a module is installed
# ------------------------
def install_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# ------------------------
# Ensure Flask is installed
# ------------------------
install_package("flask")

# ------------------------
# Launch the website
# ------------------------
print("Launching bookmark website...")

# Assume app.py is in the same folder
current_dir = os.path.dirname(os.path.abspath(__file__))
app_file = os.path.join(current_dir, "app.py")

if not os.path.exists(app_file):
    print(f"Error: {app_file} not found!")
    sys.exit(1)

# Launch Flask app
subprocess.run([sys.executable, app_file])
