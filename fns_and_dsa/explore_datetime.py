from datetime import datetime, timedelta, date

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    # Must return formatted string
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:", display_current_datetime())

# Part 2: Calculate a future date
def calculate_future_date(number_of_days):
    future_date = date.today() + timedelta(days=number_of_days)
    # Must return formatted string
    return future_date.strftime("%Y-%m-%d")

# Ask user for days
number_of_days = int(input("Enter number of days: "))

print("Future date:", calculate_future_date(number_of_days))
