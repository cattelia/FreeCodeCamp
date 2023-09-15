
def add_time(start, duration, day=""):
    '''
    start STR: "11:06 PM"
    duration STR: "2:02"    
    >>> 1:08 AM
    '''

    #Called in: printDateString(total)
    #If daypassedin is False, do not print the day of the week. >>> 6:10 PM
    #If daypassedin is True, print the day of the week.         >>> 2:02 PM, Monday

    daypassedin = False
    if day == "":
        day = "monday"
    else:
        daypassedin = True

    #Make day entry lowercase, always. I disrespect your case sensitivity.
    day = day.lower()
    week = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

    #Function that takes in STR: start time and STR: day of the week.
    def convert_start(start, day):
        
        '''
        M:0=0, T:1=1440, W:2=2880, R:3=4320, F:4=5760, S:5=7200, S:6=8640     
        ###THIS IS PROBABLY WRONG AS MONDAY min is 0. There are 10080 minutes in a week not 8640.###
        '''

        #Using the position in the array, multiple that by how many minutes there are in a day so we can know exactly where we are in the week.
        time = week.index(day) * 1440 #1440 minutes in a day

        #Converting and splitting the STR: start into multi-assignment variables
        #   In: "3:00 PM" 
        #   Out: hour="3" minute="00" sub="PM"
        hour, minute, sub = start.replace(":", " ").split(" ")
        #Convert hour and minute to INT
        hour = int(hour)
        minute = int(minute)
        
        #Convert anytime after 12PM to the 24-clock cycle
        if sub == "PM":
            hour += 12
        #Convert hours to minutes and assign it to time
        time += hour * 60
        #Add the remaining minutes to time
        time += minute

        return time


    def convert_duration(duration):

        #Converting and splitting the STR: start into multi-assignment variables
        #   In: "3:00" 
        #   Out: hour="3" minute="00"
        hour, minute = duration.split(":")

        #Convert hour and minute to INT
        hour = int(hour)
        minute = int(minute)
        #Convert hours to minutes then add to minutes
        return (hour * 60) + minute

    #Add the starting time (now in minutes) and duration time (now in minutes) together
    total = convert_start(start, day) + convert_duration(duration)
    #print(total)

    def printDateString(total):

        #With the total time we calculated above, we want to know what day of the week we are on.
        #By taking the total minutes, dividing it by how many days there are in minutes (1440 min/day)
        #   Make that an INT to remove any remaining minutes, we just want days.
        #Taking that INT: day, we want to know what day/position of the week we are by using Modulo 7, where 7 is how many days there are in a week.
        #   In: 1540 minutes
        #   day Out: 1 [day]
        day = int(total / 1440) % 7

        #1440 minutes go into 1540 one time, which accounts for 1440 of the 1540 minutes. 1-day.
        #   remainder Out: 100 minutes
        remainder = total % 1440

        #Now we want to know what the hour is in the remaining time XX:00 AM/PM.
        #Taking remainder, we find how many hours there are, which we take remainder / 60 seconds and assigning to INT: hour 
        #   In: 100 minutes
        #   Out: 1 [hour]
        hour = int(remainder / 60)

        #Since we converted any hour over 12 into a 24-hour time, we need to convert it back.
        #Also, we want to know whether this is AM or PM, using this information.
        #   1 - 11 : AM
        #   12 : PM
        #   13 - 24 : PM
        #Assigning a BOOL: isPM
        
        isPM = False
        if hour > 12:
            isPM = True
            hour -= 12
        
        #Now we want to know what the minute is in the remaining time 00:XX AM/PM.
        #   In: 100
        #   Out: 40 [minutes]
        minute = remainder % 60

        result = "{}:{:02d} {}".format(hour, minute, "PM" if isPM else "AM")
        if daypassedin:
            result = result + ", " + week[day].capitalize()
        
        return result


    print(printDateString(total))


        #print("Remainder: {}\nHour: {}\nMinute: {}".format(remainder, hour, minute))
        

    #find_representation(total)


#add_time("10:10 PM", "3:30", "Monday") #Out: 1540 // 1440 >>> 1:40 AM
#add_time("10:10 PM", "3:30", "Tuesday") #Out: 1540 // 1440 >>> 1:40 AM

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM                              >>> Pass

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday                      >>> Pass  

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM                             >>> FAIL, 12:03 AM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)                   >>> FAIL, 1:40 AM

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)    >>> FAIL, 0:03 AM, Thursday

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)               >>> FAIL, 7:42 AM