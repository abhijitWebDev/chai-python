score = 100

if score >= 101:
    print("Please verify your grade")
    quit()

# if score is between between 90 and 100 then assign A grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("The current grade is", grade )
