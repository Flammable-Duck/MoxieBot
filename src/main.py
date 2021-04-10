#!/bin/python3
import cmds.config
from cmds.fortune import get_fortune
from cmds.rateme import rateuser
from cmds.urbansearch import search_urban
from cmds.xkcd import random_xkcd, latest_xkcd

from discord.ext import commands
import discord
import random
import redditapi

print("starting...")

bot = commands.Bot(command_prefix='$')

cmds.config.init()
cmds.config.load(bot)

@bot.event
async def on_ready():
    print("MoxieBot, © 2021 BubbyRoosh and Flammable_Duck")

@bot.command()
async def uwu(ctx):
    "owo"
    await ctx.send("owo")

@bot.command()
async def xkcd(ctx):
    "get a random xkcd"
    data = random_xkcd()
    body =""
    url= "https://xkcd.com/" + str(data['num']) + "/"
    embed = discord.Embed(title=data["title"], url= url ,
                          description=body, color=discord.Color.blue())
    embed.set_footer(text= data["alt"])
    embed.set_image(url= data["img"])
    embed.set_author(name="xkcd", url="https://xkcd.com",
                     icon_url="https://www.explainxkcd.com/wiki/images/thumb/e/e4/xkcdFavicon.png/25px-xkcdFavicon.png")
    await ctx.send(embed = embed)

@bot.command()
async def urban(ctx):
    "search the Urban Dictionary"
    word = ctx.message.content.split()[1]
    data = search_urban(word)
    body = data['list'][0]['definition'] + "\n\n" + "*" + data['list'][0]['example'] + "*"
    embed = discord.Embed(title= word, url=data['list'][0]['permalink'] ,
                          description=body.replace("[", "").replace("]", ""), color=discord.Color.blue())
    embed.set_author(name="Urban Dictionary", url="https://urbandictionary.com/",
                     icon_url="https://g.udimg.com/assets/apple-touch-icon-2ad9dfa3cb34c1d2740aaf1e8bcac791e2e654939e105241f3d3c8b889e4ac0c.png")
    await ctx.send(embed = embed)

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
    "Moxie settings (none yet)"
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
    cmds.config.set_value(bot, name, value)

@bot.group()
async def reddit(ctx):
    "Reddit commands"
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
