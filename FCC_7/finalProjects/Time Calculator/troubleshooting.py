def add_time(time, duration, day=""):
    timeHour, timeMinute, sub = time.replace(":", " ").split()

    #Check subscript
    if sub == "AM":
        isPM = False
    else:
        isPM = True

    #print("{}\n{}".format(time, "It's PM\n" if isPM else "It's AM\n"))

    timeHour, timeMinute, sub = time.replace(":", " ").split()
    time = (int(timeHour) * 60) + int(timeMinute)

    #print("Time (min): {:>10}".format(time, sub))                           ###PRINT###

    durationHour, durationMinute = duration.split(":")
    duration = (int(durationHour) * 60) + int(durationMinute)
    
    
    #print("Duration (min): {:>6}".format(duration))                         ###PRINT###

    total = time + duration
    #print("Total: {:>15}".format(total))                                    ###PRINT###

    day = int(total / 1440) % 7
    #print("Day: {}".format(day))                                            ###PRINT###

    remainder = total % 1440    
    #print("Remainder: {}".format(remainder))                                ###PRINT###

    hour = int(remainder / 60)
    #print("Hours: {} ({} mins)".format(hour, hour*60))                      ###PRINT###

    minute = remainder % 60
    #print("Minutes: {:>6}".format(minute))                                  ###PRINT###

    #Change time of day for 12
    if hour == 12 and isPM is False:
        isPM = True
    elif hour == 12 and isPM is True:
        isPM = False
    #Change time of day and convert back to 12-hour clock
    elif isPM and hour > 12:
        isPM = False
        hour -= 12
    elif isPM is False and hour > 12:
        isPM = True
        hour -= 12
 
    result = "{}:{:02d} {}".format(hour, minute, "PM" if isPM else "AM")
    print(result)

'''
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM 
add_time("10:10 PM", "2:30")
# Returns: 12:40 AM
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM
'''


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)