import discord
import random
from discord.ext import commands

client = discord.Client
class Sarcasm(commands.Cog):

    def _init__(self, client):
        self.client = client

    @commands.command(aliases=['hey','HEY'])
    async def Hey(self, ctx, *, question):  # TALKING TO BOT via COMMANDS
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

    @commands.Cog.listener()
    async def on_message(self, message):
        keywords = ["sandwiches", "pizza", "food" ]
        #channel = discord.utils.get(client.guilds[10].channels, name="general")
        channel = message.channel
        for keyword in keywords:
            if keyword.lower() in message.content.lower():
                response = f"Did someone say {keyword.lower()}? Joeyy's hungry ! "
                await channel.send(response)

def setup(client):
    client.add_cog(Sarcasm(client))