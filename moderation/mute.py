import disnake
from disnake.ext import commands
import aiosqlite
import datatime

class WarningCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def mute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, time: str, reason: str):
        time = datatime.datatime.now() + datatime.datatime.delta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        embed = disnake.Embed(
            title=f"Был замучен {member.mention}"
            description=f"{inter.author.mention} замутил данного человека до {time}, за {reason}",
            timestamp=datatime.datatime.now(),
        )
        await inter.response.send_message(embed=embed)