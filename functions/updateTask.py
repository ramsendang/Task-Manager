import json

def updateTask(json_file_path, target_value, new_value):
    # Read JSON data from the specified json file in json_file_path
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # search keys associated with the specified targeted value
    keys_to_update = [key for key, value in json_data.items() if any(v == target_value for v in value.values())]

    # Update value for searched keys
    for key_to_update in keys_to_update:
        json_data[key_to_update]['task'] = new_value  # Updating the value for task.

    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

