input_str = input("Please enter a valid string: ")

# using for loop
for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("charecter is: ", char)
        break


    
