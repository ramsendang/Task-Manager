from rich.console import Console
from rich.table import Table
import uuid
from functions.deleteTask import deleteTask
from functions.readjson import readJson
from functions.userInput import getDate 
from functions.userInput import getTaskName
from functions.userInput import getTaskDetails
from functions.userInput import getStatus
from functions.insertJson import insertJson
from functions.updateTask import updateTask
from functions.status import updateStatus
console = Console()
def creatTask(file_path):
    console.print("Your have selected oution 1 (Add a Task). Please Enter the requested information to add a task ")
    # creating a unique task id 
    unique_number = uuid.uuid4()
    taskid = str(unique_number)
    # calling a functions to add task name, task details, due date and status
    taskName = getTaskName()
    taskDetails = getTaskDetails()
    dueDate = getDate()
    dueDate = str(dueDate)
    status = getStatus()
    # storing the user input into the python dictionary 
    task = {
        "task" : taskName,
        "details": taskDetails,
        "due date": dueDate,
        "status" : status
    }
    tasks = {
        taskid : task
    }
    # calling a function to add a task into the json file 
    insertJson(tasks, file_path)

def printTask(file_path):
    console.print("Your have selected oution 2 (View all the Task). ")
    print(f"Your Tasks are as follows")
    
    # creating the table 
    viewTable = Table(title ="Tast List View")

    # defining the column of the table 
    viewTable.add_column("Task", style="cyan", justify="center")
    viewTable.add_column("Description", style="cyan", justify="center")
    viewTable.add_column("Due Date", style="cyan", justify="center")
    viewTable.add_column("Status", style="cyan", justify="center")

    # fetching the data form the json file and adding it in the table row 
    file = readJson(file_path)
    for key, entry in file.items():
        viewTable.add_row(entry["task"], entry["details"], entry["due date"], entry["status"])
    console.print(viewTable)

def deleteTasks(file_path):
    print(f"you have selected option 3. Please follow the instruction below to delete a task")
    # read file from the json 
    jsonFile = readJson(file_path)
    # creates a table 
    table = Table(title="Task List")
    table.add_column("Options", style="cyan", justify="center")
    # filling the data in the row 
    for key, entry in jsonFile.items():
        table.add_row(entry['task'])
    console.print(table)
    # requesting user to enter the task name 
    deleteTaskString = input("Please Enter the task name which you want to delete : ")
    deleteTaskString = deleteTaskString.strip()
    # deleting the task 
    deleteTask(file_path, deleteTaskString)
    console.print("[bold magenta]Task Deleted Successfully : [/bold magenta] ")

def updateTasks(file_path):
    console.print("Your have selected oution 4 (Update a task). Please Enter the requested information to update a task ")
    # fetch already available task form the json 
    jsonFile = readJson(file_path)
    # creates the table 
    updateTable = Table(title="Tasks for Update")
    updateTable.add_column("Tasks", style="cyan")
    # fill the table row with the data from the json file 
    for key, entry in jsonFile.items():
        updateTable.add_row(entry['task'])
    console.print(updateTable)
    # process the update functionality 
    updateOption = input("Enter the available task for update : ")
    updatedValue = input("Enter the new task name that you want to update")
    # update the value 
    updateTask(file_path, updateOption, updatedValue)
    console.print("[bold magenta]Task Updated Successfully : [/bold magenta] ")

def updateTaskStatus(file_path):
    console.print("[bold magenta]Your have selected oution 5 (Update status). Please Enter the requested information to update status [/bold magenta]")
    # displays the available task for the json file 
    jsonFile = readJson(file_path)
    # creates the table 
    updateTable = Table(title="Tasks for Update")
    updateTable.add_column("Tasks", style="cyan")
    updateTable.add_column("Status", style="cyan")
    # fill the table row with the json data 
    for key, entry in jsonFile.items():
        updateTable.add_row(entry['task'], entry['status'])
    console.print(updateTable)   
    # request user for their choice 
    selectTask = input("Enter the available task name for updating it's status : ")
    newStatus = input("Enter your new Status for the task : ")
    # update the status 
    updateStatus(file_path, selectTask, newStatus)
    print("Status Updated Successfully")