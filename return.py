# POSITIONAL ARGUMENTS

# return = statement used to end a function
#          and send a result back to the caller

# Positional Arguments = These are the standard arguments where order strictly matters. When calling the function, Python maps the arguments to the parameters based on their exact sequence.
#                     1. positional, 2.Default, 3. keyword, 4.arbitrary

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(5,6))
print(subtract(5,6))
print(multiply(5,6))
print(divide(5,6))


# EXAMPLE

def create_name(first,last):
    first = first.title()
    last = last.title()
    # capitalize capitals a very first letter
    # title capitalizes first letter of every word
    return first + " " + last
full_name = create_name("veera lakshmi","oleti")
print(full_name)