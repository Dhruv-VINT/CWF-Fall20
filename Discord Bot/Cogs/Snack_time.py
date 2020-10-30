import discord
from discord.ext import commands

class Snack_time(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listnener()
    while(True):
        await bot.wait_until_ready()
        online_members = []
        for member in bot.get_all_members():
            if member.status != discord.Status.offline and member.id != bot.user.id:
                online_members.append(member.id)
        if len(online_members) > 0:
            user = random.choice(online_members)
            current_time = imt(datetime.datetime.now().strftime(%I))
            channel = discord.utils.get(bot.guilds[0].channels, name = "general")
            message = f"It's {current_time} o'clock! Time for some food, Aren't you starving ?! <@{user}"
            await channel.send(message)
        await asyncio.sleep(3600)

client.loop.create_task(Snack_time())

def setup(client):
    client.add_cog(Snack_time(client))
