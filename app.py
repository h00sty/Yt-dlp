from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/subtitles/{video_id}")
def get_subtitles(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "ru"],
        "subtitlesformat": "vtt",
        "cookiefile": "youtube_cookies.txt"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "id": info.get("id"),
            "subtitles": info.get("subtitles"),
            "automatic_captions": info.get("automatic_captions"),
        }


