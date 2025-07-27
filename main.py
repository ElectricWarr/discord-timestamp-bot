import os
import discord
from datetime import datetime, timedelta
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN', default=False)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)


@bot.command()
async def sync(ctx: commands.Context) -> None:
    await ctx.bot.tree.sync()
    await ctx.send(f"Synced commands")

@bot.tree.command(name="localtime", description="Whats that in local time")
async def localtime(interaction: discord.Interaction, input_time: str, input_timezone: str) -> None:
    timezones = {
        'GMT': timedelta(hours=0),
        'UTC': timedelta(hours=0),
        'CET': timedelta(hours=1),
        'EST': timedelta(hours=-5),
        'CST': timedelta(hours=-6),
        'MST': timedelta(hours=-7),
        'PST': timedelta(hours=-8),
        'EDT': timedelta(hours=-4),
        'CDT': timedelta(hours=-5),
        'MDT': timedelta(hours=-6),
        'PDT': timedelta(hours=-7),
    }
    timezone = timezones.get(input_timezone.upper(), timedelta(hours=0))
    time_in_utc = datetime.strptime(f'01-01-1970 {input_time}', "%d-%m-%Y %H:%M") + timezone
    unix_time = int((time_in_utc - datetime(1970, 1, 1)).total_seconds())
    await interaction.response.send_message(f'<t:{unix_time}:t>')

bot.run(TOKEN)