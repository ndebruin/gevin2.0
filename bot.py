#!/usr/bin/python
from os import getenv
import discord
from dotenv import load_dotenv
from random import randint

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
    if "cock" in str(message.content.lower()) or "dick" in str(message.content.lower()):
        length = randint(0, 10)
        strlen = ""
        for i in range(length):
            strlen += '='
            i
        await message.channel.send(message.author.mention+" Your dick is this long ˅```8" + strlen + "D```")


client.run(getenv("KEY"))