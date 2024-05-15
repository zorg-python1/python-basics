class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a
        else:
            return a + b

# Creating an object of Calculator class
calc = Calculator()

# Calling the add method with different numbers of arguments
print(calc.add(2, 3))  # Output: 5
print(calc.add(2))     # Output: 2 (default parameter used)
