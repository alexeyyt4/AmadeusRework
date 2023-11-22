import disnake
from disnake.ext import commands
import os
import config 

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
bot.load_extension("moderation.clear")
bot.load_extension("moderation.mute")
bot.load_extension("fun.roll")
bot.load_extension("info.server")
bot.load_extension("info.user")
bot.load_extension("info.help")

bot.run(config.TOKEN)