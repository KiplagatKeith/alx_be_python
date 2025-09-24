from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()

    return current_date

print("Current date and time: ", display_current_datetime())

number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    global number_of_days
    future_date = date.today() + timedelta(days = number_of_days)

    return future_date


print("Future date:", calculate_future_date())
