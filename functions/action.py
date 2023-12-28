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
    unique_number = uuid.uuid4()
    taskid = str(unique_number)
    taskName = getTaskName()
    taskDetails = getTaskDetails()
    dueDate = getDate()
    dueDate = str(dueDate)
    status = getStatus()
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

def printTask(file_path):
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

def deleteTasks(file_path):
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

def updateTasks(file_path):
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

def updateTaskStatus(file_path):
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