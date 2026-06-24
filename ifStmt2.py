# import ifStmt
# if __name__=="__main__":
#     print("This is second file")
# print(__name__)

# EXAMPLE 2
from ifStmt import *
print("This is second file")

def fav_juice(juice):
    print(f"Your favorite juice is {juice}")
def main():
    fav_juice("Sapota")
    fav_food("Biryani")
    print("good bye!")


    
if __name__=="__main__":
    main()