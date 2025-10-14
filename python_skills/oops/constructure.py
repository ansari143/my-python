# constructure is used to initialized the object

class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"Employee name is {self.name} salary is {self.get_salary()} and bond is for {self.bond}")

e1 = Employee(40000,"Ansari", 4)
print(e1.name)
print(e1.get_salary())
e1.get_info()




