import discord
from discord.ext import commands

import urllib.request
import urllib.parse
import re

url = 'https://www.worldometers.info/coronavirus/?'

import time

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("v. 0.0.1 Activated. @ -> "+ str(current_time))
    

@client.event
async def on_member_join(m):
    print(str(m)+" joined.")
    channel = client.get_channel(697977974653190216)
    await channel.send(str(m)+' joined.')

@client.event
async def on_member_remove(m):
    print(str(m)+" left.")
    channel = client.get_channel(697977974653190216)
    await channel.send(str(m)+' left.')

@client.command()
async def latency(ctx):
    await ctx.send(f'Response @ -> {round(client.latency * 1000)}ms')

@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    print(ctx.message.author.id)
    if ctx.message.author.id == 677924052958183435:
        await user.add_roles(role)
    else:
        await ctx.send("Only j90 can perform this command.")
    #await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

@client.command()
async def corona(ctx):
    url = 'https://www.worldometers.info/coronavirus/?'
    req = urllib.request.Request(url, headers= {"User-Agent": "Mozilla/5.0"})

    resp = urllib.request.urlopen(req)
    respData = resp.read()

    paragraphs = re.findall(r'<div class="maincounter-number">(.*?)></div>',str(respData))

    totalcases = re.findall(r'<span style="color:#aaa">(.*?)</span>',str(paragraphs))
    totalcases = "".join(totalcases)
    totalcases = totalcases.replace(" ", "")

    paragraphs2 = re.findall(r'<span>(.*?)</span>',str(paragraphs))
    paragraphs2 = " ".join(paragraphs2)
    totaldeaths = paragraphs2.split(' ')[0]
    totalrecovered = paragraphs2.split(' ')[1]

    cdr = "Total cases: "+str(totalcases)+", Total deaths: "+str(totaldeaths)+", Total recovered: "+str(totalrecovered)
    await ctx.send(cdr)


client.run('Njk2NTAwODI4MzU3NTI1NjM0.XoppCw.xi99nJizoTtnnkq-kJikM7BKwDE')