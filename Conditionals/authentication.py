username = "admin"
password = "pass"
u = input("Enter the username:")
p = input("Enter the password:")
if ((u == username) and (p == password)):
    print("Logged in successfully!!!")
elif (u != username):
    print("Invalid username")
else:
    print("Invalid password")

#                                         OR

u = input("Enter the username:")
p = input("Enter the password:")
if ((u == username) and (p == password)):
    print("Logged in successfully!!!")
else:
    if (u != username):
        print("Invalid username")
    else:
        print("Invalid password")