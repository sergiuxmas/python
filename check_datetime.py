import re
import sys

# Write a regular expression that checks for the correct date/time in this format: 2020-04-22 18:45:07
# Attention! The answer should be exactly one regular expression without additional code and logic. Check yourself before sending the result (https://regex101.com/).

pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$'


def is_datetime(date_time):
    return bool(re.match(pattern, date_time))


def check_date_time(date_time):
    if is_datetime(date_time):
        print(f"{date_time} is a datetime format")
    else:
        print(f"{date_time} is NOT a datetime format")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        value = sys.argv[1]
        check_date_time(value)
    else:
        print("Please provide a value.")
