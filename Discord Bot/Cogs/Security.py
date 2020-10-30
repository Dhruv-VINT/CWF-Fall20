import discord
from discord.ext import commands

class Security(commands.Cog):

    def _init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):  # KICK A MEMBER
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):  # BAN A MEMBER FROM SERVER
        await member.ban(reason=reason)
        await ctx.command(f'Banned {member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):  # UNBAN THE BANNED MEMBER
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(Security(client))