import pathlib
import os
from logging.config import dictConfig
from dotenv import load_dotenv
import discord

load_dotenv()

#Dossier source du projet
BASE_DIR = pathlib.Path(__file__).parent

#Les tokens
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

#Dossier des cogs (modules)
COGS_DIR = BASE_DIR / "cogs"