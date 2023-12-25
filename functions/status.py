import json

def updateStatus(json_file_path, task_to_update, newStatus):
    # Read JSON data from the file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Update due date for the specified task
    for key, value in json_data.items():
        if value.get('task') == task_to_update:
            value['status'] = newStatus

    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
