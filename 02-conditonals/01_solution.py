# store age in variable
user_age = int(input("provide me the age: "))

# categorize the persons according to age group, below 13 child, 13 and above but less than 19 teenage, from 20 t0 59 Adult, and 60+ senior

if user_age < 13:
    print("You are a child")
elif user_age < 20:
    print("You are a teenager")
elif user_age < 60:
    print("You are an Adult")
else:
    print("You are a senior")