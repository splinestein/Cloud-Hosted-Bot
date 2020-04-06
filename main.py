import discord
from discord.ext import commands

import time

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Activated. @ -> "+ str(current_time))
    

@client.event
async def on_member_join(m):
    print(str(m)+" joined.")
    channel = client.get_channel(696503641309446144)
    await channel.send(str(m)+' joined.')

@client.event
async def on_member_remove(m):
    print(str(m)+" left.")
    channel = client.get_channel(696503641309446144)
    await channel.send(str(m)+' left.')

@client.command()
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.author.bot:
        return
    if msg.content.startswith('--'):
        message = msg[2:]
        if message == "latency":
            channel = client.get_channel(696503641309446144)
            await channel.send(f'Latency: {round(client.latency * 1000)}ms')

client.run('Njk2NTAwODI4MzU3NTI1NjM0.XoppCw.xi99nJizoTtnnkq-kJikM7BKwDE')