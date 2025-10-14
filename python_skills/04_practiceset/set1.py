'''Write a function greet() that prints "Hello, Python Learner!" when
called.
Write a function square(num) that returns the square of a given number. Test
it with different numbers'''

def greet():
    '''It is a greeting function'''
    print("Hello, Python Learner!")

greet()

def square(num): 
    '''It is square of the number'''
    return num*num
print(square.__doc__, square(3))