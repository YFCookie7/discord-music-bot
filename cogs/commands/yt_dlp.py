import yt_dlp
import os
import json
import discord
from discord.ext import commands


audio_dir = "C:/Users/mikel/Documents/Github/discord-music-bot/audio/" 
audio_naming = f"%(title)s.%(ext)s"
json_file = "audio.json"
FFMPEG_PATH = "C:/ffmpeg/ffmpeg.exe"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
    'outtmpl': "/audio/"+audio_naming,   # ~/audio/abc.mp3
    "quiet": True,
}

def removelist(yt_url):
    return yt_url.split("&", 1)[0]

def get_audio(yt_url):
    # Check if the audio file already exists
    if os.path.exists(json_file) and os.stat(json_file).st_size > 0:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        for data in json_data:
            if data.get('yt_url') == yt_url:
                return data.get('audio_filename')
    return "not found"

def download_audio(yt_url):
    # Download the audio file if it does not exist
    print("Downloading: " + yt_url)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(yt_url, download=True)
        title = info['title']
        ext = "mp3"
        audio_file = ydl.prepare_filename(info)
        audio_filename = (f"{title}.{ext}")
        print("Downloaded: " + audio_filename)

    # Save the audio data to json
    data = {
        'audio_filename': audio_filename,
        'yt_url': yt_url
    }
    if os.path.exists(json_file) and os.stat(json_file).st_size > 0:
        with open(json_file, 'r+', encoding='utf-8') as f:
            json_data = json.load(f)
            json_data.append(data)
            f.seek(0)  # Move the file pointer to the beginning of the file
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            f.truncate()  # Truncate the file to remove any remaining content
    else:
        # Create a new JSON file with the data
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump([data], f, ensure_ascii=False, indent=4)
    return audio_filename

class YT_DLP(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(YT_DLP(bot))