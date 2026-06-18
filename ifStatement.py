# if = Do some code only if some conditon is True
# Else do something else

# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("you are too old to sign up!")
# elif age >= 18:
#     print("You are adult")
# elif age >= 10 and age < 18:
#     print("You are teenager")
# elif age <=0:
#     print("You haven't been born yet")
# else:
#     print("You are a kid!")



# name = input("Enter your name: ")
# if name == "":
#     print("Please enter your name: ")
# else:
#     print(f"Hello {name}")

forSale = False

if forSale:
    print("This item is for sale")
else:
    print("This item is not for sale")


user_input = input("Is item for sale? (True or False): ")
# .strip() removes spaces, .lower() converts "True"/"TRUE" to "true"
if user_input.strip().lower() == "true":
    for_sale = True
else:
    for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")