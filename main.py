import logging
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger('DISCORD BOT')
logger.setLevel(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix=["eve ", "EVE "], help_command=None)


@bot.event
async def on_ready():
    print("EVE is ready to go")
    await message.channel.send('The bot is online ')


@bot.command(name='ping')
async def _ping(ctx):
    await ctx.send('pong')


@bot.command(name="github")
async def post_github(ctx):
    embed = discord.Embed(title="GitHub Repository",
                          description="GitHub Repository des Bots "
                                      "\n**https://github.com/milantheiss/eve-bot**", color=0x0998c8)
    await ctx.send(embed=embed)


@bot.command("help")
async def send_help(ctx):
    embed = discord.Embed(title="Help", color=0x097dc8)
    embed.add_field(name="`eve mitwirkende`", value="Jeder, der an diesem Projekt mitgearbeitet hat.", inline=False)
    embed.add_field(name="`eve github`", value="Link zum Source Code", inline=False)
    embed.add_field(name="`eve help`", value="Liste aller Befehle", inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)
