class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function to make the animal speak
def make_animal_speak(animal):
    return animal.speak()

# Creating objects of different classes
dog = Dog()
cat = Cat()

# Calling the function with different objects
print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!
