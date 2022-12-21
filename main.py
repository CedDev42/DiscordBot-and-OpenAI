import discord
from discord.ext import commands
import settings

#Setup du bot, des intents, et du signe des commandes
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    #Lorsque le bot est prêt, on charge les modules cogs, on imprime leurs noms et on lance le bot
    @bot.event 
    async def on_ready():
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
                print(f"cogs.{cog_file.name[:-3]} loaded")

    bot.run(settings.DISCORD_TOKEN)

if __name__ == "__main__":
    run()