import json
import logging
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

#test

logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)

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
    logger.info("EVE is ready to go")


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
    if ctx.message.author.guild_permissions.administrator and _bot == bot_name:
        if state == "true" or state == "True":
            logger.info("Bot is now active")
            active = True
            await ctx.send("I am now active")
        elif state == "false" or state == "False":
            logger.info("Bot is now NOT active")
            active = False
            await ctx.send("I am now NOT active")
        else:
            logger.info("`State` not success fully change")
            await ctx.send("`State` Argument invalid")


bot.run(TOKEN)
