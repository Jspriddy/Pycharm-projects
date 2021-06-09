import time
#
# print(time.gmtime(0))
#
# time_here = time.localtime()
#
# # time.localtime() is a named tuple
# print("Year:", time_here[0], time_here.tm_year)
# print("Month", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)
# perf_counter to benchmark time process_time to get cpu processing speed
import time
from time import process_time as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start = my_timer()
start_time = time.strftime("%X", time.localtime(start))
input("Press enter to stop")

end = my_timer()
end_time = time.strftime("%X", time.localtime(end))
seconds = round(end - start, 2)

print("Started at {}, ended at {}"
      .format(start_time, end_time))

print(f"Your reaction time was {seconds} second(s)")