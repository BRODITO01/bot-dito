import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def minimal(ctx):
    await ctx.send(f'Hi! I am a {bot.user} , minimal hari sabtu minggu libur bos anjay!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE1NTA2Mzk1NzUyNzIwNzk3Ng.GxGTp5.UTWz6xcYukg9qcZlYulATGJgscjNp7leJkKO_4")