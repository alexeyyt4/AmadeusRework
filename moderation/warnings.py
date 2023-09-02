import disnake
from disnake.ext import commands
import aiosqlite

class WarningCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_file = "warnings.db"  # Имя файла базы данных SQLite

    @commands.slash_command()
    async def warnings(self, ctx, member: disnake.Member):
        # Открываем базу данных SQLite
            async with aiosqlite.connect(self.db_file) as db:
                # Извлекаем предупреждения для указанного участника
                cursor = await db.execute("SELECT rowid, mod_id, reason FROM warnings WHERE user_id = ?", (member.id,))
                warnings = await cursor.fetchall()
                await cursor.close()

            if warnings:
            # Если есть предупреждения, отправляем их в чат
                embed = disnake.Embed(title=f"Предупреждения для {member.display_name}", color=0xFF0000)
                for rowid, mod_id, reason in warnings:
                    moderator = ctx.guild.get_member(mod_id)
                    moderator_name = moderator.display_name if moderator else f"Пользователь с ID {mod_id}"
                    embed.add_field(name=f"ID предупреждения: {rowid} (Модератор: {moderator_name})", value=f"Причина: {reason}", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{member.display_name} не имеет предупреждений.")

def setup(bot):
    bot.add_cog(WarningCog(bot))