# class - blueprint of object
# object - instance of class

class Student:
    sub = "Python"
    cllg = "ABC"
    year = "4th year"

s1 = Student()
s2 = Student()

print(type(s1))

print(s1)   # memory adddresses
print(s2)   # memory adddresses

# accessing info
print(s1.sub,s1.cllg,s1.year)
print(s2.sub,s2.cllg,s2.year)