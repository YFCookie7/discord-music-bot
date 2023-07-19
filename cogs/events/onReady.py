from discord.ext import tasks, commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as {0.user}".format(self.bot))
        print(f"{self.bot.user.name} is now online!")


def setup(bot):
    bot.add_cog(Ready(bot))
