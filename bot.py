import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Smiley is online as {bot.user}")

bot.run(os.getenv("MTU1MTIxNTIyOTA4MDQzNjc0Ng.GGnLg9.ZzV4YXoznWmAEqKWYhaaE3OGPmtWr3XybLFcG8"))
