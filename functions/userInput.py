from datetime import datetime

def getDate():
    while True:
        date_format = "%Y-%m-%d"  # Adjust the format based on your requirements
        user_input = input(f"Enter a due date ({date_format}): ")

        try:
            dueDate = datetime.strptime(user_input, date_format).date()
            return dueDate
        except ValueError:
            print(f"Invalid date format. Please enter a date in the format {date_format}.")

def getTaskName():
    while True:
        taskName = input(f"Enter a Task Name : ")
        if len(taskName) != 0:
            print(f"Your task is {taskName}")
            return taskName
        else:
            print(f"The Task Name should not be Empty")
