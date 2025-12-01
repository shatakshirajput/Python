# format -> format() , f-strings

a = 2
b = 4

sum = a+b

print("Sum is {}".format(sum))  # normal foramtting
print("Sum of {}, {} is {}".format(a,b,sum))  # normal foramtting
print("Sum of {1}, {0} is {2}".format(b,a,sum))  # index based foramtting
print("Values are {a} and {b}".format(a = 2,b =10))  # value based foramtting

# f-strings
print(f"sum of {a} and {b} is {a+b}")