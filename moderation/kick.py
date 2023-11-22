import disnake
from disnake.ext import commands
import datetime


class KickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Кик - выкидывание человека из сервера, с возможностью возврата")
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str, ctx):
        print(f"Делаю кик в {datetime.datetime.now}, на {ctx.guild.id}")
        if member == None:
            await inter.send("Данного участника нету на сервере!")
        """Кикнуть пользователя."""
        embed = disnake.Embed(
            title="Пользователь успешно кикнут!",
            description=f"{member.mention} был успешно забанен с причиной {reason}, модератором {inter.author.mention}",
            timestamp=datetime.datetime.now()
        )
        if member.id == inter.author.id:
          await inter.response.send_message("Вы не можете самого себя кикнуть.")
          return
        if inter.author.top_role <= member.top_role:
          await inter.response.send_message("Роль человека выше чем у вас!")
        await inter.response.send_message(embed=embed)
        print(f"Сделал кик в {datetime.datetime.now}, на {ctx.guild.id}")
        await member.kick(reason=reason)

def setup(bot: commands.Bot):
  bot.add_cog(KickCommand(bot))
