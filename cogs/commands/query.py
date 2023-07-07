import discord
from discord.ext import commands
import yt_dlp

class Query(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Search youtube")
    async def query(self, ctx, yt_url: discord.Option(str, description="Search youtube", required = True)):
        await ctx.defer()

    

def setup(bot):
    bot.add_cog(Query(bot))