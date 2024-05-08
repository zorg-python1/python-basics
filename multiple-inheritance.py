# Define two parent classes: Bird and Mammal
class Bird:
    def fly(self):
        return "Can fly"

class Mammal:
    def walk(self):
        return "Can walk"

# Define a subclass called Bat that inherits from both Bird and Mammal
class Bat(Bird, Mammal):
    def __init__(self, name):
        self.name = name

# Create an instance of Bat
bat = Bat("Batty")

# Call methods inherited from Bird
print(bat.fly())  # Output: Can fly

# Call methods inherited from Mammal
print(bat.walk())  # Output: Can walk

print(Bat.mro())
