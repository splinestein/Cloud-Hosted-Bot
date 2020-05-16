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
    
@client.command()
async def latency(ctx):
    await ctx.send(f'Response @ -> {round(client.latency * 1000)}ms')

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

    cdr = "Cases :mask: : "+str(totalcases)+", Total deaths :skull: : "+str(totaldeaths)+", Total recovered :thumbsup: : "+str(totalrecovered)
    await ctx.send(cdr)

client.run('Njk2NTAwODI4MzU3NTI1NjM0.XoppCw.xi99nJizoTtnnkq-kJikM7BKwDE')