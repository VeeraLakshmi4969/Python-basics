# super() = Function used in a child class to call methods from a parent class(super Class).
#           Allows you to extend the functionality of the inherited methods
class Shapes:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else "empty"}")

class Circle(Shapes):
    def __init__(self,color, filled, radius):
        super().__init__(color,filled)
        # super init dunder method
        self.radius = radius
        
    def describe(self):
        # alt+0178
        print(f"It is a circle with an area of {3.14*self.radius*self.radius:.2f} cm²")
        super().describe()

class Square(Shapes):
    def __init__(self,color, filled, width):
        super().__init__(color,filled)
        self.width = width

    def describe(self):
        # alt+0178
        print(f"It is a squrare with an area of {self.width**2} cm²")
        super().describe()
        
class Triangle(Shapes):
    def __init__(self,color, filled, width , height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
    
    def describe(self):
        # alt+0178
        print(f"It is a Triangle with an area of {self.width*self.height/2} cm²")
        super().describe()
        
        
circle = Circle(color="red",filled=True,radius=2.3)
square = Square("pink",False,6)
triangle = Triangle("blue",True,6,7)
print(circle.color)
print(circle.filled)
print(circle.radius)

print(square.color)
print(square.filled)
print(square.width)

print(triangle.color)
print(triangle.filled)
print(triangle.width)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()