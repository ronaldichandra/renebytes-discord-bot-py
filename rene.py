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
async def ping(ctx):
    em = discord.Embed(color=discord.Colour.magenta())
    em.title = "Pong!"
    em.description = f'{bot.latency * 1000} ms'
    await ctx.send(embed=em)

if message.content.startswith('<@'):
    await bot.send_message(message.channel, "Ummm")
    await bot.semd_message(message, "Hai! Kamu telah di-mention di suatu server!")

if __name__ == "__main__":
    bot.run(TOKEN)
