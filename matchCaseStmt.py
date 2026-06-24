# Match case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            print("it is sunday")
        case 2:
            print("it is monday")
        case 3:
            print("it is tuesday")
        case 4:
            print("it is wednesday")
        case 5:
            print("it is thursday")
        case 6:
            print("it is friday")
        case 7:
            print("it is saturday")
        case _:
        # It work like wild card entry(else)
            print("Not a valid day.")
            
day_of_week(1)

# EXAMPLE 2

def week_end(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case "tuesday":
            return False
        case "wednesday":
            return False
        case "thursday":
            return False
        case "friday":
            return False
        case "saturday":
            return True
        case _:
        # It work like wild card entry(else)
            return False
            
print(week_end("sunday"))

# Another way

def week_end(day):
    match day:
        case "sunday" | "saturday":
            return True
        case "monday" | "tuesday" | "wednesday" |"thursday" |"friday":
            return False
        
print(week_end("thursday"))


