from rich.console import Console
from functions.options import createOptions
from functions.action import creatTask
from functions.action import printTask
from functions.action import deleteTasks
from functions.action import updateTasks
from functions.action import updateTaskStatus

file_path = "db.json"
console  = Console()
while True:
    # calling a functions which will display all the available option in the app and takes user input
    userInput = createOptions()
    if(userInput == "1"):
        # calling a funtion which creats a task 
        creatTask(file_path)
    elif(userInput == "2"):
        # calling a funtion which shows all the tasks 
        printTask(file_path)
    elif(userInput == "3"):
        # calling a fucntion wich delete the choosen task 
        deleteTasks(file_path)
    elif(userInput == "4"):
        # calling a function to update the name of the task
        updateTasks(file_path)
    elif(userInput=="5"):
        # calling a function to update the status of the task 
        updateTaskStatus(file_path)
    elif(userInput=="6"):
        break
    else:
        console.print("[bold magenta]Invalid Options[/bold magenta] ") 

