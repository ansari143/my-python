'''Write a function full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format "First Last" .

Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)
'''

def full_name(first, last):
    '''It will return full name'''
    return print(f"{first} {last}")

x = full_name("md", "Ansari")

def calculate_area(length, width=10):
    '''calulate the area'''
    areaOfrectangle = length * width
    return areaOfrectangle

print(calculate_area(3,5))
print(f"area of rectangle {calculate_area(3)}")
