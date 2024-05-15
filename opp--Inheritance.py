class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        return f"{self.brand} {self.model} is driving."

# Creating an object of class Car
my_car = Car("Toyota", "Camry", 2020)

# Accessing attributes and calling methods
print(my_car.brand)  # Output: Toyota
print(my_car.drive())  # Output: Toyota Camry is driving.

############################################################

#Example 2: Inheritance 

class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.brand} {self.model} is charging."

# Creating an object of class ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

# Accessing attributes and calling methods
print(my_electric_car.year)  # Output: 2022
print(my_electric_car.charge())  # Output: Tesla Model S is charging.