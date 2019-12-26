import os
import datetime

def time_apart(departure_date, todays_date):
    day_count = todays_date - departure_date
    if day_count >= 5:
        return "call Laura"
    if day_count < 5:
        return "you can wait"

departure_date = int(input("When did she depart:  "))
todays_date = int(input("What is today's date:  "))

print(time_apart(departure_date, todays_date))

v = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(v)
