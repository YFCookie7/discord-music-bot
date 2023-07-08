import discord
from discord.ext import commands
from cogs.commands.yt_dlp import removelist, get_audio, download_audio, audio_dir, FFMPEG_PATH


class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Play music")
    async def play(self, ctx, yt_url: discord.Option(str, description="Input youtube URL", required = True)):
        await ctx.respond("Loading...")
        # Stop the current audio if it is playing
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        yt_url=removelist(yt_url)
        audio_filename = get_audio(yt_url)
        if audio_filename == "not found":
            await ctx.edit(content = "Downloading...")
            audio_filename = download_audio(yt_url)

        channel = ctx.author.voice.channel
        voice = ctx.voice_client or await channel.connect()
        # await ctx.edit(content = "Now playing: " + audio_filename)
        voice.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source=audio_dir + audio_filename))

    
def setup(bot):
    bot.add_cog(Play(bot))
