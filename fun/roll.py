import disnake
from disnake.ext import commands
import random
import datetime

class RollCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="roll", description="Дает рандомное число от 0 до максимального. Дефолт аргумент - 100")
    async def roll(self, ctx, max_value: int = 100):
        if max_value <= 0:
            await ctx.send("Число не должно быть отрицательным.")
            return

        # Генерируем случайное число в диапазоне от 0 до max_value
        result = random.randint(0, max_value)
        embed = disnake.Embed(
          title=f"Выпало число: {result}",
          color=disnake.Colour.dark_gold(),
          timestamp=datetime.datetime.now()
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RollCog(bot))