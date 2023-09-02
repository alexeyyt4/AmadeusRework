import disnake
from disnake.ext import commands
import aiosqlite

class UnWarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_file = "warnings.db"  # Имя файла базы данных SQLite

    @commands.slash_command()
    async def unwarn(self, ctx, member: disnake.Member, warn_id: int):
        # Проверяем, что роль модератора выше роли участника, у которого снимаем предупреждение
            if ctx.author.top_role <= member.top_role:
                await ctx.send("Вы не можете снимать предупреждения у участников с ролью, выше или равной вашей!")
                return

            # Открываем базу данных SQLite
            async with aiosqlite.connect(self.db_file) as db:
                # Проверяем, что предупреждение существует для указанного участника
                cursor = await db.execute("SELECT mod_id, reason FROM warnings WHERE user_id = ? AND rowid = ?",
                                      (member.id, warn_id))
                warning = await cursor.fetchone()
                await cursor.close()

                if warning:
                    # Если предупреждение существует, удаляем его из базы данных
                    await db.execute("DELETE FROM warnings WHERE user_id = ? AND rowid = ?", (member.id, warn_id))
                    await db.commit()

                    moderator = ctx.guild.get_member(warning[0])
                    moderator_name = moderator.display_name if moderator else f"Пользователь с ID {warning[0]}"
                    await ctx.send(f"Предупреждение для {member.mention} снято модератором {moderator_name}.")
                else:
                    await ctx.send(f"Предупреждение с ID {warn_id} не найдено для {member.mention}.")

def setup(bot):
    bot.add_cog(UnWarnCog(bot))
