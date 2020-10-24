import discord
import random
from discord.ext import commands

class Example1(commands.Cog):
    def __init__(self,client):
        self.client = client

        @commands.command()
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




def setup(client):
    client.add_cog(Example1(client))