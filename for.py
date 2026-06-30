# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

# for x in range(1,11):
#     # ending is exclusive so we have to write n+1 
#     print(x)
# print("HAPPY NEW YEAR !")

# for x in reversed(range(1,11)):
#     # ending is exclusive so we have to white n+1 
#     print(x)
# print("HAPPY NEW YEAR !")

for x in range(1,11,2):
    print(x)

credit_card = "1234-2345-3456-4567"
for x in credit_card:
    print(x)

for x in range(1,21):
    if x==10:
        continue
    # else:
    #     print(x)
print(x)