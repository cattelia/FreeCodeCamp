def add_time(time, duration, day=""):
    
    timeHour, timeMinute, sub = time.replace(":", " ").split()
    durationHour, durationMinute = duration.split(":")
    day = day.lower()
    week = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

    #Check and correct subscript on isPM
    if sub == "AM":
        isPM = False
    else:
        isPM = True

    #Check if a day was entered or assign to "monday"
    daypassedin = False
    if day == "":
        day = "monday"
    else:
        daypassedin = True


    if isPM is True and int(timeHour) != 12:
        timeHour = int(timeHour) + 12
        #print(timeHour)                                                     ###PRINT###
        current = (timeHour * 60) + int(timeMinute)
        #print(current)
    else:
        current = (int(timeHour) * 60) + int(timeMinute)


    #current = (int(timeHour) * 60) + int(timeMinute)
    #print("Time (min): {:>10}".format(current))                             ###PRINT###
    duration = (int(durationHour) * 60) + int(durationMinute)
    #print("Duration (min): {:>6}".format(duration))                         ###PRINT###
    total = current + duration
    #print("Total (min): {:>9}".format(total))                               ###PRINT###
    #print(isPM, duration, total)                                                             ###PRINT###


    #!!!This is how many days after the entered date!!! NOT how many days have gone by
    day = int(total / 1440) % 7
    #print("Day: {:>13}".format(day))                                        ###PRINT###
    remainder = total % 1440    
    #print("Remainder: {:>7}".format(remainder))                             ###PRINT###
    hour = int(remainder / 60)
    #print("Hours: {:>11}".format(hour))                                     ###PRINT###
    minute = remainder % 60
    #print("Minutes: {:>9}".format(minute))                                  ###PRINT###
    #print("isPM:", isPM)                                                    ###PRINT### 
    print(day, remainder, hour, minute)

    #Change time of day for 12
    # 12 AM
    if hour == 0 and remainder < 60:
        isPM = False
        hour = 12
    # Rest of AM
    elif remainder <= 719:
        isPM = False
    # 12 PM
    elif remainder >= 720 and remainder < 780:
        isPM = True
    # Rest of PM
    else: 
        isPM = True
        hour -= 12 

    #print("Hours: {:>11}".format(hour))                                     ###PRINT###
    #print("isPM:", isPM)                                                    ###PRINT### 


    result = "{}:{:02d} {}".format(hour, minute, "PM" if isPM else "AM")
    if daypassedin:
            result = result + ", " + week[day+1].capitalize()
    print(result + "\n")                                                    ###PRINT###
 


#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
#add_time("11:00 PM", "1:10")
# Returns: 12:10 AM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)