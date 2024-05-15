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


