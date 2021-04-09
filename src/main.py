#!/bin/python3
from discord.ext import commands
#import discord.user
import cmds.config
from cmds.fortune import *
from cmds.rateme import *

# All commands need to go through the bot that gets run()
bot = commands.Bot(command_prefix='^')

cmds.config.init()

@bot.event
async def on_ready():
    print("MoxieBot, ©2021 BubbyRoosh and Flammable_Duck")

@bot.command()
async def uwu(ctx):
    "owo"
    await ctx.send("owo")

@bot.command()
async def fortune(ctx):
    "Broken \\n lol"
    await ctx.send(get_fortune())

@bot.command()
async def r8me(ctx):
    "Let a random number decide how good you are"
    await ctx.send(rateuser(ctx.message.author.mention))

@bot.group()
async def config(ctx):
    "Some config commands and stuff"
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid config command")

@config.command()
async def list(ctx):
    "List all configs, their descriptions, and their current values"
    await cmds.config.list_configs(ctx)

@config.command()
async def set(ctx):
    "Set a config value"
    name = ctx.message.content.split()[2]
    value = ctx.message.content.split()[3]
    print(f"{name} {value}")
    if value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False
    await cmds.config.set_value(ctx, name, value)

# yes there are safer ways to do this
# I just don't care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
