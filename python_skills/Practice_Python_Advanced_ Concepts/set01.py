'''Write a decorator logger that prints "Function is being called" before
the function runs. Use it to decorate a function say_hello() that prints
"Hello!" '''

def decorator(fun):
    def wrapper():
        print("Function is being called")
        fun()
    return wrapper

@decorator
def say_hello():
    print("Hello !")

say_hello()


'''Write a decorator timer that calculates how long a function takes to execute.
Test it with a function that sums numbers from 1 to 1,000,000.
'''

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} ran in {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def sum_to_one_million():
    # Sum 1..1_000_000 (inclusive)
    return sum(range(1, 1_000_001))

if __name__ == "__main__": #This condition ensures that the following code runs only if the file is executed directly, not when it’s imported as a module.
    total = sum_to_one_million()
    print("Total:", total)
