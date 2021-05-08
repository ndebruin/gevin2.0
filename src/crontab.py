#!/usr/bin/python

import aiocron
import asyncio
from os import getenv
import discord
from calfunc import format_dailyevents

#from dotenv import load_dotenv
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

client.run(getenv("KEY"))