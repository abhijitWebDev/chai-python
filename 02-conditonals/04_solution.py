fruit = input("Please enter the fruit: ")
color = input("Please enter the color of banana: ")
if fruit == "Banana":
    if color == "Green":
        status = "Unripe"
        print("The banana is ", status)
    elif color == "Yellow":
        status = "Ripe"
        print("The banana is ", status)
    elif color == "Brown":
        status = "OverRipe"
        print("The banana is ", status)
else:
    status = "Unknown"
    quit()