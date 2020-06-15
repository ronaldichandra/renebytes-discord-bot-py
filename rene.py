import os
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
TOKEN = os.getenv("TOKEN")

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='follow ig @renebaebae')
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='sama ronhyun')
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print("Masuk sebagai {}({})".format(bot.user.name, bot.user.id))
    bot.loop.create_task(status_task())

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
