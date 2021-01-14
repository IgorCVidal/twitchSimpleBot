from twitchio.ext import commands
import time

token = 'teu token'
nameID = 'VidaLnx'
canal = 'VidaLnx'
PREFIX ='!'


bot = commands.Bot(
    # set up the bot
    irc_token=token,
    client_id=nameID,
    nick='vidalnx',
    prefix= PREFIX,
    initial_channels=[canal])

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{nameID} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(canal, f"/me has landed!")


@bot.command(name='commercial')
async def test(ctx):
    while envio == True:
        await ctx.send('/commercial 60')
        time.sleep(3600)
if __name__ == "__main__" :
    bot.run()