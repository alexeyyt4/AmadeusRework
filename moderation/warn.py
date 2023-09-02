import disnake
from disnake.ext import commands
import aiosqlite

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_file = "warnings.db"  # Имя файла базы данных SQLite

    @commands.slash_command()
    async def warn(self, ctx, member: disnake.Member, *, reason: str):
        # Проверяем, что член не является самим собой
        if member == ctx.author:
            await ctx.send("Вы не можете предупреждать сами себя!")
            return

        # Проверяем, что роль модератора выше роли участника, которого он предупреждает
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Вы не можете предупреждать участников с ролью, выше или равной вашей!")
            return

        # Открываем или создаем базу данных SQLite
        async with aiosqlite.connect(self.db_file) as db:
            # Создаем таблицу предупреждений, если она еще не существует
            await db.execute('''CREATE TABLE IF NOT EXISTS warnings (
                                    user_id INTEGER,
                                    mod_id INTEGER,
                                    reason TEXT
                                )''')
            await db.commit()

            # Добавляем запись о предупреждении в базу данных
            await db.execute("INSERT INTO warnings (user_id, mod_id, reason) VALUES (?, ?, ?)",
                             (member.id, ctx.author.id, reason))
            await db.commit()

        await ctx.send(f"{member.mention} был предупрежден за: {reason}")
def setup(bot):
    bot.add_cog(WarnCog(bot))
