from app import bot
from json import loads
import requests

@bot.command(name='cnpj')
async def cnpj(ctx, cnpj):
    req = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    req = loads(req.text)
    await ctx.send(req)