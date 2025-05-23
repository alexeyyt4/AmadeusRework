import disnake
from disnake.ext import commands
import datetime


class BanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Бан - блокировка доступа к дискорд серверу")
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.User, reason: str):
        print(f"Делаю бан в {datetime.datetime.now}, на {inter.guild.id}")
        """Забанить пользователя."""
        embed = disnake.Embed(
            title="Пользователь успешно забанен!",
            description=f"{member.mention} был успешно забанен с причиной {reason}, модератором {inter.author.mention}",
            timestamp=datetime.datetime.now()
        )
        if member.id == inter.author.id:
            await inter.response.send_message("Вы не можете забанить самого себя.")
            return
        if inter.author.top_role <= member.top_role:
            await inter.response.send_message("Вы не можете забанить человека с ролью выше.")
            return
        await inter.response.send_message(embed=embed)
        print(f"Сделал бан в {datetime.datetime.now} на {inter.guild.id}")
        await member.ban(reason=reason)


def setup(bot: commands.Bot):
  bot.add_cog(BanCommand(bot))
