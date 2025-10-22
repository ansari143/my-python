'''decorater is a function that takes a function,it create a new function inside its body(wrapper) then its retun the new functin(wrapper)'''

def decorator(fun):
    def wrapper():
        print("i am about to print hello....")
        fun()
        print("i am about to print hello....")
    return wrapper

@decorator
def say_hello():
    print("hello")

'''f= decorator(say_hello)
f()'''
say_hello()