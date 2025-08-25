import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "put ur token here" # <<< Put ur discord bot token here

@bot.command()
async def speak(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

bot.run(TOKEN) # js runs the bot and makes it online
