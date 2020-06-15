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

async def woi(ctx):
    member = message.mentions[0] # Probably in a try block
    content = "{0.mention} ... {1.author.mention}".format(member, message)
    await ctx.send_message(..., content)

if __name__ == "__main__":
    bot.run(TOKEN)
