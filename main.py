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

# --- LEAGUE COMMANDS ---
@bot.command()
async def summoner(ctx, name: str):
    # Placeholder: Replace with API call to fetch summoner stats
    await ctx.send(f"Fetching stats for summoner: {name} ... (API call here)")

@bot.command()
async def match(ctx, match_id: str):
    # Placeholder: Replace with API call to fetch match data
    await ctx.send(f"Fetching match {match_id} ... (API call here)")

# --- ERROR HANDLING ---
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {str(error)}")

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))

