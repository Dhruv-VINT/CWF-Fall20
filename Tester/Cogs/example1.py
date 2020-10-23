import discord
from discord.ext import commands

class Example1(commands.Cog):
    def __init__(self,client):
        self.client = client

    # EVENTS
    @commands.Cog.listener()
    async def on_member_join(member, self):  # NOTIFY WHEN A MEMBER JOINS THE SERVER
        print(f"{member} has joined a server.")

    @commands.Cog.listener()
    async def on_member_remove(member, self):  # NOTIFY WHEN A MEMBER LEAVES THE SERVER
        print(f"{member} has left a server. ")


def setup(client):
    client.add_cog(Example1(client))