#  nested loop = a loop within another loop (outer,inner)
#                outer loop:
#                   inner loop:


rows =  int(input("Enter the no of rows you want: "))
colmn = int(input("Enter the no of colmns you want: "))
symbol = input("Enter which symbol do you want to print: ")
for z in range(rows):
    for x in range(colmn):
        print(symbol, end=" ")
    print()