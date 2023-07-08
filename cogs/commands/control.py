import discord
from discord.ext import commands

class Control(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Tutorial for interacting with music bot")
    async def help(self ,ctx):
        await ctx.defer()
        await ctx.respond("no help")

    @discord.slash_command(description="Add the bot to voice channel")
    async def join(self ,ctx):
        await ctx.defer()
        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.respond("Bot is now in voice channel")
        else:
            await ctx.respond("You have to join the voice channel first")

    @discord.slash_command(description="Pause music")
    async def pause(self, ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.respond("Playback paused.")
        else:
            await ctx.respond("No audio is currently playing.")

    @discord.slash_command(description="Resume music")
    async def resume(self, ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.respond("Playback resumed.")
        else:
            await ctx.respond("Audio is not currently paused.")
            
    @discord.slash_command(description="Stop music")
    async def stop(self ,ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            self.ctx = None
        else:
            await ctx.respond("No audio is currently playing.")

    @discord.slash_command(description="Remove the bot from voice channel")
    async def quit(self ,ctx):
        if ctx.voice_client is not None:
            await ctx.defer()
            await ctx.voice_client.disconnect()
        await ctx.respond("Bot has left the voice channel")
    

def setup(bot):
    bot.add_cog(Control(bot))