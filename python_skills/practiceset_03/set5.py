'''Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
and:
Print the value of "name" .
Change "grade" to "A+" .
Add a new key "city" with value "Delhi" .
Create a dictionary of three friends and their phone numbers. Use:
keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them
'''
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student.keys())
student["city"] = "Delhi"
print(student)

friends = {"ansari": 12345678,"rajan": 456789, "raju": 678590}
print("All keys", friends.keys())
print("All Values", friends.values())

for name, numbers in friends.items():
    print(f"{name}: {numbers}")
