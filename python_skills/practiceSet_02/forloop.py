#Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

#Print the multiplication table of a number (entered by user).
num = int(input("Enter a number\n"))

for i in range(1,11):
    print(num,"X", i, "=", num*i)