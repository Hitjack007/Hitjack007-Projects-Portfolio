def add_time(start, duration, start_day=None):
    # Day mapping
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    time, period = start.split()
    hour, minute = map(int, time.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    
    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(':'))
    
    # Add duration
    final_minute = minute + dur_minute
    final_hour = hour + dur_hour + final_minute // 60
    final_minute %= 60
    days_later = final_hour // 24
    final_hour %= 24

    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        final_period = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        final_period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        final_period = 'PM'
    else:
        display_hour = final_hour - 12
        final_period = 'PM'
    
    # Day of week calculation
    if start_day:
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
    else:
        new_day = None
    
    # Format day and suffix
    day_suffix = ''
    if days_later == 1:
        day_suffix = ' (next day)'
    elif days_later > 1:
        day_suffix = f' ({days_later} days later)'

    # Assemble final time string
    time_str = f"{display_hour}:{final_minute:02d} {final_period}"
    if new_day:
        time_str += f", {new_day}"
    time_str += day_suffix
    
    return time_str


