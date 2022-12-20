import discord
from discord.ext import commands
import settings

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
                print(f"cogs.{cog_file.name[:-3]} loaded")

    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()