import disnake
from disnake.ext import commands
import aiosqlite
import os
import datetime
class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_db_name(self, guild_id):
        if not os.path.exists("databases"):
            os.makedirs("databases")
        return f"databases/{guild_id}_warn.db"

    @commands.slash_command(description="Варн - выдача предупреждение участнику.")
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: disnake.Member, *, reason: str):
        print(f"Делаю варн в {datetime.datetime.now}, на {ctx.guild.id}")
        if member == None:
            await ctx.send("Данного участника нету на сервере!")
        guild_id = ctx.guild.id
        db_file = self.get_db_name(guild_id)
        # Проверяем, что член не является самим собой
        if member == ctx.author:
            await ctx.send("Вы не можете предупреждать сами себя!")
            return

        # Проверяем, что роль модератора выше роли участника, которого он предупреждает
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Вы не можете предупреждать участников с ролью, выше или равной вашей!")
            return

        # Открываем или создаем базу данных SQLite
        async with aiosqlite.connect(db_file) as db:
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
        print(f"Сделал варн в {datetime.datetime.now}, на {ctx.guild.id}")
        await ctx.send(f"{member.mention} был предупрежден за: {reason}")
def setup(bot):
    bot.add_cog(WarnCog(bot))
