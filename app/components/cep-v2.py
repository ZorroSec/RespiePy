from app import bot
import requests
from json import loads

async def cepv2(ctx, cep):
    req = requests.get(f'https://brasilapi.com.br/api/cep/v2/{cep}')
    req = loads(req.text)
    await ctx.send(req)