# collection = single "variable " used to store multiple values
# list = [] ordered and changeable.Duplicates OK
# set  = {} unordered and immutablle, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER than list


fruits = ["apple","orange","banana","goa"]

print(fruits)
print(fruits[2])
print(fruits[0:1])
print(fruits[::2])
# 2 jumps means leave one item
# print(fruits[::-1])
print("apple" in fruits)

# fruits[0] = "pineapple"
# print(fruits)
# it overrides

fruits.append("kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.insert(0,"pineapple")
print(fruits)

# fruits.sort()
# print(fruits)
print(fruits.sort()) 

fruits.reverse()
print(fruits)

# fruits.clear()
# print(fruits)

print(fruits.index("apple"))
print(fruits.count("banana"))
# print(dir(fruits))
# here dir refers to directory these are the operation(methods and attributes) that we can perform on that type of date
# print(help(fruits))
# provide description for methods and attributes
# it the output of this not terminated enter "q"