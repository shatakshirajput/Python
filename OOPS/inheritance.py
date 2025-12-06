# Inheritance - Single Inheritance

class Employee:             # parent class
    start_time = "9AM"
    end_time = "5PM"

class Teacher(Employee):    # child class
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Data Science")

print(t1.subject, t1.start_time, t1.end_time)


# Multi-level Inheritance

class Employee:             
    start_time = "9AM"
    end_time = "5PM"

class AdminStaff(Employee):     
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):    
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(50_000, "CA")

print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)


# Multiple Inheritance

class Teacher:             
    def __init__(self, salary):
        self.salary = salary

class Student():     
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):    
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta = TA("Rahul", 50_000, 7.5)

print(ta.name, ta.salary, ta.gpa)