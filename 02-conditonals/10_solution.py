pet_species = input("Enter the species of the pet: ")
age= int(input("insert the age of the per: "))

if pet_species == "Dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Grown dog food"

if pet_species == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Baby cat Food"

print("The species is ", pet_species, "And the food recomended is ", food)

