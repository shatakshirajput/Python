# Constructors -> __init__ to initialise the object(always get called when an object is made) 

class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

s1 = Student("ABC",9.2)
s2 = Student("XYZ",8.4)

print(s1.name)
print(s2.name)
print(s1.cgpa)
print(s2.cgpa)

print(s1.get_cgpa())

# types of contructors-> default(only one parameter(self)), parametrised