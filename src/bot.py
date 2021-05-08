#!/usr/bin/python
from os import getenv
import discord
from random import randint
from calfunc import format_dailyevents, format_tomorrowevents
from datetime import datetime
from dateutil import relativedelta
import aiocron

#from dotenv import load_dotenv
#load_dotenv()

breasts_enabled = True
dick_enabled = True
pokemon_enabled = True

client = discord.Client()

start_time = datetime.now()
info = "This bot was written by ndebruin, and is under a MIT License. \nMore info can be found here: https://git.draigon.org/ndebruin/gevin2.0 \nThe uptime for this bot is: "

def info_format():
    current_time = datetime.now()
    difference = relativedelta.relativedelta(current_time, start_time)
    days = difference.days
    hours = difference.hours
    full_string = info + "{} Day(s), {} Hour(s).".format(days, hours)
    return full_string

@aiocron.crontab('0 7 * * 1-5')
async def daily_notify():
    channel = client.get_channel(812364127439552563)
    message = "@everyone " + str(format_dailyevents())
    if message == 1:
        return(1)
    else:
        await channel.send(message)
        if "Asynchronous Day" in message:
            no_periods()
        else:
            return

def no_periods():
    per1.stop()
    per2.stop()
    per3.stop()
    lunch.stop()
    per4.stop()
    period_start.start()

@aiocron.crontab('47 9 * * *')
async def daily_testing():
    channel = client.get_channel(829155943937212456)
    await channel.send("this should be sent at 9:47 every day")

@aiocron.crontab('25 7 * * 1-5')
async def per1():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now first period.")

@aiocron.crontab('55 8 * * 1-5')
async def per2():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now second period.")

@aiocron.crontab('25 10 * * 1-5')
async def per3():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now third period.")

@aiocron.crontab('55 11 * * 1-5')
async def lunch():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now lunch.")

@aiocron.crontab('53 12 * * 1-5')
async def per4():
    channel = client.get_channel(812364127439552563)
    await channel.send("@everyone It is now fourth period.")

@aiocron.crontab('0 22 * * *')
async def period_start():
    per1.start()
    per2.start()
    per3.start()
    lunch.start()
    per4.start()
    period_start.stop()


daily_notify.start()
daily_testing.start()
per1.start()
per2.start()
per3.start()
lunch.start()
per4.start()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global breasts_enabled
    global dick_enabled
    global pokemon_enabled
    content = str(message.content.lower())
    if message.author == client.user:
        return
    if "^disable" in content and str(message.author.id) == "331237610460807168":
        choice = str(content.split("^disable ",1)[1])
        if choice == "tits":
            breasts_enabled = False
            await message.channel.send("``tits`` disabled")
            return
        if choice == "testing":
            await message.channel.send("daily testing message disabled")
            daily_testing.stop()
            return
        if choice == "pokemon":
            await message.channel.send("pokemon disabled")
            pokemon_enabled = False
            return
        if choice == "dick":
            await message.channel.send("``dick`` disabled")
            dick_enabled = False
            return
        if choice == "periods":
            await message.channel.send("period notifications disabled for one day")
            no_periods()
            return
        else:
            return
    if "^enable" in content and str(message.author.id) == "331237610460807168":
        choice = str(content.split("^enable ",1)[1])
        if choice == "tits":
            await message.channel.send("``tits`` enabled")
            breasts_enabled = True
            return
        if choice == "testing":
            await message.channel.send("daily testing message enabled")
            daily_testing.stop()
            return
        if choice == "pokemon":
            await message.channel.send("pokemon enabled")
            pokemon_enabled = True
            return
        if choice == "dick":
            await message.channel.send("``dick`` enabled")
            dick_enabled = True
            return
        else:
            return
    if "Congratulations" in str(message.content) and str(message.author.id) == "716390085896962058":
        await message.channel.send(message.author.mention+", That is the wrong Pokémon!")
        return
    if dick_enabled and ("cock" in content or "dick" in content):
        length = randint(0, 10)
        strlen = ""
        for i in range(length):
            strlen += '='
            i
        await message.channel.send(message.author.mention+" Your dick is this long ˅```8" + strlen + "D```")
        return
    if "boobs" in content or "tits" in content or "breasts" in content:
        await message.channel.send("``(.) (.)``")
        return
    if "^today" in content:
        temp = format_dailyevents()
        if temp == 1:
            await message.channel.send(message.author.mention+" Today is not a School day.")
        else:
            await message.channel.send(message.author.mention + " " + temp)
        return
    if "^tomorrow" in content:
        temp = format_tomorrowevents()
        if temp == 1:
            await message.channel.send(message.author.mention+" Tomorrow is not a School day.")
        else:
            await message.channel.send(message.author.mention + " " + temp)
        return
    if "^info" in content:
        await message.channel.send(info_format())

client.run(getenv("KEY"))
