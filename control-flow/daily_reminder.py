task = input("Describe your task: ")
task_priority = input("Is it high, medium or low? ")
time_bound = input("Is it time bound? yes/no? ")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is {task_priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is {task_priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is {task_priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")