'''
start with numbers = [5, 2, 9, 1, 7] and do the following:
Sort the list in ascending order.
Append the number 10 to the list.

Remove the number 2 from the list.
Create a list names = ["Alice", "Bob", "Charlie"] and use the insert()
method to add "David" at index 1 .

'''
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)

names = ["Alice", "Bob", "Charlie"]
names.insert(1,"David")
print(names)


