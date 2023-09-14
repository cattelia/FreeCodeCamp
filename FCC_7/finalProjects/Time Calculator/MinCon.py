
def add_time(start, duration, day=""):
    daypassedin = False
    if day == "":
        day = "Monday"
    else:
        daypassedin = True


    '''
    start STR: "11:06 PM"
    duration STR: "2:02"    
    >>> 1:08 AM
    '''

    #Make day entry lowercase, always. I disrespect your case sensitivity.
    day = day.lower()
    week = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]
    #start = start.split()   #In: "11:06 PM" Out: ['11:06', 'PM']


    #Get hour and minute from start
    def convert_start(start, day):

        time = week.index(day) * 1440 #1440 minutes in a day
        hour, minute, sub = start.replace(":", " ").split(" ")
        hour = int(hour)
        minute = int(minute)
        
        if sub == "PM":
            hour += 12
        time += hour * 60
        time += minute

        return time
    

    #Get hour and minute from duration
    def convert_duration(duration):
        hour, minute = duration.split(":")
        hour = int(hour)
        minute = int(minute)
        return (hour * 60) + minute

    total = convert_start(start, day) + convert_duration(duration)
    #print(total)


    def printDateString(total):
        #find day of the week
        #in order to find what day of the week, 
        day = int(total / 1440) % 7
        remainder = total % 1440
        #print(day)

        hour = int(remainder / 60)
        isPM = False
        if hour > 12:
            isPM = True
            hour -= 12
        
        minute = remainder % 60
        result = "{}:{:02d} {}".format(hour, minute, "PM" if isPM else "AM")
        if daypassedin:
            result = result + " " + week[day].capitalize()
        
        return result


    print(printDateString(total))


        #print("Remainder: {}\nHour: {}\nMinute: {}".format(remainder, hour, minute))
        

    #find_representation(total)


add_time("10:10 PM", "3:30", "Monday") #Out: 1540 // 1440 >>> 1:40 AM
add_time("10:10 PM", "3:30") #Out: 1540 // 1440 >>> 1:40 AM