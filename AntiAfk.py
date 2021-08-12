import discord
import json
import colorama
import random
import asyncio
import datetime
import time
import os

from colorama import Fore

client = discord.Client()

with open('./config.json')as f:
  config = json.load(f)

token = config.get('token')

os.system("title Anti Afk ")
@client.event
async def on_connect():
    print(f'''{Fore.CYAN}
                                                       AntiAfk
                                                Made by sword#0004
                                             https://github.com/hellahigh
                                             Logged in as: {client.user}
''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        print(f'''{Fore.CYAN}
 {message.author} Has pinged you in:

 Group chat or dms: {message.channel}

 Server: {message.guild}
''')
        time.sleep(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        ## dont touch anything above u fucking idiot its the WAIT TIME BEFORE REPLYING ##
        await message.channel.send(random.choice(['focus', 'hi', 'i dont fold son', 'nice 1 lol', 'im asleep zzz'])) # u can add more by doing " , 'msg here' "

client.run(token, bot=False)
