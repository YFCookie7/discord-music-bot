import discord
from discord.ext import commands
from cogs.commands.yt_dlp import (
    audio_dir,
    FFMPEG_PATH,
)
from os import listdir
from os.path import isfile, join


def list_music():
    audio_list = []
    files = [f for f in listdir(audio_dir) if isfile(join(audio_dir, f))]

    for file in files:
        audio_list.append(discord.SelectOption(label=file, description=""))

    return audio_list


class MusicMenu(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.select(
        placeholder="Song list",
        min_values=1,
        max_values=1,
        options=list_music(),
    )
    async def select_callback(self, select, interaction):
        if self.ctx.voice_client and self.ctx.voice_client.is_playing():
            self.ctx.voice_client.stop()
        await interaction.response.send_message(f"Playing {select.values[0]}")
        channel = self.ctx.author.voice.channel
        voice = self.ctx.voice_client or await channel.connect()
        voice.play(
            discord.FFmpegPCMAudio(
                executable=FFMPEG_PATH, source=audio_dir + select.values[0]
            )
        )


class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="List music")
    async def list(self, ctx):
        await ctx.send("Choose which music you want to play.", view=MusicMenu(ctx))


def setup(bot):
    bot.add_cog(List(bot))
