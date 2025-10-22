'''1. Combine a decorator with *args and **kwargs support so it can wrap any
function regardless of its parameters.
2. Implement __add__ in a Vector class so that adding two Vector objects
returns a new Vector with summed components.
3. Create a small program where invalid user input raises a custom exception,
logs the error, and continues execution instead of crashing.
'''
from functools import wraps
from typing import Any, Callable

def log_calls(func: Callable) -> Callable:
    """Decorator that logs calls and results for ANY signature."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"→ {func.__name__} args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} -> {result!r}")
        return result
    return wrapper

# Examples
@log_calls
def add(a, b): 
    return a + b

@log_calls
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"

@log_calls
def area(*sides, unit=None):
    if len(sides) != 2:
        raise ValueError("Provide width and height")
    w, h = sides
    return f"{w*h}{(' ' + unit) if unit else ''}"

