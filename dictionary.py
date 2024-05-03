# Create a dictionary with three key-value pairs
my_dict = {"name": "John Doe", "age": 30, "city": "New York"}

# Access the value associated with the "name" key
name = my_dict["name"]
print(name)  # Output: John Doe

# Add a new key-value pair to the dictionary
my_dict["occupation"] = "Software Engineer"

# Update the value associated with the "age" key
my_dict["age"] = 31

# Delete the "city" key-value pair from the dictionary
del my_dict["city"]

# Print the entire dictionary
print(my_dict)  # Output: {'name': 'John Doe', 'age': 31, 'occupation': 'Software Engineer'}