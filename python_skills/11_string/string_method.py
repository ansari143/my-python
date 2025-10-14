name = "ansari" #string are immutable 
#name[0] =R // Can not do because immutable
a = len(name)
print(a)
print(name.upper(), name) # orignal string name not change
print(name.lower(), name) # orignal string name not change
print(name.capitalize(), name) # orignal string name not change
print(name.title(), name) # orignal string name not change

text = " hello     worlds  Ansari "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

textfind = "Ansari is learning python to search AI"
print(textfind.find("is"))
print(textfind.replace("AI", "photo"))

textlist= "apple, Banana, Pineapples"
print(textlist.split(","))
print(",".join(['apple', ' Banana', ' Pineapples']))

textcheck = "Ansari"
print(textcheck.isalpha())
print(textcheck.isdigit())
print(textcheck.isalnum())
print(textcheck.isspace())