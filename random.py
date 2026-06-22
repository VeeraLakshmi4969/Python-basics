import random

print(random.random())
# it returns random float between 0 and 1.
print(random.randint(1,100))
# it returns random int with in the given range
#print(dir(random))

options = ("rock","paper","scissors")
option = random.choice(options)
print(option)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)

print(cards)