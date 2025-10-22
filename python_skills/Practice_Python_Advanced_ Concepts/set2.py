'''Create a class Employee with a private attribute _salary .
Use @property to define a getter for salary .
Use @salary.setter to prevent setting negative values (print a warning
instead).
Create an object and test by setting positive and negative salaries.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    #getter for salary 
    @property
    def salary(self):
        return self._salary
    
    #setter for Salary 
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("⚠️ Warning: Salary cannot be negative!")
        else:
            self._salary = value
            print(f"✅ Salary updated to {self._salary}")


# --- Testing ---
emp1 = Employee("John", 50000)

print("Initial Salary:", emp1.salary)   # Uses getter

emp1.salary = 60000    # Valid (positive)
emp1.salary = -10000   # Invalid (negative)
print("Final Salary:", emp1.salary)
