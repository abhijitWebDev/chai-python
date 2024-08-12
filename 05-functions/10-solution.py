def factorial(number):
    if(number == 0): return
    if(number == 1): return 1
    return number * factorial(number-1)

result = factorial(8)
print(result)