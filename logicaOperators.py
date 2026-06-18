# logical operators =  evaluate multiple conditions (or,and,not)
#        or = at least one condition must be True
#        and = both conditions must be True
#        not =  inverts the conditons(not False,not True)


# OR

# temp = 25
# is_raining = False

# if temp>35 or temp<10 or is_raining:
#     print("The Outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled. Come fast!")

#  AND

# temp = 25
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is sunny outside! ")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside!")
# elif 28 > temp > 0 and is_sunny:
#     print("It is warm outside!")
#     print("Weather is good today!")


# NOT

temp = 0
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside! ")
    print("Weather is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside!")
    print("Weather is sunny")
    print("Weather is good today!")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside!")
    print("Weather is sunny")
if temp >= 28 and  not is_sunny:
    print("It is hot outside! ")
    print("Weather is cloudy ouside")
elif temp <= 0 and is_sunny == False:
    print("It is cold outside!")
    print("Weather is cloudy ouside")
elif 28 > temp > 0 and  not is_sunny:
    print("It is warm outside!")
    print("Weather is cloudy ouside")
    print("Weather is good today!")
