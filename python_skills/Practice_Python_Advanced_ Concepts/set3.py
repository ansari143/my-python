'''Create a class MathUtils with:
A @staticmethod called add(a, b) that returns a + b .
A @classmethod called description(cls) that prints "This is a
utility class for math operations."
Call both methods without creating an object.'''

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


print(MathUtils.add(6,7))
MathUtils.description()