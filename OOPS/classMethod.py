# Class Method = Allow operations related to the class itself
# Takes (cls) as the first parameter which represent class it self

class Stu:
    count = 0
    tot_gpa=0
    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa
        Stu.count +=1
        Stu.tot_gpa +=gpa
    def info(self):
        return f"{self.name} has {self.gpa} gpa"
    @classmethod
    def cls_count(cls):
        return cls.count
    @classmethod
    def totalGpa(cls):
        return cls.tot_gpa
    @classmethod
    def avg__gpa(cls):
        return f"{cls.tot_gpa/cls.count}"
stu1 = Stu("Nani",(9.9))
stu2 = Stu("Mahadev",8.2)
print(Stu.totalGpa())
print(Stu.tot_gpa)
print(Stu.cls_count())
print(Stu.avg__gpa())