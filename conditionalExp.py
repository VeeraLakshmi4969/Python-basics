# conditional expression =  one line shortcut for the if-else statement(Ternary Operator)
#             Print or assign one of two values based on condition
#             x if conditon else y


num = -2
print("positive" if num>0 else "negative")

num2 = 5
result = "even" if num2 % 2 == 0 else "odd"
print(result)   
 
maxNum = num if num > num2 else num2
minNum = num if num < num2 else num2
print( maxNum)
print(minNum)

age =20
print("Adult" if age>=18 else "child")

weather = 25
print("Sunny" if weather>=25 else "Cold")

User_role = "guest"
Access = "Full Access" if User_role == "admin" else "Limited Access"
print(Access)