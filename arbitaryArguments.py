# Arbitary Arguments

# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional, 2.Default, 3. keyword, 4.arbitrary

def add(*args):
    print(type(args))
    # tuple
    total =0
    for arg in args:
        print(arg, end=" ")
        total += arg
    print()
    print(f"total = {total}")
    print(args)
add(1,3,5,7)


# EXAMPLE 2

def user_name(*name):
    for x in name:
        print(x.title(),end=" ")
        
user_name("veera","lakshmi","oleti")
    
# **kwargs

def print_address(**kwargs):
    print(type(kwargs))
    # dictionary
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "Thilak Street",
              doorno = "445-34-5",
              state = "Andhar Pradesh",
              country = "India")


# EXAMPLE THREE COMBINATION OF BOTH ARGS KWARGS


def shipping(*args,**kwargs):
    # key word arguments should be followed by position so we must define in this order only
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        # actually if something is not found it return None.
    else:
        print(f"{kwargs.get('street')} {kwargs.get('city')}")
# we must use '' single quatations inside get methon why because python will confuse whether it is string or dictionary key
    print(f"{kwargs.get('state')} {kwargs.get(' country')} \n{kwargs.get('street')}")
shipping("Miss.","Oleti","Veera","Lakshmi",
            street = "Thilak Street",
            city = "kakinada",
            state = "Andhar Pradesh",
            country = "India")