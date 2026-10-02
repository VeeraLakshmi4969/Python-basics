# Python writing files(.txt, .json, .csv)

file_text = "Good Morning Nani"

file_path = "C:\\Users\\NANI\\Desktop\\output.txt"

with open(file_path,"w") as file:
    # file, mode = w (write mode), x(also for write only it did not exist)
    # a for append , r for read
    file.write(file_text)
    print(f"{file_path} has created")


# file_text = "Good Morning Nani"

# file_path = "C:/Users/NANI/Desktop/output.txt"
# try:    
#     with open(file_path,"x") as file:
#     # file, mode = w (write mode), x(also for write only it did not exist)
#     # a for append , r for read
#         file.write(file_text)
#         print(f"{file_path} has created")
# except Exception:
#     # or FileExistsError
#     print("This file already exists")
    
    
file_text = "This is appended text. "
text = " we execute when it append"
file_path = "C:/Users/NANI/Desktop/output.txt"
    
with open(file_path,"a") as file:
    # file, mode = w (write mode), x(also for write only it did not exist)
    # a for append , r for read
    file.write("\n"+file_text+" "+text)
    print(f"{file_path} has sucessfully modified")



emp = ['nani',"mahadev","sriyansh","srinu","ramu"]
file_path = "output.txt"
   
with open(file_path,"a") as file:
    # file, mode = w (write mode), x(also for write only it did not exist)
    # a for append , r for read
    for emplo in emp:   
        file.write("\n"+emplo+" ")
    print(f"{file_path} has succesfully updated")
