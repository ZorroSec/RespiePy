from app import bot
from json import loads
import requests

@bot.command(name='ddd')
async def ddd(ctx, ddd):
    req = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{ddd}')
    req = loads(req.text)
    await ctx.send(req)