import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    print("online")

@client.event
async def on_member_join(m):
    print(str(m)+" joined.")
    #chaid = '692025511727333407'
    channel = client.get_channel(696503641309446144)

    await channel.send(str(m)+' joined.')

@client.event
async def on_member_remove(m):
    print(str(m)+" left.")
    #chaid = '692025511727333407'
    channel = client.get_channel(696503641309446144)
    await channel.send(str(m)+' left.')

client.run('Njk2NTAwODI4MzU3NTI1NjM0.XoppCw.xi99nJizoTtnnkq-kJikM7BKwDE')