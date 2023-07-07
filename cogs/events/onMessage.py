from discord.ext import commands

class Message(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        # if message.channel.id == 1099680104688394250:
        #     channel = self.bot.get_channel(729915471113224225)
        #     await channel.send(message.content)

def setup(bot):
    bot.add_cog(Message(bot))