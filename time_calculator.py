addison-tech's Solution to Build a Time Calculator Project
Close
×
PY
def add_time(start, duration, starting_day=None):
    # Days of the week reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period.upper() == 'PM':
        start_hour += 12 if start_hour != 12 else 0
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add minutes and carry over hours if needed
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    # Add hours and calculate total days passed
    total_hours = start_hour + duration_hour + extra_hours
    total_days = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format with AM/PM
    if final_hour_24 == 0:
        final_hour = 12
        period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        period = 'PM'

    # Format minutes
    final_minutes_str = f"{final_minutes:02}"

    # Determine new weekday if given
    if starting_day:
        day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (day_index + total_days) % 7
        new_day = days_of_week[new_day_index]
        day_part = f", {new_day}"
    else:
        day_part = ""

    # Determine days later text
    if total_days == 1:
        days_later = " (next day)"
    elif total_days > 1:
        days_later = f" ({total_days} days later)"
    else:
        days_later = ""

    # Compose final time string
    new_time = f"{final_hour}:{final_minutes_str} {period}{day_part}{days_later}"

    return new_time

# Example Usage:
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

Add initial Time Calculator project
