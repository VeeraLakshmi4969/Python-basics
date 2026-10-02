# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# A predator is an animal that hunts, kills, and eats other animals
# Prey is the animal that gets hunted and eaten
# Flee means to run away from danger

# GRAND PARENT
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        
# PARENT CLASSES
class Prey(Animal):
    def flee(self):
        print(f"This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This animal is hunt")

# CHILD
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Robo")
hawk = Hawk("Dega")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

rabbit.sleep()