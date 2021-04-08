#!/bin/python3
from discord.ext import commands
import discord.user
from commands.commands import *

bot = commands.Bot(command_prefix='^')

@bot.event
async def on_ready():
    print("MoxieBot, ©2021 BubbyRoosh and Flammable_Duck")



# yes there are safer ways to do this
# I just don' care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
