import icalendar
import recurring_ical_events
from requests import get
from os import getenv
from datetime import date

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

