import disnake
from disnake.ext import commands
import aiosqlite
import datetime

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Мут - временная блокировка чата в минутах (используеться timeout дискрода)")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, time: str, reason: str):
        print(f"Делаю мут в {datetime.datetime.now}, на {ctx.guild.id}")
        if member == None:
            await inter.send("Данного участника нету на сервере!")
        await member.timeout(reason=reason, until=time)
        embed = disnake.Embed(
            title=f"Был замучен {member.global_name}",
            description=f"{inter.author.mention} замутил данного человека до {time}, за {reason}",
            timestamp=datetime.datetime.now(),
        )
        print(f"Сделал мут в {datetime.datetime.now}, на {ctx.guild.id}")
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MuteCog(bot))