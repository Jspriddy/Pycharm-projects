import time
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print("The epoch of this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Daylight Saving Time is in effect for this location")
    print("\t The DST timezone is {}".format(time.tzname[1]))

print("Today is " + time.strftime('%A, %B %d, %Y.'))
print("Local time is " + time.strftime('%Y-%m-%d %M:%S', time.localtime()))
print("Local time is " + time.strftime('%Y-%m-%d %M:%S', time.gmtime()))
