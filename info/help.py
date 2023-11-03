import disnake
from disnake.ext import commands
import datetime

from disnake.interactions import MessageInteraction

class Select(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Модерация", value="1"),
            disnake.SelectOption(label="Фан", value="2"),
            disnake.SelectOption(label="Информация", value="3"),
            disnake.SelectOption(label="[ДОПОЛНИТЕЛЬНО]Дискорд сервера сообщества бота", value="4")
        ]
        super().__init__(
            placeholder="Тыкай сюда!",
            custom_id="help",
            max_values=1,
            min_values=1,
            options=options,
        )
class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_select_option(self, interaction):
         if interaction.custom_id == "help":
          if interaction.values[0] == "1":
              embed = disnake.Embed(
                  title="Модерация🛡️",
                  description="**/ban - Забанить пользователя'\n/kick - Кикнуть пользователя\n/clear - Очистка сообщений (двухнедельные не удаляются. хотя могло и измениться за время написания этого текста)\n/warn и /unwarn - Заварнить/Снять варн пользователю ( для снятия варна нужно знать ID варна )\n/warnings - Показывает предупреждения пользователя",
                  timestamp=f"AmBot v1.0 (02.11.2023)"
              )
              await inter.response.send_message(embed=embed)
          if interaction.values[0] == "2":
              embed = disnake.Embed(
                  title="Фан🎪",
                  description="/ping - проверить пинг бота\n/roll - Всем знакомый ролл ( можно задать максималное число )",
                  timestamp=f"AmBot v1.0 (02.11.2023)"
              )
              await interaction.response.send_message(embed=embed)
          if interaction.values[0] == "3":
              embed = disnake.Embed(
                  title="Информация🎩",
                  description="/serverinfo - Дает информацию о сервере\n/userinfo - Дает информацию о участнике ( Надо чтобы указанный вами человек находился на сервере. )",
                  timestamp=f"AmBot v1.0 (02.11.2023)"
            )
              await inter.channel.send_message(embed=embed)
          if Select.values == "4":
              await interaction.response.send_message("https://discord.gg/8PafGdMnY8")

    @commands.slash_command(name="help", description="Учебник по командам")
    
    async def help(self, ctx):
        view = disnake.ui.View(timeout=None)
        view.add_item(Select())
        await ctx.send("Пожалуйста, выберете одну из кнопок в выпадающем меню:", view=view)

        
def setup(bot):
        bot.add_cog(HelpCommand(bot))