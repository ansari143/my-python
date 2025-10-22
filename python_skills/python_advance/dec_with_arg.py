def repeat(n):
    def decoratot(fun):
        def wrapper(a):
            for i in range(n):
                fun(a)

        return wrapper
    return decoratot
@repeat(7)
def say_hello(a):
    print("Say hello", a)


say_hello("Harry")