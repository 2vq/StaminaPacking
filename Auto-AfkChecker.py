import discord
import json
import colorama
import os
import time
import random
from colorama import Fore
from discord.ext import commands

token = ''
prefix = ','

client = commands.Bot(command_prefix = prefix, case_insensitive = True, self_bot = True)

@client.event
async def on_connect():
    os.system(f'cls & title [Auto-Afk-Checker] - Connected To {client.user}')
    print(f'''
                                            {Fore.CYAN}  Discord-Auto-Afk-Checker
                                          Currently Connected To: {client.user}
                                          {Fore.GREEN}       Current Prefix: {prefix}
    ''')
# thanks kyicks l o l
@client.command()
async def afkcheck(ctx, limit):
    global stop_afkcheck
    await ctx.message.delete()
    stop_afkcheck = False
    try:
        limit = int(limit)
    except:
        print("ERROR INVALID INT!")
        return

    for i in range(int(limit)):
        if not stop_afkcheck:
            await ctx.send(f"{limit}")
            limit -= 1 
            math = f"0.{random.randint(0,2)}"
            time.sleep(float(math))
        else:
            break

@client.command()
async def antiafk(ctx):
    await ctx.message.delete()
    em = discord.Embed(title = "Anti-Afk", description = "Turned on Anti-Afk with the reply of ``*zzz im asleep slumberrr*`` and the delay of ``*0 seconds!*``")
    await ctx.send(embed = em)

client.run(token, bot = False)
