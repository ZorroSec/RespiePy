from app import bot
import requests
from json import loads

@bot.command(name='address')
async def address(ctx, address):
    req = requests.get(f'http://ip-api.com/json/{address}')
    req = loads(req.text)
    await ctx.send(req)