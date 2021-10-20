import discord
import random
import time

client = discord.Client()

token = 'token here'

@client.event
async def on_ready():
    print(f'''
    {client.user}
    ''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        print('''reacting to ping.''')
        time.sleep(random.choice([3]))
        await message.add_reaction('😃')

client.run(token, bot = False)
