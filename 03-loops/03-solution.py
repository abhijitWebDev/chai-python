num = int(input("Please enter the number of which you want the table of : "))

for i in range(1, 11):
    if(i == 5):
        continue
    print(num, 'x', i, '=', num * i)

