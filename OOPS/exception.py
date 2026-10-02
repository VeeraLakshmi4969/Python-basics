# Exception is an event that interupt normal flow of a program
# (ZeroDivisionError, TypeError, Value)
# To handle these we use exception handlers
# 1.try 2.except 3.finally


try:
    num  = int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You cant divisible by zero")
except ValueError:
    print("Enter number only")
except Exception:
    print("Something went wrong")
    
