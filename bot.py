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
today = date.today()
#today = "2021-04-25"

def get_dailyevents():
    olddate = ""

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
    if dailyevents[0] == str(today):
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

client.run(getenv("KEY"))