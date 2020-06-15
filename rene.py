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

if match("<@!?435379055253127178>", message.content) is not None:
    text = await client.send_message(message.channel, "Pesan telah dikirim")
    await client.send_message(message.channel, "Ummm")
    await client.edit_message(text, "Hai! Kamu telah di-mention di suatu server!")

if __name__ == "__main__":
    bot.run(TOKEN)
