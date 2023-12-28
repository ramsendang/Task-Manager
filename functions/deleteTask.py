import json

def deleteTask(json_file_path, target_value):
    # Read JSON data from the json file path 
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Identify keys associated with the specified value
    keys_to_delete = [key for key, value in json_data.items() if any(v == target_value for v in value.values())]

    # Delete key-value pair(s) associated with the specified value
    for key_to_delete in keys_to_delete:
        del json_data[key_to_delete]

    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

