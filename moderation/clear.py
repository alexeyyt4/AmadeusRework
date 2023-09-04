import disnake
from disnake.ext import commands
import io
import chat_exporter

class ClearCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Очистка чата с сохранением чата в .html файле")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
        transcript = await chat_exporter.export(
        inter.channel,
        limit=amount + 1,
        military_time=True,
        tz_info="Europe/Moscow",
        bot=commands,
        )
        
        if transcript is None:
            return
        
        transcript_file=disnake.File(
            io.BytesIO(transcript.encode()),
            filename=f"transcript-{inter.channel.name}.html",
        )
        await inter.channel.purge(limit=amount + 1)
        await inter.response.defer()
        await inter.edit_original_response(f"Чат был почищен на {amount}", file=transcript_file)

def setup(bot: commands.Bot):
    bot.add_cog(ClearCog(bot))
