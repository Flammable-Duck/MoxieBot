#!/bin/python3
from discord.ext import commands
#import discord.user
from cmds.fortune import *
from cmds.rateme import *

# All commands need to go through the bot that gets run()
bot = commands.Bot(command_prefix='^')

@bot.event
async def on_ready():
    print("MoxieBot, ©2021 BubbyRoosh and Flammable_Duck")

@bot.command()
async def uwu(ctx):
    await ctx.send("owo")

@bot.command()
async def fortune(ctx):
    await ctx.send(get_fortune())

@bot.command()
async def r8me(ctx):
    await ctx.send(rateuser(ctx.message.author.mention))


# yes there are safer ways to do this
# I just don't care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
