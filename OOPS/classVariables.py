# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    
    passout = 2027
    numOfstud = 0
    class_year = 2026
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.numOfstud +=1
        
stud1 = Student("Mahadev",24)
stud2 = Student("Sriyansh",20)
stud3 = Student("Nani",20)

print(stud1.name, stud1.age)
print(stud2.passout)

print(Student.passout)

# we can call class variables by using class also
print(Student.numOfstud)

print(f"My graduating class of {Student.class_year} has {Student.numOfstud}")
print(stud1.name,stud2.name,stud3.name)
