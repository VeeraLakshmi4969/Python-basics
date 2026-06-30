# Keyword Arguments = Keyword arguments are passed by explicitly naming the parameter during the function call. Because you specify exactly which parameter the value belongs to, the order no longer matters.
#                     1. positional, 2.Default, 3. keyword, 4.arbitrary
 
 
def hello(greeting, title, first, last):
    first = first.title()
    last = last.title()
    title = title.capitalize()
    # here title is Mrs. Mr. Miss. 
    print(f"{greeting} {title}{first} {last}")
    
# keyword arguments should follow positional arguments
hello("Good Morning.",title="Miss.",last="oleti",first="veera lakshmi")

# import time
# for x in range(1,11):
#     print(x)
#     time.sleep(1)

# print("1","2","3","4","5",sep="^")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,last=234,first=567,area=890)

print(phone_num)
