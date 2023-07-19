import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", help_command=None, intents=intents)

conn = sqlite3.connect("audio.db")
c = conn.cursor()
c.execute(
    """
    CREATE TABLE IF NOT EXISTS audio (
        audio_filename TEXT NOT NULL,
        yt_url TEXT NOT NULL,
        duration TEXT NOT NULL,
        uploader TEXT NOT NULL
    )
"""
)
conn.commit()
c.close()
conn.close()

for foldername in os.listdir("./cogs"):
    for filename in os.listdir(f"./cogs/{foldername}"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{foldername}.{filename[:-3]}")

bot.run(DISCORD_TOKEN)
