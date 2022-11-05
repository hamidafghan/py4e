# time = input("Give the time in 12-h format (08:10:20AM): ")  # 08:10:20AM
time = "01:40:00PM"

"""
12:00:00AM - Midnight
00:00:00 - Midnight

12:00:00PM - Mid day
12:00:00 - Mid day

01:00:00PM -> 13:00:00
01:00:00AM -> 01:00:00
"""

hour = time[0:2]  # "12"
clock = time[-2:]  # AM

if hour == "12":
    if clock == "AM":
        print("00" + time[2:-2])
    else:  # PM
        print(time[:-2])
else:
    if clock == "AM":
        print(time[:-2])
    else:
        print(str(int(hour) + 12) + time[2:-2])
