# dictionary = a collection fo {key:value} pairs ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}

# use dir(capitals) to know the all methods and attributes of dictionary
# use help(capitals) to know the description of  all methods and attributes of dictionary

print(capitals.get("India"))
print(capitals.get("Japan"))
print(capitals.get("New Delhi"))



if capitals.get("Russia"):
    print("That capital exists.")
else:
    print("That capital does not exist.")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
capitals.pop("China")
capitals.popitem()
# it will delete latestly added element
# capitals.clear()
print(capitals)

keys = capitals.keys()

print(keys)

for key in keys:
    print(key)
    # OR

for k in capitals.keys():
    print(k)

values = capitals.values()
for value in values:
    print(value)

# items = capitals.items()
# print(items)
# it will return 2d list of Tuple

# OR

for key,value in capitals.items():
    print(f"{key} : {value}")