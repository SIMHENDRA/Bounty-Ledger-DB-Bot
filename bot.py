import handler
import discord
from discord.ext import commands
import sys


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Sheriff activation')

@client.event
async def on_message(message):
    if message.content.startswith('$'):
        comd = message.content[1:]
        try:
            op = handler.handle(comd)
            if op:
                await message.channel.send("```\n" + op + "\n```")
        except:
            await message.channel.send("`errrrrrr`")

client.run(sys.argv[1])

