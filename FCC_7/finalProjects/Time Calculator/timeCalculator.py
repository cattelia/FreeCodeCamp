
def add_time(start, duration, day="Monday"):

    '''
    start STR: "11:06 PM"
    duration STR: "2:02"    
    >>> 1:08 AM
    '''

    week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

    #Get hour and minute from start
    start = start.split()   #In: "11:06 PM" Out: ['11:06', 'PM']
    startHour = int(start[0].split(":")[0])
    startMinute = int(start[0].split(":")[1])

    #print("Start hour: {}".format(startHour))
    #print("Start minute: {}".format(startMinute))

    #Get hour and minute from duration
    durationHour = int(duration.split(":")[0])
    durationMinute = int(duration.split(":")[1])


    
    #24-hour conversion
    if start[1] == "PM" and startHour != 12:
        startHour += 12
    else:
        pass
    
    #Printed Output
    if startMinute < 10:
        print("The current time: {}:0{}".format(str(startHour), str(startMinute)))
    else:
        print("The current time: {}:{}".format(str(startHour), str(startMinute)))
    

'''
from datetime import datetime, timedelta

    datetime_original = datetime(year=2006, month=11, day=23, hour=10, minute=40)
    print("\nOriginal datetime: ", datetime_original, "\n")
    datetime_original = datetime(year=2023, hour=10, minute=40)
    print("\nOriginal datetime: ", datetime_original, "\n")
     
    # Time to add or subtract
    time_delta = timedelta(hours=10, minutes=23, seconds=45)
    print("Timedelta: ", time_delta, "\n")
     
    # Add
    datetime_new = datetime_original + time_delta
    print("After adding time: ", datetime_new, "\n")
    
    print("Time delta {}".format(timedelta()))
'''

'''
    We are going to convert a 12-hour clock to a 24-hour clock.
    AM: 0:00 - 11:59    >>> time as written
    PM: ]12:00[ - 23:59   >>> 12 + remainder after 12 up to 24

        Pull the time in hours and minutes and convert it to an integer.
        Convert those numbers to a 24-hr clock:
            - Hours 1 - 11 AM, stays the same
            - Hour 12 PM, stays the same
            - Hours 1 - 11 PM, time + 12

    #this needs to be tackled later. Get the time down first.
    Unless otherwise stated, we are starting on Monday.
    If the time rolls from 23:49 -> 0/24, then the day becomes the next day, Tuesday.
    However, if the time rolls from 11:50 - 12:00, it is still the same day. #duh

    
'''

add_time("11:06 PM", "2:02")
add_time("12:16 PM", "2:02")
add_time("1:02 PM", "2:02")
