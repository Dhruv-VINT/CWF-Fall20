import discord
import random
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!',intents = intents)

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server. ")

@client.command(aliases=['hey','HEY'])
async def Hey(ctx, *, question):
    responses = ['These are just feelings. They’ll go away.',
                 'You can’t just give up! Is that what a dinosaur would do?',
                 'I’m curvy and I like it.',
                 'Joey doesn’t share food!',
                 'I don’t like it when people take food off my plate, okay?',
                 'Hey, how you doin ?'
                 'What am I gonna do? Keep trying to get rid of these feelings.',
                 'Now, let’s go, baby. It’s food time. Bring it, bitch.',
                 'Everything’s fine, it’s just a little crush.']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

client.run('')

