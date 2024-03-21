# Base Class
class Animal:
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")

class Dog(Animal):
    def bark(self):
        print("I can bark ! Woo Woo!!!")

#create object of animal class
dog = Dog()
# Call method from parent class
dog.eat()
dog.sleep()

# call method from child class
dog.bark()

