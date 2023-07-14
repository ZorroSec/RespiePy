from app import bot
from json import loads
import requests

@bot.command(name='cep')
async def cep(ctx, cep):
    req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    req = loads(req.text)
    await ctx.send(req)