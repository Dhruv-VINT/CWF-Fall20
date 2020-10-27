import discord
import os
import random
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!',intents = intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bamboozled'))
    print("Bot is ready")


extensions = ['Cogs.Member', 'Cogs.Sarcasm','Cogs.Clear_Message','Cogs.Security']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run('******************************************')
