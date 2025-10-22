'''2. Read, Write, and Append Files
Write a program that writes three lines of text to a file tasks.txt .
Open tasks.txt in append mode and add a new line "Task Completed!" .
Read the file and print all lines as a list using readlines()'''

# Step 1: Write three lines of text to a file
with open("tasks.txt", "w") as file:
    file.write("Learn Python Basics\n")
    file.write("Practice Coding Daily\n")
    file.write("Build Fun Projects\n")

# Step 2: Open the file in append mode and add a new line
with open("tasks.txt", "a") as file:
    file.write("Task Completed!\n")

# Step 3: Read the file and print all lines as a list
with open("tasks.txt", "r") as file:
    lines = file.readlines()

print(lines)

