import subprocess
import sys
import shutil

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)

def command_exists(cmd):
    return shutil.which(cmd) is not None

if sys.version_info < (3, 8):
    print("Python 3.8+ required")
    sys.exit(1)

print("Python OK")

if not command_exists("pip3"):
    print("Installing pip...")
    run(["sudo", "dnf", "install", "-y", "python3-pip"])
else:
    print("pip OK")

if not command_exists("ffmpeg"):
    print("Installing ffmpeg...")
    run(["sudo", "dnf", "install", "-y", "ffmpeg"])
else:
    print("ffmpeg OK")

print("Installing yt-dlp...")
run([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])

print("\nyt-dlp setup complete!")
print("Test with: yt-dlp --version")
