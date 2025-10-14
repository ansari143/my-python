#input the number
num = int(input("enter the number to reverse ..\n"))

rev = 0
while num>0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10
print("reverse number", rev)