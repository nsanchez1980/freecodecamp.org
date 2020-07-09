def add_time(start, duration, day=""):

    new_time = ""
    current_time = []
    current_hour = []
    current_day = 0
    days_later = 0
    time_to_add = []
    more_days = 0

    day_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    current_day = 0
    if day!="":
        while current_day <= 6:
            if day.lower() == day_of_the_week[current_day].lower():
                break
            else:
                current_day = current_day + 1
    
    current_time = start.split(" ")
    current_hour = current_time[0].split(":")
    hour = int(current_hour[0])
    if current_time[1] == "PM":
        hour = hour + 12
    minute = int(current_hour[1])
    time_to_add = duration.split(":")
 
    minute = minute + int(time_to_add[1])
    if minute > 59:
        hour = hour + 1
        minute = minute - 60
    hour = hour + int(time_to_add[0])
    while hour >= 24:
        hour = hour - 24
        more_days = more_days + 1
        days_later = more_days
    if hour == 24: hour = 0


    if more_days > 0:
        while current_day <= 6:
            current_day = current_day + 1
            more_days = more_days - 1
            if current_day>6:
                current_day = 0
            if more_days == 0: 
                break


    if hour > 12:
        new_time = str(hour - 12)+":"+'{:02d}'.format(minute)+" PM"
    elif hour == 12:
        new_time = "12:"+'{:02d}'.format(minute)+" PM"            
    elif hour == 0:
        new_time = "12:"+'{:02d}'.format(minute)+" AM"        
    else:
        new_time = str(hour)+":"+'{:02d}'.format(minute) + " AM"
    if day!="":
        new_time = new_time + ", " + day_of_the_week[current_day]
    if days_later>0:
        if days_later==1:
            new_time = new_time + " (next day)"
        else:
            new_time = new_time + " (" + str(days_later) + " days later)"

    return new_time



print(add_time("2:59 AM", "24:00", "saturDay"))

