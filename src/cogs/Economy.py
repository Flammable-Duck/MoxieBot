from functions.users import user_bal, change_bal, top_users
from functions.roulette import play_roulette
from functions.loan import give_player_loan
from functions.beg import beg_command

import discord
from discord.ext import commands

class Economy(commands.Cog):
    """Economy commands"""

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def bal(self, ctx):
        "see a user's coin balance"
        try:
            user_uid = int(ctx.message.content.split()[1].replace(
                "!", "").replace(">", "").replace("<", "").replace("@", ""))
        except:
            user_uid = ctx.message.author.id
        u2_mention = await bot.fetch_user(user_uid)

        coins = user_bal(user_uid)

        title = str(u2_mention) + "'s Balance:"
        body = "**Coins**: ⍟" + str(coins)

        embed = discord.Embed(title=title,
                              description=body, color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command()
    async def give(self, ctx):
        "give <target> <amount>"
        user1_uid = int(ctx.message.author.id)
        user2_uid = int(ctx.message.content.split()[1].replace(
            "!", "").replace(">", "").replace("<", "").replace("@", ""))
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
                await ctx.send(ctx.message.author.mention + " gave " + ctx.message.content.split()[1] + " " + str(amount) + " coins!")

    @commands.command()
    async def beg(self, ctx):
        "beg for money cuz your broke"
        await ctx.send(beg_command(ctx.message.author.id))

    @commands.command()
    async def loan(self, ctx):
        "loan <amount>"
        give_player_loan(0, 0)

    @commands.command()
    async def rich(self, ctx):
        "see the richest users"
        title = "Richest Users"
        search = top_users()
        body = ""
        number = 0
        for user in search:
            uid = user[0]
            bal = user[1]
            user_name = await bot.fetch_user(uid)
            number += 1
            rank = str(number).replace(
                "1", ":first_place: ").replace("2", ":second_place: ").replace("3", ":third_place: ").replace("4", ":small_blue_diamond: ").replace("5", ":small_blue_diamond: ")
            body += rank + "**" + str(bal) + "** - " + str(user_name) + "\n"
        embed = discord.Embed(title=title,
                              description=body, color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command()
    async def roulette(self, ctx):
        "roulette <amount> <bet>(red, black, green, even, odd, number)"
        amount = int(ctx.message.content.split()[1])
        bettype = ctx.message.content.split()[2]
        coin_bal = user_bal(ctx.message.author.id)
        if amount > coin_bal:
            await ctx.send("You dont have enough coins! \n Balance: %s" % coin_bal)
        else:
            winnings, result = play_roulette(
                ctx.message.author.id, bettype, amount)
            change_bal(ctx.message.author.id, int(winnings))
            await ctx.send(result)


def setup(bot):
    bot.add_cog(Economy(bot))