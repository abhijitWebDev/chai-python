distance = int(input("Please enter the distance: "))

if distance < 3:
    activity = "walk 🚶"
elif distance <= 15:
    activity = "Bike 🚲"
else: 
    activity = "Car 🚗"
print("The mode of transport for you is", activity)