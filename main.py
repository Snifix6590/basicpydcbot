import discord
from discord.ext import commands

# Define the bot prefix
bot = commands.Bot(command_prefix='!')

# Event called when the bot is online
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Example command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am here.')

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
