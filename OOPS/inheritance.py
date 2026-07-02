# Inheritance =  Allows a  class to inherit attributes and methods from another class
#                Helps with code reusability and extensibility


class Animal:
    is_alive = True
    def __init__(self,name):
        self.name = name
        
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# class Mouse(Animal):
#     pass

# or

class Dog(Animal):
    def speak(self):
        print("Boww")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
        
class Mouse(Animal):
    def speak(self):
        print("quieeez")

dog = Dog("Tommy")
cat = Cat("Meow")
mouse = Mouse("Mickey")

print(dog.name)
cat.sleep()
mouse.eat()

dog.speak()
cat.speak()
mouse.speak()

