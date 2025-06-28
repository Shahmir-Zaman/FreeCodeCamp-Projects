def add_time(start, duration, start_day=None):
    # Creating a list of days
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    time_parts = start.split()
    time_part = time_parts[0]
    period = time_parts[1]  # AM or PM
    
    start_hour = int(time_part.split(':')[0])
    start_minutes = int(time_part.split(':')[1])
    
    # Parse duration
    duration_hour = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    
    # Convert start time to 24-hour format for easier calculation
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Add duration to start time
    total_minutes = start_minutes + duration_minutes
    total_hours = start_hour + duration_hour
    
    # Handle minute overflow
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60
    
    # Calculate days passed
    days_passed = total_hours // 24
    final_hour = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        new_period = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        new_period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        new_period = 'PM'
    else:
        display_hour = final_hour - 12
        new_period = 'PM'
    
    # Format minutes with leading zero if needed
    formatted_minutes = str(total_minutes).zfill(2)
    
    # Build the result string
    new_time = f"{display_hour}:{formatted_minutes} {new_period}"
    
    # Add day of week if provided
    if start_day:
        # Find the starting day index (case insensitive)
        start_day_lower = start_day.lower()
        start_day_index = None
        for i, day in enumerate(days_of_week):
            if day.lower() == start_day_lower:
                start_day_index = i
                break
        
        if start_day_index is not None:
            # Calculate the final day
            final_day_index = (start_day_index + days_passed) % 7
            final_day = days_of_week[final_day_index]
            new_time += f", {final_day}"
    
    # Add day indicator
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time


# Test cases
print(add_time('3:00 PM', '3:10'))
# Expected: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Expected: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Expected: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Expected: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Expected: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Expected: 7:42 AM (9 days later)
