def greet():
    print("Hello, world!")

# Call the function
greet()


def greet(name):
    print(f"Hello, {name}!")

# Call the function with a parameter
greet("Alice")


def add(a, b):
    return a + b

# Call the function and store the result
result = add(3, 5)
print("Result:", result)


def greet(name):
    """
    Greet the user with the given name.
    
    Args:
        name (str): The name of the user.
    """
    print(f"Hello, {name}!")

# Access the docstring using __doc__
print(greet.__doc__)

# Call the function
greet("Alice")



add = lambda a, b: a + b
result = add(3, 5)
print("Result:", result)
