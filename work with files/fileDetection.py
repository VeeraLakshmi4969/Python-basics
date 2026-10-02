# Python file detection


import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"This file {file_path} exists")
    if os.path.isfille(file_path):
        print(f"This is a {file_path} file")
    elif os.path.isdir(file_path):
        print(f"This is a {file_path} dictionary")
else:
    print("The location doesnot exist")