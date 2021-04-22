from functions.urbansearch import search_urban
from functions.xkcd import random_xkcd
from functions.reddit import get_links
import random

import discord
from discord.ext import commands


class Internet(commands.Cog, name="Internet stuff"):
    "API's are cool!"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def xkcd(self, ctx):
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

    @commands.command()
    async def urban(self, ctx, *, word: str = None):
        "search the Urban Dictionary"
        if not word:
            await ctx.send("Usage: urban <search term>")
        else:
            data = search_urban(word)
            try:
                body = data['list'][0]['definition'] + "\n\n*" + data['list'][0]['example'] + "*"

                embed = discord.Embed(title= word, url=data['list'][0]['permalink'] ,
                                  description=body.replace("[", "").replace("]", ""), color=discord.Color.blue())
                embed.set_author(name="Urban Dictionary", url="https://urbandictionary.com/",
                                 icon_url="https://g.udimg.com/assets/apple-touch-icon-2ad9dfa3cb34c1d2740aaf1e8bcac791e2e654939e105241f3d3c8b889e4ac0c.png")
                
            except IndexError:
                embed = discord.Embed(title=word,
                                      description="*No results Found*", color=discord.Color.blue())
                embed.set_author(name="Urban Dictionary", url="https://urbandictionary.com/",
                                 icon_url="https://g.udimg.com/assets/apple-touch-icon-2ad9dfa3cb34c1d2740aaf1e8bcac791e2e654939e105241f3d3c8b889e4ac0c.png")
            await ctx.send(embed=embed)
            

    @commands.group()
    async def reddit(self, ctx):
        "Reddit commands"
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid reddit command")

    @reddit.command()
    async def hot(self, ctx):
        "reddit hot <subreddit>"
        posts = await get_links(ctx.message.content.split()[2], 10)
        if len(posts) > 0:
            post = posts[random.randint(0, len(posts))]
            await ctx.send(f"{post.title}\n{post.url}")


def setup(bot):
    bot.add_cog(Internet(bot))
