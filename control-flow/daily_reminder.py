# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize a default reminder
reminder = f"'{task}' has an unrecognized priority level."

# Process the task using a match case statement
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task"
    case "medium":
        reminder = f"'{task}' is a medium-priority task"
    case "low":
        reminder = f"'{task}' is a low-priority task"

# Check if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder = f"The time-bound input '{time_bound}' is invalid. Please answer 'yes' or 'no'."

# Print the customized reminder
print("\nReminder:", reminder)
