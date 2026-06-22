# # Membership operators = used to test whether a value or variable is found in a sequence (String, List, Tuple, Set or Dictionary)
# # 1.in 2.not in

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# letter = letter.upper()
# if letter in word:
#     print(F"{letter} was found")
# else:
#     print(f"{letter} was not found")
    
# # EXAMPLE 2

# students = {"Mahadev","Nani","Srinu","Ramu","Nagur","Maha"}

# student = input("Enter student name that you want to search: ")
# student = student.capitalize()

# if student in students:
#     print(f"{student} was found.")
# else:
#      print(f"{student} was not found.")
     
# # EXAMPLE 3

# grade =  {"Mahadev":"A",
#           "Nani":"B",
#           "Srinu":"C",
#           "Ramu":"D",
#           "Nagur":"E",
#           "Maha":"F"}

# student = input("Enter a student name that you want to know grade : ")

# if student in grade:
#     print(grade.get(student))
#     print(grade[student])
# # Square Brackets: grade[student]Requires the key to exist.
# # Raises a KeyError if missing.
# # Crashes your program if unhandled.
# # Get Method: grade.get(student)Safe from missing key errors.
# # Returns None if missing.
# # Prevents program crashes.
# # Accepts a custom default value.
# else:
#     print(f"{student} not found.")
    
# EXAMPLE 4

email = "4969.nanigmail.com"

if "@"in email and "." in email:
    print("Your mail is valid")
elif "@"not in email or "." not in email:
    print("Your mail is not valid")