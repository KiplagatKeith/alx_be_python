# daily_reminder.py

Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        elif Time_Bound == "no":
            print(f"Reminder: '{Task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time input.")

    case "medium":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that requires immediate attention today!")
        elif Time_Bound == "no":
            print(f"Reminder: '{Task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time input.")

    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a low priority task that requires immediate attention today!")
        elif Time_Bound == "no":
            print(f"Reminder: '{Task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time input.")

    case _:
        print("Invalid priority input.")
