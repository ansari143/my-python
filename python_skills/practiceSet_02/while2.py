#Write a program that keeps asking the user to enter a password until they enter the correct one.

correct_Password = "Password123"
user_input =""

while user_input != correct_Password :
    user_input = input("enter corret password")
    if(user_input != correct_Password ):
        print("password is not correct, try again\n")
print("access granted")
