'''3. Lambda Functions
Write a lambda function that adds two numbers and test it.
Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.
'''

sum= lambda a,b:a+b
print(sum(3,4))

number = [1, 2, 3, 4, 5]
square = list(map(lambda x:x**2, number))

print(square)


