#function keep the variable until returns

def sum(a,b): # a and b are local variable it can be access under only function
    c= a+b
    z = 1 # it creates local varible called z which is destroyed after this function returns 
    return c
    
print(sum(2,3))

z = 8 # z is global variable 
print (z)