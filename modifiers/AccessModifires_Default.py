# Python modifier
# Public, protected, and private

# Public
# if any variable declear without any special symble is public means  accessible from any part of the program
# [name, id, email, def employee(): ] these are mentioned without any special symbl

class ZSolution:
    # call Constractor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # public member of function
    def displayName(self):
        print("Values from Default members.")
        print("Name of Employee : ", self.name)
        print("Age of the Employee : ", self.age)


# Create object
obj = ZSolution("Zaman", 20)


class Payments(ZSolution):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def finalDisplay(self):
        print("Derive values from default member of parent class.")
        print("Salary of Employee : ", self.salary)


# Create object of Payments
pay = Payments("Jamal", 20, 34000)

pay.displayName()
pay.finalDisplay()
