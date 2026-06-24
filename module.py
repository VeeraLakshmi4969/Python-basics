# # module = a file containing code you want to include in your program
# #          use 'import' to include a module(built in or your own)
# #          useful to break up a large program reusable separate files

# import math
# print(math.pi)
# # or
# import math as m
# print(m.pi)
# # or
# from math import e
# print(e)

# a,b,c,d,e =1,2,3,4,5

# print(math.e**a)
# print(math.e**b)
# print(math.e**c)
# print(math.e**d)
# print(math.e**e)

# example

import module2
result = module2.pi
print(result)
print(module2.square(3))
print(module2.cube(3))
print(module2.circumference(3))
print(module2.area(3))