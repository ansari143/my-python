# st is unorder list with unique value enclose with {}
s = {1, 2,3,4}

print(s, type(s))
#print(s[3]) in set you can not access the elemement through index

s.add(3) # can not add dublicate
s.add(5)
s.remove(2) # if not present it will throw the error
s.discard(7) # if not present it will not throw the error
s.pop()
print(s, type(s))
