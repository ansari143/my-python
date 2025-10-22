'''1. File I/O Basics
Create a text file notes.txt using Python and write "Learning Python is
fun!" into it.
Open notes.txt , read its content, and print it to the console.'''

with open("notes.txt", "a") as f:
    content = "Learning Python is fun!"
    f.write(content)
    result = f.read()
    print(result)