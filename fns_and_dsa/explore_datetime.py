from datetime import datetime, timedelta, date

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:", display_current_datetime())

# Part 2: Calculate a future date
number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    future_date = date.today() + timedelta(days=number_of_days)
    # Format as "YYYY-MM-DD"
    return future_date.strftime("%Y-%m-%d")

print("Future date:", calculate_future_date())
