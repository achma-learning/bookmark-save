import subprocess
import sys
import os

# Ensure Flask is installed
def install_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

install_package("flask")

# Launch the website
print("Launching bookmark website...")
current_dir = os.path.dirname(os.path.abspath(__file__))
app_file = os.path.join(current_dir, "app.py")

if not os.path.exists(app_file):
    print(f"Error: {app_file} not found!")
    sys.exit(1)

subprocess.run([sys.executable, app_file])
