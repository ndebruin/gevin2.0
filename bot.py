#!/usr/bin/python
from os import getenv
import discord
from dotenv import load_dotenv
from random import randint
import icalendar
import recurring_ical_events
from datetime import date
import aiocron
import asyncio

calfile = open("icalfeed.ics")
cal = calfile.read()

def get_dailyevents():
    olddate = ""
    today = date.today()

    calendar = icalendar.Calendar.from_ical(cal)
    events = recurring_ical_events.of(calendar).at(2021)

    for event in events:
            day = event["DTSTART"].dt
            if str(day) == str(today):
                    summary = event["SUMMARY"]
                    if olddate == day and "asynchronous" in summary.lower():
                            events.append("Asynchronous Day")
                    else:
                            events = [str(day), str(summary)]
                    olddate = day
                
    return(events)

def format_dailyevents():
    dailyevents = get_dailyevents()
    if str(date.today()) == "2021-05-31":
        return("@everyone Today is Memorial Day. Enjoy your day off of school!")
    elif str(date.today()) == "2021-06-10":
        return("@everyone Today is the **last** day of School! It is also a {}.".format(dailyevents[1]))
    elif str(date.today()) == dailyevents[0]:
        day = dailyevents[1]
        if "Asynchronous Day" in dailyevents:
            return("@everyone Today is a {}, and is an Asynchronous Day.".format(day))
        else:
            return("@everyone Today is a {}.".format(day))

async def notify_dailyevents():
    channel = client.get_channel(812364127439552563)
    await channel.send(str(format_dailyevents()))

@aiocron.crontab('0 7 * * 1-5')
async def daily_notify():
    await notify_dailyevents()

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

load_dotenv()

client = discord.Client()

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
    if "^what day" in str(message.content.lower()) and str(message.author.id) == "331237610460807168":
        await notify_dailyevents()
        
daily_notify.start()
temp.start()
per1.start()
per2.start()
per3.start()
lunch.start()
per4.start()

client.run(getenv("KEY"))