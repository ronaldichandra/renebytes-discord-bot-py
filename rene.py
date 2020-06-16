import os
import discord
import time
from discord.ext import commands
client = discord.Client()

bot = commands.Bot(command_prefix=".")
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print("Masuk sebagai {}({})".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name="follow ig @renebaebae"))

async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(f'{bot.user.mention}'):
        em = discord.Embed(color=discord.Colour.magenta())
        em.title = "Pong!"
        em.description = f'Type .help for more details.'
        await bot.send_message(message.channel, embed=em)

@bot.command(pass_context=True)
async def ping(ctx):
    em = discord.Embed(color=discord.Colour.magenta())
    em.title = "Pong!"
    em.description = f'{bot.latency * 1000} ms'
    await ctx.send(embed=em)

if __name__ == "__main__":
    bot.run(TOKEN)
