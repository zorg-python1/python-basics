class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def drive(self):
    print("The car is driving.")

  def stop(self):
    print("The car has stopped.")

car1 = Car("Toyota", "Corolla", 2023)
car2 = Car("Honda", "Civic", 2022)

print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Civic

car1.drive()  # Output: The car is driving.
car2.stop()  # Output: The car has stopped.