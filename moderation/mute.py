import disnake
from disnake.ext import commands
import aiosqlite
import datetime

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Мут - временная блокировка чата в минутах (используеться timeout дискрода)")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        embed = disnake.Embed(
            title=f"Был замучен {member.global_name}",
            description=f"{inter.author.mention} замутил данного человека до {time}, за {reason}",
            timestamp=datetime.datetime.now(),
        )
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MuteCog(bot))