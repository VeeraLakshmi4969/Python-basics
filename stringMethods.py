# # String Methods

# name = input("Enter your full name: ")
# result  = len(name)
# print(result)
# # finding first occurence of character
# result2 = name.find("e")
# print(result2)
# # finding last occurence of character so we use reversefind
# result3 =  name.rfind("e")
# print(result3)
# # if given character not present it return -1

# result4 = name.capitalize()
# print(result4)

# result5 = name.upper()
# print(result5)
# print(name.lower())

# print(name.isdigit())
# # it check weather string contain only numbers
# print(name.isalpha())
# # it check weather string contain only alphabets

phone_num = input("Enter your phone number: ")
print(phone_num.count("9"))
print(phone_num.replace("1","2"))
print(phone_num.replace("-",""))
print(phone_num.replace("-"," "))