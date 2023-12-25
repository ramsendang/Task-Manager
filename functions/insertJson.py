import json

def insertJson(data, file_path):
    try: 
        with open(file_path, "r") as json_file:
            jsondata = json.load(json_file)
    except:
        jsondata = {}
    jsondata.update(data)
    try:
        with open(file_path, "w") as json_file:
            print(f"Task added Successfully")
            json.dump(jsondata, json_file, indent=2)
    except:
        print("Task not added successfully")