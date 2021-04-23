#!/usr/bin/env python
# ^^ Why would you remove that..

import discord
from discord.ext import commands

import sys
import traceback

print("starting...")


def get_prefix(bot, message):
    """Bot Prefixes."""
    prefixes = ['$', '&', 'Hey Moxie ']
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix,
                   description='Moxie Bot!')

initial_extensions = ['cogs.Economy',
                      'cogs.Fun',
                      'cogs.Internet']

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

    await bot.change_presence(activity=discord.Game(name="refactoring :nauseated_face:"))
    print(f'Successfully logged in and booted...!')

bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg",
        bot=True, reconnect=True)
