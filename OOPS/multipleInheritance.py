# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# A predator is an animal that hunts, kills, and eats other animals
# Prey is the animal that gets hunted and eaten
# Flee means to run away from danger
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunt")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
Hawk().hunt()
fish.hunt()
Fish().flee()