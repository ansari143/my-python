'''Write a program that asks the user to enter a number and handles:
ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero
Create a custom exception NegativeNumberError and raise it when the user
enters a negative number.
'''
class NegativeNumberError(Exception):
    """Raised when the input number is negative"""
    pass

try:
    number = float(input("Enter a number\n"))
    if number <0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    result = 100/number
    print(f"Result: 100/number: {result}")

except ValueError:
    print(" it is not a numebr")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except NegativeNumberError as e:
    print(f"error: {e}")
finally:
    print("Program finished.")

