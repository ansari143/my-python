'''
class is a blueprint or a template eg : form of an exam that contains name,age, electives, father's name etc
object : specific instance created from the template(class). eg form which conatins the data of Ansari

class contains data =attributs and method = functions
'''

class Employee:
    company ="IBM"

    def get_salary(self): #self is important here because self ia a way to reference 
                          #  the object of the class which is being created
        return 30000
    
e1 = Employee() # an object of class Employee is created here
print(e1.get_salary()) # employee e1's get salary method call

e2 = Employee()
print(e2.get_salary()) # employee e2's get salary method call


