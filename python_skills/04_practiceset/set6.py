''' 6. Variable Scope and Docstrings
Write a function increment() that has a local variable counter initialized to
0 and increments it by 1 each time it is called. Observe whether the value
persists across function calls.
Write a function multiply(a, b) that has a proper docstring explaining what
it does. Then use help(multiply) to display the docstring '''

def increment():
    x = 0
    x += 1
    print("counter=", x)

increment() 
increment()
increment() 
increment()
increment() 
increment()

def multiply(a, b):
    """
    multiply(a, b)

    This function takes two numbers 'a' and 'b' as input
    and returns their product.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

# Example usage
result = multiply(5, 3)
print("Result:", result, multiply.__doc__)

# Display the docstring using help()
help(multiply)