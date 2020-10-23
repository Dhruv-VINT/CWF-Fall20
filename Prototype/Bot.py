import discord
import random
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!',intents = intents)

@client.event
async def on_ready(): # BOT IS ONLINE
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bamboozled'))
    print("Bot is ready")

@client.event
async def on_member_join(member):  # NOTIFY WHEN A MEMBER JOINS THE SERVER
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):  # NOTIFY WHEN A MEMBER LEAVES THE SERVER
    print(f"{member} has left a server. ")

@client.command(aliases=['hey','HEY'])
async def Hey(ctx, *, question):    # TALKING TO BOT via COMMANDS
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
async def clear(ctx, amount=5):   # CLEAR RECENT MESSAGES ON THE CHANNEL
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):  # KICK A MEMBER
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):  # BAN A MEMBER FROM SERVER
    await member.ban(reason=reason)
    await ctx.command(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):  # UNBAN THE BANNED MEMBER
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



client.run('NzY2MDM4MzQ3MDQ2MDYwMDYy.X4dizg.AQdhFoD0aOchi5eX3scTxAAXMuc')
