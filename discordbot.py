import discord
import traceback
import team
from os import getenv
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def LoLteams(ctx, *names):
    t = team.team(*names)
    ms = t[0][0] + "\n" + t[0][1] + "\n" + t[0][2] + "\n"  + t[0][3] + "\n" + t[0][4] + "\n-----------------------------\n" + t[1][0] + "\n" + t[1][1] + "\n"+ t[1][2] + "\n"+ t[1][3] + "\n" + t[1][4] + "\n"
    await ctx.send(ms)

@bot.command()
async def LoLみくじ(ctx):
    await ctx.send(f'お前のレーン、{team.mikuji()}だよ by 国情のONI')

@bot.command()
async def LoLteams5(ctx, *names):
    t = team.team5(*names)
    ms = t[0] + "\n" + t[1] + "\n" + t[2] + "\n"  + t[3] + "\n" + t[4] + "\n"
    await ctx.send(ms)
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
