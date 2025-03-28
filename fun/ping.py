import disnake
from disnake.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Пинг - проверка работоспособности бота.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Понг! Текущая задержка бота: {round(self.bot.latency * 1000)}мс")


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))