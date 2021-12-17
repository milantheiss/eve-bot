import json
import logging
import os
import random

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

active = True

with open("config.json") as file:
    bot_name = json.load(file).get("bot-name")


@bot.event
async def on_ready():
    print("EVE is ready to go")


@bot.command(name='ping')
async def _ping(ctx):
    if active:
        await ctx.send('pong')


@bot.command(name="github")
async def post_github(ctx):
    if active:
        embed = discord.Embed(title="GitHub Repository",
                              description="GitHub Repository des Bots "
                                          "\n**https://github.com/milantheiss/eve-bot**", color=0x0998c8)
        await ctx.send(embed=embed)


@bot.command(name="flipacoin")
async def flip_a_coin(ctx):
    ran = round(random.random())
    if ran == 0:
        await ctx.send("Kopf")
    else:
        await ctx.send("Zahl")


@bot.command("help")
async def send_help(ctx):
    if active:
        embed = discord.Embed(title="Help", color=0x097dc8)
        embed.add_field(name="`eve mitwirkende`", value="Jeder, der an diesem Projekt mitgearbeitet hat.", inline=False)
        embed.add_field(name="`eve github`", value="Link zum Source Code", inline=False)
        embed.add_field(name="`eve help`", value="Liste aller Befehle", inline=False)
        await ctx.send(embed=embed)


@bot.command("setBotState")
async def set_bot(ctx, _bot, state):
    global active
    print(_bot)
    print(bot_name)
    if ctx.message.author.guild_permissions.administrator and _bot == bot_name:
        print(state)
        if state == "true" or state == "True":
            active = True
            await ctx.send("I am now active")
        else:
            active = False
            await ctx.send("I am now NOT active")


bot.run(TOKEN)
