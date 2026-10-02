# "Duck Typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methos
#                 "If it looks like a duck and quacks like duck, it must be a duck"

class Animal:
    alive = True
    
class Dog(Animal):
    def speak():
        return "Meow"
class Cat(Animal):
    def speak():
        return "Boww"
class Car:
    alive=False
    def speak():
        return "pee"
animals=[Cat,Dog,Car]
for x in animals:
    print(x.speak())
    print(x.alive)