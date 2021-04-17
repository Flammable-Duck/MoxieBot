#!/usr/bin/env python
from cmds.fortune import get_fortune
from cmds.rateme import rateuser
from cmds.urbansearch import search_urban
from cmds.xkcd import random_xkcd
from cmds.users import user_bal, change_bal, top_users
from cmds.roulette import play_roulette
from cmds.reddit import get_links
from cmds.loan import give_player_loan

from discord.ext import commands
import discord
import random                                                                                                                                                                                                                                                       
print("starting...")

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("MoxieBot, © 2021 BubbyRoosh and Flammable Duck")

class Economy(commands.Cog):
    """Economy commands"""
    @commands.command()
    async def bal(_, ctx):
        "see a user's coin balance"
        try:
            user_uid = int(ctx.message.content.split()[1].replace("!","").replace(">","").replace("<","").replace("@",""))
        except:
            user_uid = ctx.message.author.id
        u2_mention = await bot.fetch_user(user_uid)

        coins = user_bal(user_uid)

        title = str(u2_mention) + "'s Balance:"
        body = "**Coins**: ⍟" + str(coins)

        embed = discord.Embed(title=title,
                              description=body, color=discord.Color.blue())
        await ctx.send(embed = embed)

    @commands.command()
    async def give(_, ctx):
        "give <target> <amount>"
        user1_uid = int(ctx.message.author.id)
        user2_uid = int(ctx.message.content.split()[1].replace("!","").replace(">","").replace("<","").replace("@",""))
        amount = int(ctx.message.content.split()[2])
        coin_bal = user_bal(ctx.message.author.id)
        if user1_uid == user2_uid:
            await ctx.send("You cant give yourself money!")
        else:
            if amount > coin_bal:
                await ctx.send("You dont have enough!")
            else:
                change_bal(user1_uid, -amount)
                change_bal(user2_uid, amount)
                await ctx.send(ctx.message.author.mention + " gave "+ ctx.message.content.split()[1] + " " + str(amount) + " coins!")
    @commands.command()
    async def loan(_, ctx):
        "loan <amount>"
        give_player_loan(0, 0)

    @commands.command()
    async def rich(_, ctx):
        "see the richest users"
        title = "Richest Users"
        search = top_users()
        body = ""
        number = 0
        for user in search:
            uid, bal = user
            user_name = await bot.fetch_user(uid)
            number += 1
            rank = str(number).replace(
                "1", ":first_place: ").replace("2", ":second_place: ").replace("3", ":third_place: ").replace("4", ":small_blue_diamond: ").replace("5", ":small_blue_diamond: ")
            body += rank + "**" + str(bal) + "** - " + str(user_name) + "\n"
        embed = discord.Embed(title=title,
                              description=body, color=discord.Color.blue())
        await ctx.send(embed = embed)

    @commands.command()
    async def roulette(_, ctx):
        "roulette <amount> <bet>(red, black, green, even, odd, number)"
        amount = int(ctx.message.content.split()[1])
        bettype = ctx.message.content.split()[2]
        coin_bal = user_bal(ctx.message.author.id)
        if amount > coin_bal:
            await ctx.send("You dont have enough coins! \n Balance: %s"%coin_bal)
        else:
            winnings, result = play_roulette(ctx.message.author.id, bettype, amount)
            change_bal(ctx.message.author.id, int(winnings))
            await ctx.send(result)

class Fun(commands.Cog):
    """Fun commands"""
    @commands.command(name="1984")
    async def _1984(_, ctx):
        "literally 1984"
        await ctx.send("""
        ```
        ⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣾⣟⠳⢦⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠉⠉⠉⠉⠉⠒⣲⡄⠀
        ⠀⠀⠀⠀⠀⣿⣿⣿⡇⡇⡱⠲⢤⣀⠀⠀⠀⢸⠀⠀⠀1984⠀⣠⠴⠊⢹⠁
        ⠀⠀⠀⠀⠀⠘⢻⠓⠀⠉⣥⣀⣠⠞⠀⠀⠀⢸⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⢸⠀⠀
        ⠀⠀⠀⠀⢀⣀⡾⣄⠀⠀⢳⠀⠀⠀⠀⠀⠀⢸⢠⡄⢀⡴⠁⠀     ⡞⠀
        ⠀⠀⠀⣠⢎⡉⢦⡀⠀⠀⡸⠀⠀⠀⠀⠀⢀⡼⣣⠧⡼⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀
        ⠀⢀⡔⠁⠀⠙⠢⢭⣢⡚⢣⠀⠀⠀⠀⠀⢀⣇⠁⢸⠁⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀
        ⠀⡞⠀⠀⠀⠀⠀⠀⠈⢫⡉⠀⠀⠀⠀⢠⢮⠈⡦⠋⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀
        ⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⣀⡴⠃⠀⡷⡇⢀⡴⠋⠉⠉⠙⠓⠒⠃⠀⠀⠀
        ⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⡼⠀⣷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⡞⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢧⠀⠀⠀⠀⠀⠀⠀⠈⠣⣀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ```""")

    @commands.command()
    async def uwu(_, ctx):
        "owo"
        await ctx.send("owo")

    @commands.command()
    async def fortune(_, ctx):
        "The classic fortune command"
        await ctx.send(get_fortune())

    @commands.command()
    async def r8me(_, ctx):
        "Let Moxie rate you!"
        await ctx.send(rateuser(ctx.message.author.mention))


class Internet(commands.Cog):
    @commands.command()
    async def xkcd(_, ctx):
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
    async def urban(_, ctx):
        "search the Urban Dictionary"
        word = ctx.message.content.split()[1]
        data = search_urban(word)
        body = data['list'][0]['definition'] + "\n\n" + "*" + data['list'][0]['example'] + "*"
        embed = discord.Embed(title= word, url=data['list'][0]['permalink'] ,
                              description=body.replace("[", "").replace("]", ""), color=discord.Color.blue())
        embed.set_author(name="Urban Dictionary", url="https://urbandictionary.com/",
                         icon_url="https://g.udimg.com/assets/apple-touch-icon-2ad9dfa3cb34c1d2740aaf1e8bcac791e2e654939e105241f3d3c8b889e4ac0c.png")
        await ctx.send(embed = embed)

    @commands.group()
    async def reddit(_, ctx):
        "Reddit commands"
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid reddit command")

    @reddit.command()
    async def hot(_, ctx):
        "reddit hot <subreddit>"
        posts = await get_links(ctx.message.content.split()[2], 10)
        if len(posts) > 0:
            post = posts[random.randint(0, len(posts))]
            await ctx.send(f"{post.title}\n{post.url}")

bot.add_cog(Economy())
bot.add_cog(Fun())
bot.add_cog(Internet())
# yes there are safer ways to do this
# I just don't care
bot.run("ODI5NTkxNTcwNzU1NDg1NzE2.YG6XWw.a5jFzhjcoK8XCWaOUJsVI3PQKsg")
