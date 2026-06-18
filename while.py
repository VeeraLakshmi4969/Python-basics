#While loop =  execute some code WHILE some condition remains true


# name = input("Enter your full name: ")
# while name=="":
#     print("You did not entered your name. Please enter your name")
#     name = input("Enter your full name: ")
# print(f"Hello {name}")

# age =  int(input("Enter your age: "))
# while age > 0:
#     print("Age should not be zero")
#     age = int(input("Enter your age: "))
# print(f"Your age is {age}")

# order = input("Enter your order (q to quit): ")
# while not order=="q":
#     print(f"Your order {order} was palced")
#     order = input("Enter your order (q to quit): ")
# print("Byeeeee !.")

num = int(input("Enter a number between 1 to 100: "))
while num < 1 or num >100:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 to 100: "))
print(f"Your number is {num}")

