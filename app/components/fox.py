import requests
from app import bot
from json import loads

@bot.command(name='inspirity')
async def inspirity(ctx):
    req = requests.get('https://zenquotes.io/api/random')
    req = loads(req.text)
    quote = req[0]['q'] + '-' + req[0]['a']
    await ctx.send(quote)