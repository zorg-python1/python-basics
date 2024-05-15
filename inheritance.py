# # Define a superclass called Animal
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# # Define a subclass called Dog, inheriting from Animal
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# # Define another subclass called Cat, inheriting from Animal
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# # Create instances of Dog and Cat
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# # Call the speak method for each instance
# print(dog.speak())  # Output: Buddy says Woof!
# print(cat.speak())  # Output: Whiskers says Meow!



# Define a superclass called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass called Mammal, inheriting from Animal
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def speak(self):
        return f"{self.name} makes a sound."

# Define another subclass called Dog, inheriting from Mammal
class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Define another subclass called Cat, inheriting from Mammal
class Cat(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of Dog and Cat
dog = Dog("Buddy", "brown", "Labrador")
cat = Cat("Whiskers", "gray", "Siamese")

# Call the speak method for each instance
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
