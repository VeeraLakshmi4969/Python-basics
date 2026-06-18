# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :<= left justify
# :> = right justify
# :^ center align
# : + = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 120.34

print(f"Price 1 is {price1:.2f} Rs.")
print(f"Price 2 is {price2:.1f} Rs.")
print(f"Price 3 is {price3:.3f} Rs.")
# this 2f 1f 3f are no of decimal points
print(f"Price 3 is {round(price1,3)} Rs.")
print()

print(f"Price 1 is {price1:10} Rs.")
print(f"Price 2 is {price2:10} Rs.")
print(f"Price 3 is {price3:10} Rs.")
print()
# take 10 spaces include input
# if the actual length is more than 10  it leave it as it is

print(f"Price 1 is {price1:010} Rs.")
print(f"Price 2 is {price2:010} Rs.")
print(f"Price 3 is {price3:010} Rs.")
print()
# take 10 spaces include input with padded
# for padding we may use "0" only
# if we gave any other number then it take as string length

# right justify
print(f"Price 1 is {price1:>10} Rs.")
print(f"Price 2 is {price2:>10} Rs.")
print(f"Price 3 is {price3:>10} Rs.")
print()


# left justify
print(f"Price 1 is {price1:<10} Rs.")
print(f"Price 2 is {price2:<10} Rs.")
print(f"Price 3 is {price3:<10} Rs.")
print()

# center align
print(f"Price 1 is {price1:^10} Rs.")
print(f"Price 2 is {price2:^10} Rs.")
print(f"Price 3 is {price3:^10} Rs.")
print()

# for positive numbers it assign positive
print(f"Price 1 is {price1:+} Rs.")
print(f"Price 2 is {price2:+} Rs.")
print(f"Price 3 is {price3:+} Rs.")
print()


# for positive numbers it assign positive
print(f"Price 1 is {price1: } Rs.")
print(f"Price 2 is {price2: } Rs.")
print(f"Price 3 is {price3: } Rs.")
print()

# sperate thounds place by 3rd multiples
print(f"Price 1 is {price1:,} Rs.")
print(f"Price 2 is {price2:,} Rs.")
print(f"Price 3 is {price3:,} Rs.")
print()

# sperate thounds place by 3rd multiples
print(f"Price 1 is {price1:+,.2f} Rs.")
print(f"Price 2 is {price2:+,.2f} Rs.")
print(f"Price 3 is {price3:+,.2f} Rs.")
