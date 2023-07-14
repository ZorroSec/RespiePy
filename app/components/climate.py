from app import bot
import requests
from json import loads

@bot.command(name='climate')
async def climate(ctx, cityCode):
    req = requests.get(f'https://brasilapi.com.br/api/cptec/v1/clima/previsao/{cityCode}')
    req = loads(req.text)
    await ctx.send(req)