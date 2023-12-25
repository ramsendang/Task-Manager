import uuid
from rich.console import Console
from rich.table import Table
from functions.readjson import readJson
from functions.insertJson import insertJson
from functions.deleteTask import deleteTask
from functions.updateTask import updateTask
from functions.inputDate import getDate
from functions.status import updateStatus
file_path = "db.json"
console  = Console()
while True:
    # creating a command line interface showing users for available options
    table = Table(title="Options List")
    table.add_column("Options", style="cyan", justify="center")
    table.add_column("Option Description", style="yellow")
    table.add_row("1", "Add a Task")
    table.add_row("2", "View all the task")
    table.add_row("3", "Delete a task")
    table.add_row("4", "Update a task")
    table.add_row("5", "Update Status")
    table.add_row("6", "Quit")
    console.print(table)
    
    userInput = input("Enter a choice : ")
    userInput = userInput.strip()
    if(userInput == "1"):
        unique_number = uuid.uuid4()
        taskid = str(unique_number)
        taskName = input("Enter a Task Name : ")
        print(f"Your task is {taskName}")
        taskDetails = input("Enter a Task Details : ")
        print(f"Your task description is {taskName}")
        dueDate = getDate()
        dueDate = str(dueDate)
        print(f"Your Task due date is {dueDate}")
        status = input("Enter the status of the task (e.g. Done, In Progeress, Not Started)")
        print(f"Your Task's status is {status}")
        task = {
            "task" : taskName,
            "details": taskDetails,
            "due date": dueDate,
            "status" : status
        }
        tasks = {
            taskid : task
        }
        insertJson(tasks, file_path)
        print(f"Task added Successfully")
    elif(userInput == "2"):
        print(f"Your Tasks are as follows")
        viewTable = Table(title ="Tast List View")
        viewTable.add_column("Task", style="cyan", justify="center")
        viewTable.add_column("Description", style="cyan", justify="center")
        viewTable.add_column("Due Date", style="cyan", justify="center")
        viewTable.add_column("Status", style="cyan", justify="center")
        file = readJson(file_path)
        for key, entry in file.items():
            viewTable.add_row(entry["task"], entry["details"], entry["due date"], entry["status"])
        console.print(viewTable)
    elif(userInput == "3"):
        jsonFile = readJson(file_path)
        table = Table(title="Task List")
        table.add_column("Options", style="cyan", justify="center")
        for key, entry in jsonFile.items():
            table.add_row(entry['task'])
        console.print(table)
        deleteTaskString = input(console.print("[bold magenta]Please Enter the task name which you want to delete : [/bold magenta] "))
        deleteTaskString = deleteTaskString.strip()
        deleteTask(file_path, deleteTaskString)
        console.print("[bold magenta]Task Deleted Successfully : [/bold magenta] ")
    elif(userInput == "4"):
        jsonFile = readJson(file_path)
        updateTable = Table(title="Tasks for Update")
        updateTable.add_column("Tasks", style="cyan")
        for key, entry in jsonFile.items():
            updateTable.add_row(entry['task'])
        console.print(updateTable)
        updateOption = input("Enter the available task for update : ")
        updatedValue = input("Enter the new task name that you want to update")
        updateTask(file_path, updateOption, updatedValue)
        console.print("[bold magenta]Task Updated Successfully : [/bold magenta] ")
    elif(userInput=="5"):
        jsonFile = readJson(file_path)
        updateTable = Table(title="Tasks for Update")
        updateTable.add_column("Tasks", style="cyan")
        updateTable.add_column("Status", style="cyan")

        for key, entry in jsonFile.items():
            updateTable.add_row(entry['task'], entry['status'])
        console.print(updateTable)   
        selectTask = input("Enter the available task name for updating it's status : ")
        newStatus = input("Enter your new Status for the task : ")
        updateStatus(file_path, selectTask, newStatus)
        print("Status Updated Successfully")
    elif(userInput=="6"):
        break
    else:
        print("Invalid options") 

