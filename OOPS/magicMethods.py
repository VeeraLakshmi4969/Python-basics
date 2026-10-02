# Magic Methods is also known as tunder methods with double underscore
# __init__,__str__,__eq__,
# They are automatically called by many of pythons built_in operations
# They allow developers to define or customize behaviour of objects
class Book:
    def __init__(self,name,author,pageNums):
        self.name = name
        self.author = author
        self.pageNums=pageNums
    def __str__(self):
        return f"{self.name} was written by '{self.author}'"
    def __eq__(self,other):
        return self.name == other.name and self.author == other.author
    
    def __lt__(self,other):
        return self.pageNums < other.pageNums
    
    def __gt__(self,other):
        return self.pageNums > other.pageNums
    
    def __add__(self,other):
        return self.pageNums+ other.pageNums
    def __contains__(self,keywords):
        return keywords in self.name or keywords in self.author
    def __getitem__(self, key):
        if key=="author":
            return self.author
        elif key=="name":
            return self.name
        else:
            return f"{key} not found"
book1= Book("a,b", "Nani",105)
book2 =Book("b","Maha",300)
print (book1==book2)
print(book1)
print("a" in book2)