import os
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print("Masuk sebagai {}({})".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name="follow ig @renebaebae"))

@bot.command(pass_context=True)
async def ping(ctx):
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await ctx.send('Pong! {0}ms'.format(int(ms)))

if __name__ == "__main__":
    bot.run(TOKEN)
