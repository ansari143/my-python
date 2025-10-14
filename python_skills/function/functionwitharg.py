def add(a,b): # a and b are parameter
    x= a+b
    return x
c= add(1,2) # 1 and 2 are arguments
print(c)


def addthree(a,b,c=1):
    d= a+b+c
    return d
x = addthree(2,5,7) # c will be override
print(x)