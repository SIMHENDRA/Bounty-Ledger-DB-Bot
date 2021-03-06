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
    if message.content.startswith('$board'):
        comd = message.content[1:]
        try:
            op = handler.handle(comd)
            if op:
                await message.channel.send(content="```Open attached with your browser.```", file=op)
        except Exception as e: 
            print(e)
            await message.channel.send("```\nerrrrrrr\n```")
        return

    elif message.content.startswith('$'):
        comd = message.content[1:]
        try:
            op = handler.handle(comd)
            if op:
                await message.channel.send("```\n" + op + "\n```")
        except Exception as e: 
            print(e)
            await message.channel.send("`errrrrrr`")


client.run(sys.argv[1])

print("after run reached.")

