#!/usr/bin/python
from os import getenv
import discord
from dotenv import load_dotenv
from random import randint
import icalendar
import recurring_ical_events
from datetime import date

def dailyevents():
    cal = open("icalfeed.ics")

    today = date.today()

    olddate = ""

    calendar = icalendar.Calendar.from_ical(cal.read())
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
    #print(events)

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

client.run(getenv("KEY"))