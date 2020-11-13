from datetime import date
import time
import datetime

print(time.ctime())  # prints current date/time in a pretty format

curr = time.time()   # gets a current timestamp as a float of seconds and milliseconds

for i in range(100000):
    pass

now = time.time()    # do it again

elapsed = now - curr # how much time in between

elapsed_ms = elapsed * 1000

print(f"{elapsed_ms:.2f} milliseconds have elapsed")

# for t in range(10,1,-1):
#     print(t)
#     time.sleep(1)

# Normally you'd have a loop that looks at an external resource
# at regular intervals and waits for something to happen.

# while True:
#     if something:
#         do something
#         break
#     else:
#         time.sleep(some period)


# CURRENT datetime
now = datetime.datetime.now()

# FUTHER OR PAST date time
ny2019 = datetime.datetime(2019,12,31)

ny2020 = datetime.datetime(2020,12,31)

# DELTA or DIFFERENCE BETWEEN DATES

betweenyears = ny2020 - ny2019   # this is a timedelta
print(betweenyears)
tilnewyears = ny2020 - now
print(tilnewyears)

# Can also be used as an advanced elapsed timer

now = datetime.datetime.now()

time.sleep(2.333)

later = datetime.datetime.now()

elapsed = later - now

print(f'{elapsed.seconds}s:{elapsed.microseconds}ms')
