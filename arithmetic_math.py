# Arthmetic operations
from math import floor
from unittest import result

friends = 5
# friends = friends +1
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends %= 2
# friends **= 3
# friends = friends ** 2
# this (**) means power
# print(friends)


# Math functions

x = 3.14
y = -4
z = 5
result = round(x)
# it produce closest big (up) number
print(result)
absaluteVal = abs(y)
print(absaluteVal)
# absaluteVal is a distance from 0
print(pow(4,2))
print(pow(z,3))
print(max(x,y,z))
print(min(x,y,z))
print(floor(x))
# it produce closest small (down) number


# import math
#
# x=100
# y=101.1
# print(math.pi)
# print(math.e)
# print(math.sqrt(x))
# print(math.ceil(y))
# # ceil is used to round point up

import math

radius = float(input("Enter radius: "))
# circle circumference = 2 pi r
result = 2 * math.pi * radius
print(result)
print(f"The circumference is: {round(result)} cm²")
print(round(result,2))
# it will round and display 2 decimal points

# import math
#
# radius = float(input("Enter radius:"))
# # circle area = pi r square
# Area = math.pi * radius ** 2
# print(Area)
# # OR
# Area2 = math.pi * pow(radius,2)
# print(f"The Area of the circle is: {Area2} cm²")
# print(f"The Area of the circle is: {round(Area2,3)} cm²")
# to get power 2 turn on numlock and hold alt key type 0178



import math

# hypotenuse(karnam) of right angle triangle
# c=square root(a²+b²)
a = float(input("Enter side A:"))
b = float(input("Enter side B:"))
c = pow(a,2)+pow(b,2)
d = math.sqrt(c)
print(f"The result is {d}")
# There are 2 types of functions one is built in another is userdefined
# for built in functions no need to import package
# for user defined functions we have to use classes