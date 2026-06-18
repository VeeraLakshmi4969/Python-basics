# validate user input exercise
# 1 username should not contain 12 character
# 2 username must not contain spaces
# 3 username must not contain digits

username =  input("Enter your name: ")

if len(username)>12:
    print("Length should not exceed than 12 characters")
elif  username.find(" ")!= -1:
    # OR elif not username.find(" ") == -1 means if spaceses available
    print("User name should not contain Spaces")
elif not username.isalpha():
    print("user name should not contain digits")
else:
    print(f"Welcome {username}!")


   