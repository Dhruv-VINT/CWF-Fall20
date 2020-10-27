import discord
from discord.ext import commands

class Clear_Message(commands.Cog):

    def _init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=5):  # CLEAR RECENT MESSAGES ON THE CHANNEL
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Clear_Message(client))