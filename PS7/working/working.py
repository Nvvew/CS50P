import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)'
    
    match = re.match(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    # Extract matched groups for start time and end time
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert start and end times to 24-hour format
    start_time_24 = to_24_hour_format(start_hour, start_minute, start_period)
    end_time_24 = to_24_hour_format(end_hour, end_minute, end_period)

    return f"{start_time_24} to {end_time_24}"

def to_24_hour_format(hour, minute, period):
    # Default the minute to '00' if it's not provided
    if minute is None:
        minute = "00"

    hour = int(hour)
    minute = int(minute)

    # Validate hour and minute
    if hour < 1 or hour > 12 or minute < 0 or minute > 59:
        raise ValueError("Invalid time")

    # Convert to 24-hour format
    if period == "AM":
        if hour == 12:
            hour = 0  # 12 AM is 00:xx in 24-hour format
    elif period == "PM":
        if hour != 12:
            hour += 12  # PM hours are offset by +12, except for 12 PM

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()