import sys
import subprocess
import shutil
import os
import zipfile
import urllib.request

FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_DIR = os.path.join(os.getenv("LOCALAPPDATA"), "ffmpeg")

def run(cmd):
    print("Running:", " ".join(cmd))
    subprocess.check_call(cmd, shell=True)

def exists(cmd):
    return shutil.which(cmd) is not None

if sys.version_info < (3, 8):
    print("Python 3.8+ required")
    sys.exit(1)

print("Python OK")

if not exists("pip"):
    print("pip not found. Reinstall Python and enable 'Add Python to PATH'")
    sys.exit(1)

print("pip OK")

print("Installing yt-dlp...")
run([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])

if not exists("ffmpeg"):
    print("Downloading FFmpeg...")
    os.makedirs(FFMPEG_DIR, exist_ok=True)

    zip_path = os.path.join(FFMPEG_DIR, "ffmpeg.zip")
    urllib.request.urlretrieve(FFMPEG_URL, zip_path)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(FFMPEG_DIR)

    extracted = next(
        d for d in os.listdir(FFMPEG_DIR)
        if d.startswith("ffmpeg-") and os.path.isdir(os.path.join(FFMPEG_DIR, d))
    )

    bin_path = os.path.join(FFMPEG_DIR, extracted, "bin")

    os.environ["PATH"] += os.pathsep + bin_path
    run(["setx", "PATH", os.environ["PATH"]])

    print("FFmpeg installed and added to PATH")
else:
    print("FFmpeg already available")

print("\nSetup complete!")
print("Restart terminal, then test with:")
print("yt-dlp --version")
