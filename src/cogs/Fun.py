from functions.fortune import get_fortune
from functions.rateme import rateuser

import discord
from discord.ext import commands

class Fun(commands.Cog):
    """Fun commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="1984")
    async def _1984(self, ctx):
        "literally 1984"
        await ctx.send("""
        ```
        ⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣾⣟⠳⢦⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠉⠉⠉⠉⠉⠒⣲⡄⠀
        ⠀⠀⠀⠀⠀⣿⣿⣿⡇⡇⡱⠲⢤⣀⠀⠀⠀⢸⠀⠀⠀1984⠀⣠⠴⠊⢹⠁
        ⠀⠀⠀⠀⠀⠘⢻⠓⠀⠉⣥⣀⣠⠞⠀⠀⠀⢸⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⢸⠀⠀
        ⠀⠀⠀⠀⢀⣀⡾⣄⠀⠀⢳⠀⠀⠀⠀⠀⠀⢸⢠⡄⢀⡴⠁⠀     ⡞⠀
        ⠀⠀⠀⣠⢎⡉⢦⡀⠀⠀⡸⠀⠀⠀⠀⠀⢀⡼⣣⠧⡼⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀
        ⠀⢀⡔⠁⠀⠙⠢⢭⣢⡚⢣⠀⠀⠀⠀⠀⢀⣇⠁⢸⠁⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀
        ⠀⡞⠀⠀⠀⠀⠀⠀⠈⢫⡉⠀⠀⠀⠀⢠⢮⠈⡦⠋⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀
        ⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⣀⡴⠃⠀⡷⡇⢀⡴⠋⠉⠉⠙⠓⠒⠃⠀⠀⠀
        ⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⡼⠀⣷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⡞⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢧⠀⠀⠀⠀⠀⠀⠀⠈⠣⣀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ```""")

    @commands.command()
    async def uwu(self, ctx):
        "owo"
        await ctx.send("owo")

    @commands.command()
    async def fortune(self, ctx):
        "The classic fortune command"
        await ctx.send(get_fortune())

    @commands.command()
    async def r8me(self, ctx):
        "Let Moxie rate you!"
        await ctx.send(rateuser(ctx.message.author.mention))

def setup(bot):
    bot.add_cog(Fun(bot))
