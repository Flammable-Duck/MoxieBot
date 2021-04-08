from discord.ext import commands
from commands.rateme import rateuser
from commands.fortune import get_fortune

bot = commands.Bot(command_prefix='^')

@bot.command()
async def uwu(ctx):
    await ctx.send("owo")

@bot.command()
async def fortune(ctx):
    await ctx.send(get_fortune())

@bot.command()
async def r8me(ctx):
    #fucking arfe how the fucj do I get usernames fuck shit fuck
    # the string "test name" will be used until bubby or I fixes this, becuase i do want to make commit before i sleep
    await ctx.send(rateuser("test name"))