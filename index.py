import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())
TOKEN = 'MTAzOTI1NTg4ODgyNjk5MDcxMw.GksOfW.QKznFDJbDhbwmd3yvVrJyd2eyuyb7ypybGVQdk'

@bot.command()
async def do(ctx, pre, type, stat):
    embed =discord.Embed(
        title= 'New Stat',
        description=f'**Username:** {pre}\n**Type:** {type}\n**Status:** {stat}',
        color=0x774dea
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/930661781498642452/1036703925191057418/tcu.gif')
    embed.set_footer(text='Programmed By ArdianS', icon_url='https://media.discordapp.net/attachments/930661781498642452/1036703925191057418/tcu.gif')

    channel = bot.get_channel(1039366436809879593)
    await channel.send(embed=embed)

bot.run(TOKEN)
