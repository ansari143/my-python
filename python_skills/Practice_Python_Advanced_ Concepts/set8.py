'''
Write a function sum_all(*args) that accepts any number of integers and
returns their sum.
Write a function print_details(**kwargs) that prints key-value pairs passed
as arguments, for example:

print_details(name="Alice", age=25, city="Delhi")
# Output:
# name: Alice
# age: 25
# city: Delhi'''

def sum_all(*args):
    total = 0
    for x in args:
        total+=x
    return total

print(sum_all(1,2,3,3))

def print_details(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to print_details 
    for item in kwargs.keys():
        print(f"{item} : {kwargs[item]}")

print_details(name="Alice", age=25, city="Delhi")
