# Tuple = () ordered and unchangeable. Duplicates OK. FASTER than list

colors = ("red","blue","green","yellow")
print(len(colors))
print("blue" in colors)
# colors.add("pink") not works because un changeable

print(colors.index("pink"))
print(colors.count("green"))