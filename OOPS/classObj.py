# object  = A "bundle" of related attributes (variables) and methods(functions)
#           Ex. phone, cup, book
#           You need a "class " to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        # This is necessary line to create object
        # init means initiation
        # it is dunder menthod = double underscore
        
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
        # here self means what object we are working with
        
        
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
        
    def describe(self):
        return f"{self.model}\n{self.color}\n{self.year}"
        
car1 = Car("Tata",2026,"Gray",True)
car2 = Car("Mahindra",2025,"cream",False)
print(car1)
# It returns address of car1 object
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.stop()

print(car1.describe())
# Or
# we may another file car
# # class Car:
#     def __init__(self, model, year, color, for_sale):
#         # This is necessary line to create object
#         # init means initiation
#         # it is dunder menthod = double underscore
        
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


# store the all code there and import it

# from car import Car