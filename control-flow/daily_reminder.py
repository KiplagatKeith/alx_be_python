# daily_reminder.py

# Ask user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority using match-case
match priority:
    case "high":
        priority_text = f"'{task}' is a high priority task"
    case "medium":
        priority_text = f"'{task}' is a medium priority task"
    case "low":
        priority_text = f"'{task}' is a low priority task"
    case _:
        priority_text = f"'{task}' has an unknown priority"

# Check if task is time-bound and print reminder
if time_bound == "yes":
    print(f"Reminder: {priority_text} that requires immediate attention today!")
else:
    print(f"Reminder: {priority_text}. Consider completing it when you have free time.")
