#!/usr/bin/python
from os import getenv
import discord
#from dotenv import load_dotenv
from random import randint
import aiocron
import asyncio
from calfunc import format_dailyevents, format_tomorrowevents

#load_dotenv()
client = discord.Client()

@aiocron.crontab('0 7 * * 1-5')
async def daily_notify():
    channel = client.get_channel(812364127439552563)
    message = "@everyone " + str(format_dailyevents())
    if message == 1:
        return(1)
    else:
        await channel.send(message)

@aiocron.crontab('47 9 * * *')
async def temp():
    channel = client.get_channel(829155943937212456)
    await channel.send("this should be sent at 9:47 every day") 

@aiocron.crontab('30 7 * * 1-5')
async def per1():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now first period.")

@aiocron.crontab('0 9 * * 1-5')
async def per2():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now second period.")

@aiocron.crontab('30 10 * * 1-5')
async def per3():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now third period.")

@aiocron.crontab('0 12 * * 1-5')
async def lunch():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now lunch.")

@aiocron.crontab('58 12 * * 1-5')
async def per4():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now forth period.")

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

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
    if "boobs" in str(message.content.lower()) or "tits" in str(message.content.lower()) or "breasts" in str(message.content.lower()):
        await message.channel.send("``(.) (.)``")
    if "^today" in str(message.content.lower()):
        temp = format_dailyevents()
        if temp == 1:
            await message.channel.send(message.author.mention+" Today is not a School day.")
        else:
            await message.channel.send(message.author.mention + " " + temp)
    if "^tomorrow" in str(message.content.lower()):
        temp = format_tomorrowevents()
        if temp == 1:
            await message.channel.send(message.author.mention+" Tomorrow is not a School day.")
        else:
            await message.channel.send(message.author.mention + " " + temp)
        
daily_notify.start()
temp.start()
per1.start()
per2.start()
per3.start()
lunch.start()
per4.start()

client.run(getenv("KEY"))