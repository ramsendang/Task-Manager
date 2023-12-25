from datetime import datetime

def getDate():
    while True:
        date_format = "%Y-%m-%d"  # Adjust the format based on your requirements
        user_input = input(f"Enter a due date ({date_format}): ")

        try:
            user_date = datetime.strptime(user_input, date_format).date()
            return user_date
        except ValueError:
            print(f"Invalid date format. Please enter a date in the format {date_format}.")

