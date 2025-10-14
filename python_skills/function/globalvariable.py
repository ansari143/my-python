# can we modify global variable inside the function , yes we can do but use global keyword. but best bractice to not use the global variable much, becuase 

def sum(a,b):
    print("summing the number")
    c = a+b 
    global z
    z=2
    return c


#z=10
print(sum(2,5))
print(z)