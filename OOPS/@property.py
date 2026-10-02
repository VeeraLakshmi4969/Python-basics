# property decorator used to define a method as a property (it can be accessed like an attibute)
# Benifits: Add addition logic when read, write, and delete attributes
# Gives you getter, setter abd deleter Method

class Rect:
    def __init__(self,width,height):
        self._width=width
        self._height=height
        
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width=new_width
        else:
            print("width must be greater than zero")
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height=new_height
            print(self.height)
        else:
            print("height must be greater than zero")
    @width.deleter
    def width(self):
        del self._width   
        print("width has deleted")
    @height.deleter
    def height(self):
        del self._height   
        print("height has deleted")  
rec = Rect(5,6)
print(rec._width)
print(rec._height)
del rec.height
del rec.width
rec.height = 25
rec.width = 25
print(rec.width)
print(rec.height)