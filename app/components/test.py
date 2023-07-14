from app import bot

@bot.command()
async def hello(ctx, name):
    await ctx.send(f'Hi, {name}')
