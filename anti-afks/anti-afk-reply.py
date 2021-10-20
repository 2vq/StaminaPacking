import discord
import random
import time
import os

from colorama import Fore

client = discord.Client()


token = ''

@client.event
async def on_connect():
    os.system(f'cls & title [Anti-Afk] By hellahigh - Connected To {client.user}')
    print(f'''{Fore.MAGENTA}
Anti-Afk
https://github.com/aimvelocity
''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        print(f'''
     {Fore.GREEN}      You are being Afk-Checked
 {Fore.RED}===============================================
 {message.author} Has pinged you.
 Groupchat / Dm: {message.channel}
 Server: {message.guild}
 ===============================================
       {Fore.GREEN}       Replyed to Afk-Check
''')

        time.sleep(random.choice([5]))#,2,3,4,5]))#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))#16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        await message.reply(random.choice(['.','hgwa', 'ujawgdf', 'jefhafuh','f','jf','ehjgrf','ddj','s','sf','/','2','hi','hd','k','ff','hi','p','n','mm']))
client.run(token, bot = False)
