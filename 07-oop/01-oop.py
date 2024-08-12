class Car:
    totalCar = 0

    def __init__(self, brand, model):
        # Encapsulation
        self.__brand = brand
        self.__model = model
        # self.totalCar += 1
        Car.totalCar += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Disel"
    @staticmethod
    def genral_description():
        return "Cars are means of transport and are amazing"
    
    # Getter method
    def chai_brand(self):
        return self.__brand + "!"
    
    # Decorator
    @property
    def model(self):
        return self.__model

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Car, Battery, Engine):
    pass




# create object
# my_car = Car("Tata", "Tiago")
# my_car.model = "city"
# print(my_car.model)
# print(my_car.genral_description())
# print(Car.genral_description())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.full_name())

# Inheritance
# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_amazing_car.chai_brand())
# print(my_amazing_car.fuel_type())

# safari = Car("Tata", "Safari")
# nexon = Car("Tata", "Nexon")
# print(safari.fuel_type())
my_new_tesla = ElectricCarTwo("Toyota", "Camri")
print(my_new_tesla.engine_info(), my_new_tesla.battery_info())