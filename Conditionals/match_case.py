color = input("Enter the color: ")
match color:
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case "red":
        print("Stop")
    case _ :
        print("Invalid color")