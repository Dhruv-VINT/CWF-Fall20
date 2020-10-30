import discord
import os
import random
from discord.ext import commands

bot = discord.Client()
class Reminder(commands.Cog):

    def _init__(self, client):
        self.client = client

    


def setup(client):
    client.add_cog(Reminder(client))