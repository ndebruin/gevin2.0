import icalendar
import recurring_ical_events
from requests import get
from os import getenv
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()
callink = getenv("LINK")

def get_dailyevents():
    cal = get(callink)
    cal = cal.text
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
            else:
                return(1)    
    return(events)

def format_dailyevents():
    dailyevents = get_dailyevents()
    if dailyevents == 1:
        return(1)
    elif str(date.today()) == "2021-05-31":
        return("Today is Memorial Day. Enjoy your day off of school!")
    elif str(date.today()) == "2021-06-10":
        return("Today is the **last** day of School! It is also a {}.".format(dailyevents[1]))
    elif str(date.today()) == dailyevents[0]:
        day = dailyevents[1]
        if "Asynchronous Day" in dailyevents:
            return("Today is a {}, and is an Asynchronous Day.".format(day))
        else:
            return("Today is a {}.".format(day))
    else:
        return(1)