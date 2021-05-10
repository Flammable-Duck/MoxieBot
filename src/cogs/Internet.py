"""
All commands using APIs or otherwise relying on other servises
"""
import discord
from discord.ext import commands
from functions.reddit import get_hot, get_top
from functions.urbansearch import search_urban
from functions.xkcd import random_xkcd


class Internet(commands.Cog, name="Internet"):
    """
    Internet commands
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def xkcd(self, ctx):
        """
        get a random xkcd
        $xkcd
        """
        data = random_xkcd()
        url = "https://xkcd.com/" + str(data['num']) + "/"
        embed = discord.Embed(title=data["title"],
                              url=url,
                              description="",
                              color=discord.Color.blue())

        embed.set_footer(text=data["alt"])
        embed.set_image(url=data["img"])
        embed.set_author(name="xkcd",
                         url="https://xkcd.com",
                         icon_url="https://www.explainxkcd.com/wiki/images/thumb/e/e4/xkcdFavicon.png/25px-xkcdFavicon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def urban(self, ctx, *, word: str = None):
        """
        search the urban dictionary
        $urban <serch term>
        """
        if not word:
            await ctx.send("Usage: urban <search term>")
        else:
            data = search_urban(word)
            try:
                body = data['list'][0]['definition'] + \
                    "\n\n*" + data['list'][0]['example'] + "*"

                embed = discord.Embed(title=word, url=data['list'][0]['permalink'],
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
        "view Reddit posts by subreddit"
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid reddit command")

    @reddit.command()
    async def hot(self, ctx, sub=None):
        "<subreddit>"
        # Cringe moment right here
        if sub != None:
            post = await get_hot(sub, 10)
            if post != None:
                await ctx.send(f"{post.title}\n{post.url}")
        else:
            await ctx.send("No subreddit specified!")

    @reddit.command()
    async def top(self, ctx, sub=None):
        "<subreddit>"
        if sub != None:
            post = await get_top(sub, 10)
            if post != None:
                await ctx.send(f"{post.title}\n{post.url}")
        else:
            await ctx.send("No subreddit specified!")


def setup(bot):
    bot.add_cog(Internet(bot))
