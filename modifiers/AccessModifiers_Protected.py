# Protected modifier
# Special type of modifier in python starts with '_' single underscore is called protected modifier
# only accessible from the class protected functions
# [_name, _age, _salary, def _displayNameAndAge(): ]
from AccessModifiers_Private import Employee
from AccessModifires_Default import ZSolution
class Employee:
    # protected Data Members
    _name = None
    _age = None
    _salary = None

    # constractor
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    # Projected member of function
    def _displayNameAndBranch(self):
        print("Values from Protected members.")
        print("Name is : ", self._name)
        print("Age is : ", self._age)


# Derived Class
class EmployeeSalary(Employee):

    # constractor
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age, salary)

    # public member function
    def displayDetails(self):
        # accessing protected member
        print("Derive values of protected members.")
        print("Salary is : ", self._salary)

        # Accssing protected member function
        self._displayNameAndBranch()





# Create object for derive class
obj = EmployeeSalary("Miraz", 3, 12365)

# Calling public member functions
obj.displayDetails()



