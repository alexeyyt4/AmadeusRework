import disnake
from disnake.ext import commands
import datetime

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="help", description="Учебник по командам")
    async def help(self, ctx):
        embed = disnake.Embed(
        title="Учебник",
        description=f"**Модерация:**\n\n/ban - Забанить пользователя'\n/kick - Кикнуть пользователя\n/clear - Очистка сообщений (двухнедельные не удаляются. хотя могло и измениться за время написания этого текста)\n/warn и /unwarn - Заварнить/Снять варн пользователю ( для снятия варна нужно знать ID варна )\n/warnings - Показывает предупреждения пользователя\n\n**Развлечения:**\n\n/ping - понг!\n/roll - Рандомное число от 1 до указанного вами.\n\n**Информация:**\n\n/serverinfo - Информация о сервере\n/userinfo - Информация о пользователе ( нужно чтобы пользователь находился на сервере )",
        color=disnake.Colour.dark_gold()
        )
        embed.set_footer(
        text="AmBot v1.0 (03.11.2023)"
        )
        await ctx.send(embed=embed)

        
def setup(bot):
        bot.add_cog(HelpCommand(bot))