import json
def readJson(file_path):
    try: 
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    except:
        data = {}
    return data