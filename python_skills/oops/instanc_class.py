# constructure is used to initialized the object

class Employee:
    company = "TCS" # this is class attribute
    def __init__(self, salary, name, bond, company):
        self.salary = salary # create instance attribute of name 
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"Employee name is {self.name} salary is {self.get_salary()} and bond is for {self.bond}")

e1 = Employee(40000,"Ansari", 4, "IBM")
print(e1.name)
print(e1.get_salary())
e1.get_info()
print(e1.company) #will always print instance attribute wherever present
print(Employee.company) #will always print class attribute

#object itroespection
print(dir(e1))




