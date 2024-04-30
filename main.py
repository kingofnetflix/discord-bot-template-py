import random
import discord
import aiohttp
import asyncio
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)
# this system is really bad, i dont encourage using it like this but this temp is mainly for me lol
# unfortuntly this messy code is made by kingofnetflix

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')

@bot.tree.command(name="example", description="example interaction / slash command")
async def example(interaction: discord.Interaction):
    await interaction.response.send_message('hello, i am a example bot made by kingofnetflix')


bot.run('TOKEN')
