import disnake
from disnake.ext import commands
import datetime

class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="userinfo", description="Дает информацию о участнике.")
    async def serverinfo(self, ctx, member: disnake.Member):
        embed = disnake.Embed(
            title="Информация о сервере:",
            description=f"**Имя пользователя: {member.name}\nID: {member.id}\nДата создания профиля: ||{member.created_at}||\nДата присоединения к серверу: ||{member.joined_at}||**",
            
        )
        embed.set_thumbnail(member.display_avatar.url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(UserInfoCog(bot))