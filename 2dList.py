# 2dlist = [list1,list2,list3]


fruits = ["apple","banana","goa","watermelon"]
colors = ["red","blue","green","yellow","pink"]
subjects = ["maths","physics","chemistry"]

twodimensional = [fruits,subjects,colors]
print(twodimensional)

print(twodimensional[0])
print(twodimensional[1][2])

# for row wise print
for x in twodimensional:
    print(x)

# for print all the elements in 2d list
for x in twodimensional:
    for y in x:
        print(y)
# print(y, end=" ") print() for side by side printing


# twodim =[["apple","banana","goa","watermelon"],
# ["red","blue","green","yellow","pink"],
# ["maths","physics","chemistry"]]


twodim ={("apple","banana","goa","watermelon"),
         ("red","blue","green","yellow","pink"),
         ("maths","physics","chemistry")}
# we can create 2d list, 2d tuple, 2d set with list,tuple,set
print(twodim)