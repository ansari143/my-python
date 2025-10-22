'''Write a program that reads a file and creates another file with all words
converted to uppercase.'''

with open("tasks.txt") as f:
    content = f.read()
    content_upper = content.upper()
    with open("task1.txt", "a") as nextfile:
        nextfile.write(content_upper)