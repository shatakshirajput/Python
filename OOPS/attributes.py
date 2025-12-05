# Attributes -> class attributes(belong to class, common for all the objects), instance attributes (belong to objects,differnt for all objects)

class Student:
    cllg_name = "ABC College"        # class attribute(can be accessed by class also)

    def __init__(self,name,cgpa):
        self.name = name    # instance attributes
        self.cgpa = cgpa    # instance attributes

stu1 = Student("Rahul",9.2)
stu2 = Student("Ram",7.5)

print(stu1.name)
print(stu1.cgpa)
print(stu1.cllg_name)
print(stu2.name)
print(stu2.cgpa)
print(stu2.cllg_name)
print(Student.cllg_name)

# if class and instance attributes are same then high priority will be accessed(instance for objects, class for class)