password = input("Please enter a password: ")

passwordLength = len(password)

if passwordLength < 6:
    strength = "Weak"
elif passwordLength <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("The password you have entered is ", strength)