import yt_dlp
import os
import json
from discord.ext import commands
import re
import sqlite3

audio_dir = "./audio/"
FFMPEG_PATH = "C:/ffmpeg/ffmpeg.exe"

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "256",
        }
    ],
    "outtmpl": "/audio/%(title)s.%(ext)s",  # ~/audio/abc.mp3  audio_naming = f"%(title)s.%(ext)s"
    "quiet": True,
}


# Remove or replace special characters
def sanitize_filename(filename):
    sanitized = re.sub(r'[\\/:"*?<>|]', "", filename)
    return sanitized


# Remove the list parameter from the youtube url
def removelist(yt_url):
    return yt_url.split("&", 1)[0]


# Check if the audio file already exists
def get_audio(yt_url):
    conn = sqlite3.connect("audio.db")
    c = conn.cursor()

    c.execute("SELECT * FROM audio WHERE yt_url = ?", (yt_url,))
    result = c.fetchone()
    if result:
        audio_filename, yt_url, duration, uploader = result
        c.close()
        conn.close()
        return audio_filename
    else:
        c.close()
        conn.close()
        return "not found"


# Download the audio file
def download_audio(yt_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(yt_url, download=False)
        ydl.prepare_filename(info)
        audio_filename = info["title"]

    minutes, seconds = divmod(info["duration"], 60)

    audio_filename = sanitize_filename(audio_filename)
    ydl_opts["outtmpl"] = "/audio/" + audio_filename

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(yt_url, download=True)
        audio_filename = audio_filename + ".mp3"

    data = {
        "audio_filename": audio_filename,
        "yt_url": yt_url,
        "duration": f"{minutes:02d}:{seconds:02d}",
        "uploader": info["uploader"],
    }

    conn = sqlite3.connect("audio.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO audio (audio_filename, yt_url, duration, uploader)
        VALUES (?, ?, ?, ?)
    """,
        (data["audio_filename"], data["yt_url"], data["duration"], data["uploader"]),
    )
    conn.commit()
    c.close()
    conn.close()

    return audio_filename


class YT_DLP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(YT_DLP(bot))
