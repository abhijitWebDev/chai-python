from hello import chai, square;

chai("Ginger tea");
square(4);

chai_one = "hello";
chai_three = "Masala chai";


# def main():
#     i = 1
#     while i < 5:  # Added colon here
#         i = i + 2
#         print(i)
#     print("Hello")

# main()

chai_types= {"Masala":"Spicy", "Ginger":"Zesty", "Green-Tea":"Mild"}
print(chai_types)
print(chai_types["Masala"])
print(chai_types.get("Gingery"))
chai_types["Ginger"] = "Fresh"
print(chai_types)



# for chai in chai_types:
#     print("Hello from chai",chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("Masala hai")

chai_types["Earl grey"] = "Citrus"

print(chai_types)

chai_types.pop("Ginger")

print(chai_types)

chai_types.popitem()

print(chai_types)

del chai_types["Green-Tea"]

print(chai_types)

chai_types_copy = chai_types.copy()

print(chai_types_copy)

tea_shop = {
    "Chai" : {
        "Masala":"Spicy", "Ginger": "Zesty"
    },
    "Tea": {
        "Green":"Mild", "Black":"Strong"
    }
}

print(tea_shop["Chai"]["Masala"])

squared_nums = {x: x**2 for x in range(6)} # type: ignore

print(squared_nums)
squared_nums.clear()
print(squared_nums)
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delecious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

# Tuples
tea_tuples = ("Black Tea", "Green Tea", "Oolon Tea")
print(tea_tuples[0])



