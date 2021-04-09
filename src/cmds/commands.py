from discord.ext import commands

# This is seen as a different bot from the main.py one
# bot = commands.Bot(command_prefix='^')

@bot.command()
async def uwu(ctx):
    await ctx.send("owo")

@bot.command()
async def fortune(ctx):
    await ctx.send(fortune.get_fortune())

@bot.command()
async def r8me(ctx):
    #fucking arfe how the fucj do I get usernames fuck shit fuck
    # the string "test name" will be used until bubby or I fixes this, becuase i do want to make commit before i sleep
    await ctx.send(fortune.rateuser("test name"))
