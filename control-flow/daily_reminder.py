Task = input("Describe your task: ")
Priority = input("Is it high, medium or low? ")
Time_Bound = input("Is it time bound? yes/no? ")

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
        elif Time_Bound == "no":
            print(f"Note: {Task} is {Priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")

    case "medium":
        if Time_Bound  == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
        elif Time_Bound  == "no":
            print(f"Note: {Task} is {Priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")

    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")
        elif Time_Bound  == "no":
            print(f"Note: '{Task}' is {Priority} task. Consider completing it when you have fee time")
        else:
            print("Invalid time")