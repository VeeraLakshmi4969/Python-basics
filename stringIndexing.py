# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credict_num = "124-356-789-366"

print(credict_num[0])

# negative index consider reverse string
print(credict_num[-2])

print(credict_num[0 : 6])

print(credict_num[ : 6])

print(credict_num[7 : 9])

print(credict_num[7 : ])

print(credict_num[1 : 12 : 2])

print(credict_num[1 : : 3])


print(credict_num[: : 3])

last_digits= credict_num[-3:]
print(f"xxx-xxx-xxx-{last_digits}")

# it producee reverse of string
credict_num = credict_num[::-1]
print(credict_num)