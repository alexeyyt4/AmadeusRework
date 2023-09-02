import disnake
from disnake.ext import commands
import os

bot = commands.Bot(help_command=None, intents=disnake.Intents.all())
@bot.event
async def on_ready():
    print(f"Успешно вошел в {bot.user}.")

bot.load_extension("fun.ping")
bot.load_extension("moderation.ban")
bot.load_extension("moderation.kick")
bot.load_extension("moderation.warn")
bot.load_extension("moderation.unwarn")
bot.load_extension("moderation.warnings")

bot.run("MTA3NjYwMTM3MjE4NDY4MjU5OA.GVn0Je.LWXjBOrfQjPx25Xu4FSyEabedFAGkbaB-cLY3w")