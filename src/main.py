#!/bin/python3
import cmds.config
from cmds.fortune import *
from cmds.rateme import *

from discord.ext import commands

import random

import redditapi

print("starting...")

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
    "The classic fortune command"
    await ctx.send(get_fortune())

@bot.command()
async def r8me(ctx):
    "Let Moxie rate you!"
    await ctx.send(rateuser(ctx.message.author.mention))

@bot.group()
async def config(ctx):
    "Moxie settings"
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid config command")

@config.command()
async def list(ctx):
    "List all settings"
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

@bot.group()
async def reddit(ctx):
    "Reddit neckbeard fedora hat"
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid reddit command")

@reddit.command()
async def hot(ctx):
    "See a random hot post in a subreddit"
    posts = await redditapi.get_links(ctx.message.content.split()[2], 10)
    if len(posts) > 0:
        post = posts[random.randint(0, len(posts))]
        await ctx.send(f"{post.title}\n{post.url}")

# yes there are safer ways to do this
# I just don't care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
