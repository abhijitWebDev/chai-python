# store user age in a variable
user_age = int(input("Please enter your age: "))

# define the day
day = 'wednesday'

# get price
price = 12 if user_age >= 18 else 8


# discount
if day == "wednesday":
    price -= 2
# compare the age and day and allocate price

print("Ticket price for you is $", price)