
from datetime import datetime, timedelta

def add_time(start, duration, day="Monday"):

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
