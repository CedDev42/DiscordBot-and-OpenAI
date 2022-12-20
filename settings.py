import pathlib
import os
from logging.config import dictConfig
from dotenv import load_dotenv
import discord

load_dotenv()

BASE_DIR = pathlib.Path(__file__).parent

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

COGS_DIR = BASE_DIR / "cogs"