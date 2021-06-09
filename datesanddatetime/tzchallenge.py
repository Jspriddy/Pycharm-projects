import pytz
import datetime

# for x in pytz.all_timezones:
#     print(x)

countries = {"1": "Europe/Lisbon", "2": "Europe/London", "3": "Europe/Luxembourg",
             "4": "Europe/Madrid", "5": "Europe/Malta", "6": "Indian/Mahe", "7": "Indian/Mauritius",
             "8": "Indian/Mayotte", "9": "Indian/Kerguelen"}

for key in sorted(countries):
    head, sep, tail = countries[key].partition('/')
    chosen_country = tail
    print(f"{key}: {chosen_country}")

choice = "-"
while choice != "0":
    if choice in countries.keys():
        country = countries[choice]
        tz_to_display = pytz.timezone(country)
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(chosen_country, world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X %z')))
        print("UTC is {}".format(datetime.datetime.utcnow().strftime('%A %x %X %z')))
    choice = input("Please choose a time zone or 0 to quit\n > ")

print("Goodbye")
