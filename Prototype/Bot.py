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


extensions = ['Cogs.Member', 'Cogs.Sarcasm','Cogs.Clear_Message']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


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



client.run('NzY2MDM4MzQ3MDQ2MDYwMDYy.X4dizg.u7fZn6sl1u0lDLWxKfWgaNia2nM')
