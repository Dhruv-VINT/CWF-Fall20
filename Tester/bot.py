import discord
import os
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!')



@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run('')