# input() = A function that prompts the user to enter data
#           Returns the entered data as string
name = input("What is  your name:")
print(f"Hello {name}")
age = input("How old are you?")
print(f"You are age {age} old")
print("Happy Birthday")
age = int(age)+1
# OR age = int(input("How old are you?"))
print(f"Now you are {age} old")