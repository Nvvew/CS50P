import datetime
import inflect
import sys

def main():
    # Prompt user for date of birth
    dob_str = input("Date of Birth (YYYY-MM-DD): ")

    # Try to parse the date of birth
    try:
        dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        # Invalid format, exit without exception
        sys.exit("Invalid date format")

    # Get today's date
    today = datetime.date.today()

    # Calculate the difference in days
    delta = today - dob
    minutes = delta.days * 24 * 60

    # Create an inflect engine
    p = inflect.engine()

    # Convert the number of minutes to words, with commas and without "and"
    minutes_in_words = p.number_to_words(minutes, andword=",")

    # Capitalize the first letter and print the result
    print(minutes_in_words.capitalize(), "minutes")

if __name__ == "__main__":
    main()
