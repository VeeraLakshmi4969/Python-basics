# Typecasting = the process of converting  a variable from one data type to another 
# str(),int(),float(),bool()
name = "Mahadev"
age=3
is_kid=True
weigth=12.6
print(type(name))
print(type(age))
print(type(is_kid))
print(type(weigth))

# Type conversion
age = float(age)
weigth = int(weigth)
print(age)
print(weigth)


age= age+10
print(age)

age=str(age)
print(age)
age = age + "10"
print(age)

name = bool(name)
print(name)
# Original name      bool(name) result    Reason
# "John"             True                 It is a string with text.
# "" (empty string)  False                There is no text/data inside.
# "0" (text zero)    True                 Any text inside quotes evaluates to True.
# 0 (number zero)    False                Numeric zero equates to False in Python.


name2 = ""
print(bool(name2))