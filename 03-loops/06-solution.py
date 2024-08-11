number= int(input("Please enter number: "))
factorial = 1

while(number > 0):
    factorial = factorial * number
    number = number - 1
print("The factorial value of number is ", factorial)