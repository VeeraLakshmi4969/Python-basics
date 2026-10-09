path = "C:/Users/NANI/Desktop/Python/output.txt"
try:
    
    with open(path,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You have no permission to read this")
    
    
# FOR JSON FILE
import json
path = "C:/Users/NANI/Desktop/Python/output.json"
try:
    
    with open(path,'r') as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You have no permission to read this")


# For csv

import csv
path = "C:/Users/NANI/Desktop/Python/output.csv"
try:
    
    with open(path,'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(line[1])
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You have no permission to read this")
