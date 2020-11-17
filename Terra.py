import discord
from discord.ext import commands
from googlesearch import search 


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.content.startswith('just google'):
        searchContent = ""
        text = str(message.content).split(' ')
        for i in range(2, len(text)):
            searchContent = searchContent + text[i]

        for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(j)

client.run("Nzc4MjU2NDc3NjA5Mzk0MTk2.X7PV0w.9bFKxZfInNgB4dJQCLpyBKuVBdo")