import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

from app.components import test
from app.components import fox
from app.components import cep
from app.components import cnpj
from app.components import address