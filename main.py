#!/bin/python3

from discord.ext import commands

bot = commands.Bot(command_prefix='^')

@bot.command()
async def uwu(ctx):
    await ctx.send("owo")

# yes there are safer ways to do this
# I just don' care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
