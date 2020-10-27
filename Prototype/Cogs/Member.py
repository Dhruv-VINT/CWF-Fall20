import discord
from discord.ext import commands

class Member(commands.Cog):

    def _init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):  # NOTIFY WHEN A MEMBER JOINS THE SERVER
        print(f"{member} has joined a server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):  # NOTIFY WHEN A MEMBER LEAVES THE SERVER
        print(f"{member} has left a server. ")

def setup(client):
    client.add_cog(Member(client))



