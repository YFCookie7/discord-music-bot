import asyncio
import discord
from discord.ext import commands
import yt_dlp
import os

MP3_PATH = "C:/Users/mikel/Documents/Github/discord-music-bot/"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
}

class Chat(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Tutorial for interacting with music bot")
    async def help(self ,ctx):
        await ctx.defer()
        await ctx.respond("hello")


    @discord.slash_command(description="Add the bot to voice channel")
    async def join(self ,ctx):
        await ctx.defer()
        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.respond("Bot is now in voice channel")
        else:
            await ctx.respond("You have to join the voice channel first")
            

    @discord.slash_command(description="Remove the bot from voice channel")
    async def quit(self ,ctx):
        if ctx.voice_client is not None:
            await ctx.defer()
            await ctx.voice_client.disconnect()
        await ctx.respond("Bot has left the voice channel")


    @discord.slash_command(description="Play music")
    async def play(self, ctx):
        # Check if the bot is already connected to a voice channel
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        # video_url = 'https://www.youtube.com/watch?v=GZ6DpXiQhms'
        # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #     info = ydl.extract_info(video_url, download=True)
        #     audio_filename = ydl.prepare_filename(info)
        # audio_filename = audio_filename[:-5] + ".mp3"

        audio_filename = "League of Legends, PVRIS - Burn It All Down (Lyrics) [GZ6DpXiQhms].mp3"
        channel = ctx.author.voice.channel
        voice = ctx.voice_client or await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe", source=MP3_PATH + audio_filename))



    @discord.slash_command(description="Stop music")
    async def stop(self ,ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            self.ctx = None
        else:
            await ctx.send("No audio is currently playing.")


    @discord.slash_command(description="Pause music")
    async def pause(self, ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Playback paused.")
        else:
            await ctx.send("No audio is currently playing.")

    @discord.slash_command(description="Resume music")
    async def resume(self, ctx):
        if ctx.voice_client is not None and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Playback resumed.")
        else:
            await ctx.send("Audio is not currently paused.")
    
        
        


    # @discord.slash_command(name="prompt", description="Predefine bot's behavior")
    # async def prompt(self,
    #     ctx,
    #     prompt: discord.Option(discord.SlashCommandOptionType.string)
    # ):
    #     await update_prompt(prompt)
    #     await ctx.respond(f"New prompt: `{prompt}`.")


    # @discord.slash_command(description="Erase Conversation Memory")
    # async def erase(self, ctx):
    #     await ctx.defer()
    #     await erase()
    #     await ctx.respond(f"{ctx.author.mention}, ChatBot memory erased!")


    # async def get_ai_model(ctx: discord.AutocompleteContext):
    #     return ["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"]

    # @discord.slash_command(name="model", description="Select AI Model")
    # async def model_command( self,
    # ctx: discord.ApplicationContext,
    # ai_model: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_ai_model), description="Select AI Model", required = False, default = '')
    # ):
    #     await ctx.defer()
    #     with open('config.json', "r+") as f:
    #         data = json.load(f)

            
    #         if (ai_model!=''):
    #             data['default_model'] = ai_model
    #             f.seek(0)
    #             json.dump(data, f, indent=4)
    #             f.truncate()
    #             await ctx.respond(f'{ctx.author.mention}, Chatbot model is switched to `{ai_model}`!')
    #             return
    #         curr_model=data['default_model']
    #         await ctx.respond(f'{ctx.author.mention}, The current chatbot model is `{curr_model}`!')


    

def setup(bot):
    bot.add_cog(Chat(bot))