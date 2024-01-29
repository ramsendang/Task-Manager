from rich.console import Console
from rich.table import Table
console = Console()
# creates the command line options 
def createOptions():
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