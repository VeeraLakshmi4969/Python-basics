# Python writing files (.json)

import json
employee = {
    "name": "SpongeBod",
    "age":30,
    "job":"cook"
}

file_path = "C:\\Users\\NANI\\Desktop\\Python\\output.json"
try:
    with open(file_path,"w") as file:
        json.dump(employee, file, indent=8)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("File was already existed")