def add_time(start, duration, start_day=None):
    # Days of the week (for optional day handling)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # --- Parse start time ---
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert to 24-hour clock
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # --- Parse duration ---
    dur_hour, dur_minute = map(int, duration.split(":"))

    # --- Total minutes ---
    total_minutes = start_hour * 60 + start_minute + dur_hour * 60 + dur_minute

    # Days later
    days_later = total_minutes // (24 * 60)
    # Remaining minutes for final time
    total_minutes = total_minutes % (24 * 60)

    # --- Convert back to 12-hour clock ---
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60

    if new_hour == 0:
        display_hour = 12
        display_period = "AM"
    elif new_hour < 12:
        display_hour = new_hour
        display_period = "AM"
    elif new_hour == 12:
        display_hour = 12
        display_period = "PM"
    else:
        display_hour = new_hour - 12
        display_period = "PM"

    # --- Build output string ---
    new_time = f"{display_hour}:{new_minute:02d} {display_period}"

    # Add day of week if provided
    if start_day:
        start_day = start_day.lower().capitalize()
        if start_day not in days:
            return "Error: Invalid day of week."
        new_day_index = (days.index(start_day) + days_later) % 7
        new_day = days[new_day_index]
        new_time += f", {new_day}"

    # Add info about days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

