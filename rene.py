import os
import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print("Masuk sebagai {}({})".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name="follow ig @renebaebae"))

@bot.command(pass_context=True)
em = discord.Embed(color=discord.Colour.pink())
    em.title = "Pong!"
    em.description = f'{bot.latency * 1000} ms'
    await ctx.send(embed=em)
   
if __name__ == "__main__":
    bot.run(TOKEN)
