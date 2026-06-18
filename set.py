# set  = {} unordered and immutablle(cannot replace), but Add/Remove OK. NO duplicates

vegies = {"potato","tomoto","bottleguard","bittergourd"}

print(len(vegies))
# NOT  print(vegies.len())
print("tomoto" in vegies)

# print(vegies[0]) not work because set is unordered

vegies.add("carrot")
print(vegies)

vegies.remove("bittergourd")
print(vegies)