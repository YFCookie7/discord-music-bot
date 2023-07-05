import discord
from discord.ext import tasks, commands
from discord import Activity, ActivityType
import random
import json
import asyncio

class Ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot   

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.bot))
        print(f"{self.bot.user.name} is now online!")
        # task = asyncio.create_task(self.random_activity())

    # async def random_activity(self):
    #     while True:
            
    #         with open('config.json', "r") as f:
    #             data = json.load(f)
    #         activity_type = random.randint(0, 3)
    #         activity_name=random.choice(data['activity'][activity_type])
            
    #         if(activity_type==0):
    #             # await self.bot.change_presence(activity=discord.Game(activity_name))
    #             await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=activity_name))
    #         elif (activity_type==1):
    #             await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_name))
    #         elif (activity_type==2):
    #             await self.bot.change_presence(activity=discord.Activity(name=activity_name, type=discord.ActivityType.streaming, url='https://www.NintendoSucks.com'))
    #         else:
    #             await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_name))           

    #         await asyncio.sleep(1800)


def setup(bot):
    bot.add_cog(Ready(bot))