#!/usr/bin/python
from os import getenv
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "Congratulations" in str(message.content) and str(message.author.id) == "716390085896962058":
        await message.channel.send(message.author.mention+", That is the wrong Pokémon!")
    
client.run(getenv("KEY"))