# if name == main: (This script can be imported OR run standalone)
#                   Functions and classes in this module can be reused without the main block of code executing
# https://chatgpt.com/share/6a3a6c97-f1a8-83e8-908a-5d877118cfa2
# from ifStmt2 import *

# print(__name__)
# if __name__=='__main__':
#     print("This is first file")
    
print("This is another example")
    
def fav_food(food):
    print(f"Your favorite food is {food}")
def main():
    fav_food("Biryani")
    print("Goodbye!")
    
if __name__=='__main__':
    main()
