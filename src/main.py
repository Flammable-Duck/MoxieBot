#!/usr/bin/env python3
"""
=============================================
   __     __)                 ______         
  (, /|  /|            ,     (, /    )       
    / | / |  _____/       _    /---(  ____/_ 
 ) /  |/  |_(_)  /(___(__(/_) / ____)(_) (__ 
(_/   '         /          (_/ (             
=============================================
MoxieBot, © 2021 BubbyRoosh and Flammable Duck

A general purpose Discord bot built with discord.py

"""

import sys
import traceback

import discord
from discord.ext import commands

print("starting...")


def get_prefix(bot, message):
    """Bot Prefixes."""
    prefixes = ['$', '&', 'Hey Moxie ']
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix,
                   description='Moxie Bot!')

initial_extensions = ['cogs.Economy',
                      'cogs.Fun',
                      'cogs.Internet',
                      'cogs.Moderation']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    """Runs when Bot is ready"""

    print("\nMoxieBot, © 2021 BubbyRoosh and Flammable Duck")
    print(
        f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Game(name="Moxie Bot!!"))
    print('Successfully logged in and booted...!')

bot.run("TOLKEN HERE",
        bot=True, reconnect=True)
