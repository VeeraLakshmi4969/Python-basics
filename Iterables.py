# Iterables =  An object/collection that can return its elements one at a time,
#              allowing it to e iterated over in a loop

numbers = [1,2,3,4,5]

for number in numbers:
    print(number, end=" ")
    
numbers = (1,2,3,4,5)
for number in reversed(numbers):
    print(number)
    
# tuple and list is also iterable

fruits = {"Apple","Banana","Pineapple","Goa"}

for fruit in fruits:
    print(fruit)
    

    
# for fruit in reversed(fruits):
#     print(fruit)
# 'set' object is not reversible

# STRING
name = "Oleti Veera Lakshmi"

for character in name:
    print(character, end=" ")
print()

# DICTIONARIES
my_dictionary = {'A':1, 'B':2, 'C':3, 'D':4}

for key in my_dictionary:
    print(key, end=" ")
print()

for value in my_dictionary.values():
    print(value, end=" ")
print()

for key,value in my_dictionary.items():
    print(f"{key} : {value}")