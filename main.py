import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sqlite3

# load .env
load_dotenv() 
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', help_command=None, intents=intents) 

conn = sqlite3.connect('audio.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS audio (
        audio_filename TEXT NOT NULL,
        yt_url TEXT NOT NULL,
        duration TEXT NOT NULL,
        uploader TEXT NOT NULL
    )
''')
conn.commit()
c.close()
conn.close()

# Load events, commands
for foldername in os.listdir('./cogs'): #for every folder in cogs
    for filename in os.listdir(f'./cogs/{foldername}'):# for every file in a folder in cogs
        if filename.endswith('.py') and not filename in ['util.py', 'error.py']: #if the file is a python file and if the file is a cog
            bot.load_extension(f'cogs.{foldername}.{filename[:-3]}')#load the extension

# Launch bot
bot.run(DISCORD_TOKEN)
