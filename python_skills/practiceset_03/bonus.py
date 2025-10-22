'''Write a program that takes a list of numbers and removes all duplicates using
a set.
Given a dictionary of products and their prices, find the product with the
highest price.
Write a program that merges two dictionaries into one.
'''

numbers = [1,2,2,3,3,5]
list_set = set(numbers)
print(list_set)

products = {"banana": 34, "brush": 89, "Nailpaint":45}
for name, price in products.items():
    print(f"{name}: {price}")
x = products.values()
print(x)
y= list(x)
print(y)
highest_price_product = max(products,key=products.get)
print(products[highest_price_product])

# Two dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Print the result
print("Merged dictionary:", merged_dict)