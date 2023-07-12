import discord
from discord.ext import commands
import subprocess
from cogs.commands.yt_dlp import removelist, get_audio, download_audio, audio_dir, FFMPEG_PATH



class btn_play(discord.ui.View):

    def __init__(self, result, ctx):
        super().__init__()
        self.result = result
        self.ctx = ctx

    @discord.ui.button(label="Play!", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("OK")

        print(self.result.id) # YouTube video url
        if self.ctx.voice_client and self.ctx.voice_client.is_playing():
            self.ctx.voice_client.stop()
        
        audio_filename = get_audio(self.result.id)
        if audio_filename == "not found":
            await self.ctx.edit(content = "Downloading...")
            audio_filename = download_audio(self.result.id)

        channel = self.ctx.author.voice.channel
        voice = self.ctx.voice_client or await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source=audio_dir + audio_filename))


class searchResults:
    def __init__(self, title, id, thumbnail, duration):
        self.title = title
        self.id = id
        self.thumbnail = thumbnail
        self.duration = duration

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Search youtube")
    async def search(self, ctx, keyword: discord.Option(str, description="Search youtube", required = True)):
        await ctx.defer()

        command = [
            'yt-dlp',
            'ytsearch3:' + keyword,
            '--get-title',
            '--get-id',
            '--get-thumbnail',
            '--get-duration',
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip().split('\n')

        search_results = []
        for i in range (0,12,4):
            title = output[i]
            id = "https://www.youtube.com/watch?v=" + output[i+1]
            thumbnail = output[i+2]
            duration = output[i+3]
            search_results.append(searchResults(title, id, thumbnail, duration))
            
        await ctx.respond("Here's the search result of " + keyword)
        for i in range(0,3):            
            embed = discord.Embed(
                title = search_results[i].title,
                description= search_results[i].id,
                color = discord.Color.blurple(),
            )
            embed.add_field(name="Duration", value=search_results[i].duration, inline=True)
            embed.set_thumbnail(url=search_results[i].thumbnail)
            await ctx.respond(embed=embed, view=btn_play(search_results[i], ctx))


def setup(bot):
    bot.add_cog(Search(bot))

