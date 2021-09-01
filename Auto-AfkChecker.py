# splrs ducking to run my stamina on friday when i dont have school xd
import discord
import json
import colorama
import os
import time
from colorama import Fore
from discord.ext import commands


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

client = commands.Bot(command_prefix = prefix, case_insensitive = True, self_bot = True)

@client.event
async def on_connect():
    os.system(f'cls & title [Auto-Afk-Checker] - Connected To {client.user}')
    print(f'''
                                            {Fore.CYAN}  Discord-Auto-Afk-Checker
                                          Currently Connected To: {client.user}
                                          {Fore.GREEN}       Current Prefix: {prefix}
    ''')

@client.command()
async def autoafk(ctx, user:discord.User = None):
    await ctx.message.delete()
    if user is None:
        print(f'''{Fore.RED} [ERROR] No one was Pinged!''')
    await ctx.send(f'afk check {user.mention} 1')
    time.sleep(0)
    await ctx.send("2")
    time.sleep(0)
    await ctx.send("3")
    time.sleep(0)
    await ctx.send("4")
    time.sleep(0)
    await ctx.send("5")
    time.sleep(0)
    await ctx.send("6")
    time.sleep(0)
    await ctx.send("7")
    time.sleep(0)
    await ctx.send("8")
    time.sleep(0)
    await ctx.send("9")
    time.sleep(0)
    await ctx.send("10")

@client.command()
async def antiafk(ctx):
    await ctx.message.delete()
    em = discord.Embed(title = "Anti-Afk", description = "Turned on Anti-Afk with the reply of ``*zzz im asleep slumberrr*`` and the delay of ``*0 seconds!*``")
    await ctx.send(embed = em)

client.run(token, bot = False)
