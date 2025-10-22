'''Use the walrus operator to read input until the user enters "quit" . Print each
input as it is entered.
Use the walrus operator in a list comprehension to store lengths of words
from ["python", "rocks", "ai"] in a list while filtering out words shorter
than 4 characters.
'''
while (data:=input("enter the number\n")):
    print(data)
    if data == "q":
        break

words = ["python", "rocks", "ai"]
lengths = [length for w in words if (length := len(w)) >= 4]

print("Word lengths (≥4 characters):", lengths)

