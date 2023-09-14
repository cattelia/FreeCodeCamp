
def add_time(start, duration, day="Monday"):

    '''
    start STR: "11:06 PM"
    duration STR: "2:02"    
    >>> 1:08 AM
    '''

    #Make day entry lowercase, always. I disrespect your case sensitivity.
    day = day.lower()
    weekL = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
    

    #Get hour and minute from start
    start = start.split()   #In: "11:06 PM" Out: ['11:06', 'PM']
    startHour = int(start[0].split(":")[0])*60
    startMinute = int(start[0].split(":")[1])
    startTime = startHour + startMinute

    print(startTime)

    #Get hour and minute from duration
    durationHour = int(duration.split(":")[0])*60
    durationMinute = int(duration.split(":")[1])
    durationTime = durationHour + durationMinute

    #Calculating minutes
    if startMinute + durationMinute >= 60:
        startHour += 1
        startMinute = (startMinute + durationMinute) % 60
    else:
        startMinute += durationMinute

    #24-hour Conversion & Calculating hours
    if start[1] == "PM" and startHour != 12:
        startHour = startHour + durationHour + 12
    else:
        startHour += durationHour



    print(startHour)

    #Convert back (Ignoring AM/PM)
    if startHour > 12 and startHour != 12:
        startHour -= 12
    else:
        pass


    #Printed Output
    if startMinute < 10:
        print("The current time: {}:0{} {}".format(str(startHour), str(startMinute), start[1]))
    else:
        print("The current time: {}:{} {}".format(str(startHour), str(startMinute), start[1]))


'''
    Calculations:
    #Same Day w/o Date
    "3:00 PM", "3:10"               >>> 6:10 PM
    "11:43 AM", "00:20"             >>> 12:03 PM

    #Same Day w/ Date
    "11:30 AM", "2:32", "Monday"    >>> 2:02 PM, Monday

    #Next Day
    "10:10 PM", "3:30"              >>> 1:40 AM (next day)

    #Few Days
    "11:43 PM", "24:20", "tueSday"  >>> 12:03 AM, Thursday (2 days later)
    "6:30 PM", "205:12"             >>> 7:42 AM (9 days later)
 
'''

#24-hour Conversion Check (Not worried about minutes)
#add_time("11:06 PM", "2:02")       #>>> 23:06
#add_time("12:16 PM", "2:02")       #>>> 12:16
#add_time("1:02 PM", "2:02")        #>>> 13:02

#Minute Check (Not worried about hours)
#add_time("1:02 PM", "2:58")        #>>> 14:00
#add_time("12:16 PM", "2:58")       #>>> 13:14

#Calculation Check
#add_time("11:06 PM", "2:02")       #>>> 25:08
#add_time("12:16 PM", "2:02")       #>>> 14:18
#add_time("1:02 PM", "2:02")        #>>> 15:04
#add_time("12:00 PM", "0:00")       #>>> 12:00
#add_time("11:59 PM", "0:01")       #>>> 12:00              #FAILED 24:00, not 12:00. Fixed.

#Test Calculations
#add_time("3:00 PM", "3:10")        #>>> 6:10 PM
#add_time("11:43 AM", "00:20")      #>>> 12:03 PM

#add_time("11:30 AM", "2:32", "Monday") #>>> 2:02 PM, Monday

add_time("10:10 PM", "3:30")        #1:40 AM (next day)    #FAILED 13:40, not 1:40.
