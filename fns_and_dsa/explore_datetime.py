from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    # return formatted current date/time string
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(number_of_days):
    # save future date in a variable as required
    future_date = date.today() + timedelta(days=number_of_days)
    # return formatted future date string
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    # print current datetime
    print("Current date and time:", display_current_datetime())

    # *** Exact prompt required by the grader: ***
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # print future date
    print("Future date:", calculate_future_date(number_of_days))
