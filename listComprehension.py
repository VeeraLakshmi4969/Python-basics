# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

# List comprehension 

doubles = [x *2 for x in range(1,11)]
# x*2 multiple of 2
# x**2 x power 2
print(doubles)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [z*z for z in range(1,11)]
print(squares)

# EXAMPLE 2

fruits = ["apple","banana","coconut","orange"]
fruits = [x.upper() for x in fruits]
print(fruits)

firstChar = [x[0] for x in fruits]
print(firstChar)

# EXAMPLE 3

numbers = [-2,3,5,-9,-6,1]

positive_nums = [num for num in numbers if num >=0]
negitive_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2 == 0]
odd_nums = [num for num in numbers if num%2 != 0]
print(positive_nums)
print(negitive_nums)
print(even_nums)
print(odd_nums)

# EXAMPLE 3

marks = [33,89,67,54,3,66,90,99,45]
good_marks  = [x for x in marks if 45<=x]
print(good_marks)