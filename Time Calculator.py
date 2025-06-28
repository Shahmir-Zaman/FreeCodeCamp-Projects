def add_time(start, duration,start_day=None):
    #Creating a List of Days
    daysOfWeek=["Monday","Tuesday","Wednessday","Thursday","Friday","Saturday",]
    new_time=""
    new_time_minute=0
    new_time_hour=0
    next_day=0
    final_day=""
    #Extracting the time 
    start_hour=int(start.split(":")[0])
    start_minutes=int(start.split(":")[1].split(" ")[0])
    time_of_day=start.split(" ")[1]
    duration_hour=int(duration.split(":")[0])
    duration_minutes=int(duration.split(":")[1])

    #Casses which will cause an error
    if start_hour > 12 or start_minutes > 59 or duration_minutes > 59:
        return "Given time is not valid"


    #Coding the logic
    new_time_minute=start_minutes+duration_minutes
    if new_time_minute >60:
        duration_hour+=1
        new_time_minute=(str(new_time_minute-60)).rjust(2,"0")

    print(f'{start_hour}\n{start_minutes}\n{duration_hour}\n{duration_minutes}\n{new_time_minute}')
    #return new_time
add_time('6:30 PM', '205:35')