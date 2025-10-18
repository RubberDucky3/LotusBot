import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Intents let your bot access messages and user data
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def scramble(ctx):
    import random
    moves = ["R", "L", "U", "D", "F", "B"]
    modifiers = ["", "'", "2"]
    scramble = " ".join(random.choice(moves) + random.choice(modifiers) for _ in range(20))
    await ctx.send(f"🧊 Your scramble: `{scramble}`")

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))

