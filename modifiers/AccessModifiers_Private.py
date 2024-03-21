# Private Modifier
# Special type and most secure access  modifier is only accessible within the class
# To declare, add double underscore '__' before a member or variable
# [__name, __salary, __dept, def __employeeDetails(): ]

class Employee:
    #Private members variable
    __name = None
    __salary = None
    __dept = None

    # constractor
    def __init__(self, name, salary, dept):
        self.__name=name
        self.__salary=salary
        self.__dept=dept

    # private member function
    def __displayDetails(self):
        print("Values from Private members.")
        print("Name : ", self.__name)
        print("Salary : ", self.__salary)
        print("Dept : ",self.__dept)

    # Public member function for display result
    def finalDisplay(self):
        self.__displayDetails()

employee = Employee("Miraz", 32145, "Software Engineer")
employee.finalDisplay()

