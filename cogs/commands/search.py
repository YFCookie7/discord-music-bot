import discord
from discord.ext import commands
import yt_dlp

class searchResults:
    def __init__(self, title, url, duration, thumbnail):
        self.title = title
        self.url = url
        self.duration = duration
        self.thumbnail = thumbnail

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Search youtube")
    async def search(self, ctx, yt_url: discord.Option(str, description="Search youtube", required = True)):
        await ctx.defer()

        if ctx.voice_client and ctx.voice_client.is_playing():
            print("qwe")

        
        result = []
        result.append(searchResults("qwe","qwe","qwe","qwe"))
        result.append(searchResults("qwe","qwe","qwe","qwe"))
        result.append(searchResults("qwe","qwe","qwe","qwe"))
        print(result[0].title)
        print(result[1].title)
        print(result[2].title)
    

def setup(bot):
    bot.add_cog(Search(bot))