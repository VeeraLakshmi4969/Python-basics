# Static Methods = A method tht blong to a class rather than any object from that class(instance) usually used for general utility functions
# Instance Methods = Best for operations on objects

class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def details(self):
        return f"{self.name} is working as {self.role}"
    @staticmethod
    def is_valid(role):
        valid = ["mech eng","civil eng","software eng", "web dev"]
        return role in valid
emp1= Employee("nani","software eng")
print(Employee.is_valid("mech eng"))


# we may also write is_valid() without help of static method but why used this means:
# organize code and also no need of object to access if