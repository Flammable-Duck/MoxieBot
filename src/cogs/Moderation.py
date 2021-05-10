"""
All moderation commands
"""
import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions


class Moderation(commands.Cog):
    """
    Moderation commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        """
        kick a user from the server
        $kick <user> <reason>
        user: The user
          reason: The reason they were kicked
        """
        if not reason:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked for **no reason submitted**.")
        else:
            await user.kick(reason=reason)
            await ctx.send(f"**{user}** has been kicked for **{reason}**.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        """
        ban a user from the server
        $ban <user> <reason>
        user: The user
        reason: The reason they were kicked
        """
        if not reason:
            await user.ban()
            await ctx.send(f"**{user}** has been banned for **no reason submitted**.")
            await user.send(f"You has been banned from **{ctx.message.guild.name}**.")
        else:
            await user.ban(reason=reason)
            await ctx.send(f"**{user}** has been banned. \nReason: *{reason}*.")
            await user.send(f"You has been banned from **{ctx.message.guild.name}** \n**Reason:** *{reason}*.")

    @commands.command(name='unban')
    async def _unban(self, ctx, uid):
        """
        unban a user from the server
        $unban <user>
        user: The user
        reason: The reason they were kicked
        """
        user = await self.bot.fetch_user(uid)
        await ctx.guild.unban(user)
        await ctx.send(f"**{user}** has been unbanned.")
        await user.send(f"You has been unbanned from **{ctx.message.guild.name}**.")


def setup(bot):
    bot.add_cog(Moderation(bot))
