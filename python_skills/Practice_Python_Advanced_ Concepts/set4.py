'''Create a class Book with attributes title and author .
Implement __str__() so that printing the object displays "Title by
Author" .
Implement __len__() so that len(book) returns the length of the title.
Create two Book objects and test these methods.
'''
class Book:
    def __init__(self,title, author ):
        self.title = title
        self.author = author
    def __str__(self):
        print(f"{ self.title} by {self.author}")
    def __len__(self):
        result = len(self.title)
        return result
    
book1 = Book("Two states", "Chetan Bhagat")
book2 = Book("Python", "Ansari")
book1.__str__()
print(book1.__len__())
book2.__str__()
print(book2.__len__())