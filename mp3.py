import yt_dlp
import os

SAVE_FOLDER = "C:/Users/geren/Documents/YouTube_downloader/Downloads"
os.makedirs(SAVE_FOLDER, exist_ok=True)

print("Paste YouTube video or playlist URLs (empty line to start download):")

urls = []
while True:
    url = input().strip()
    if not url:
        break
    urls.append(url)

if not urls:
    print("No URLs given.")
    exit()

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": {
        "default": f"{SAVE_FOLDER}/%(title)s.%(ext)s",
        "playlist": f"{SAVE_FOLDER}/%(playlist_title)s/%(title)s.%(ext)s",
    },
    "noplaylist": False,
    "ignoreerrors": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

print("Done!")
