weather = input("Please mention weather: ")
weather = weather.capitalize()
print(weather)

if weather == "Sunny":
    activity = "Go for walk 🚶"
elif weather == "Rainy":
    activity = "Read a 📖"
elif weather == "Snowy":
    activity = "Build a ⛄"
else:
    activity = "Yet to be decided"
print(activity)