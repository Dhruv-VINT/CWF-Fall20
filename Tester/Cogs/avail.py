import discord
from discord.ext import commands

class Avail(commands.Cog):
    def __init__(self,client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready(self):  # BOT IS ONLINE
            print("Bot is ready")

def setup(client):
    client.add_cog(Avail(client))