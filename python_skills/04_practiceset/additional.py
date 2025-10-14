'''Write a recursive function fibonacci(n) that prints the first n Fibonacci
numbers.
Write a function safe_divide(a, b) that returns the result of a / b , but
returns "Cannot divide by zero" if b is 0 .
Create a small module my_utils.py with a function is_even(n) that returns
True if n is even. Import and use it in another Python file.
'''

def fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
print(fibonacci(2))

def safe_divide(a, b):
    if(b==0):
        return "Cannot divide by zero"
    else:
        return a/b
    
print(safe_divide(8,9))

import my_utils

x = my_utils.is_even(2)

print(x)