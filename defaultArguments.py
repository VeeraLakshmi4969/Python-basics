# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2.Default, 3. keyword, 4.arbitrary

def net_price(cost,discount=0,tax=0.05):
    return cost * (1-discount) * (1 +ta4x)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))


# EXERCISE

import time
# Parameters without defaults (required arguments) must always be placed first. 
# Parameters with defaults (optional arguments) must come last.
def timer( end,start=0):
    for x in range(start,end):
        print(x)
        time.sleep(1)
    print("Done !")
    
timer(15)
timer(30,15)