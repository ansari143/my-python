'''Write a recursive function factorial(n) that returns the factorial of a
number.
Write a recursive function sum_of_digits(n) that returns the sum of all digits
of a given number.
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
         return n*factorial(n-1)
    
print(factorial(5))

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return(n%10)+sum_of_digits(n//10)
'''
123 = 1+2+3 = 6
123%10 = 3
123//10= 12
12%10 = 2
12//10= 1
'''

print(sum_of_digits(4567))