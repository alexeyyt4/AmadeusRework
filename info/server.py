import disnake
from disnake.ext import commands
import datetime

class ServerInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="serverinfo", description="Дает информацию о сервере.")
    async def serverinfo(self, ctx):
        embed = disnake.Embed(
            title="Информация о сервере:",
            description=f"Имя сервера: {ctx.guild.name}\nВладелец: {ctx.guild.owner.mention}\nКоличество участников: {ctx.guild.member_count}\nДата создания сервера:||{ctx.guild.created_at}||",
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(ServerInfoCog(bot))