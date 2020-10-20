import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready")

client.run('NzY2MDM4MzQ3MDQ2MDYwMDYy.X4dizg.U2Sj3b6A5pvRsGH9T0XHrN-4IEA')

