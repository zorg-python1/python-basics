# Example 1: Using continue to skip even numbers

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through the numbers
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Skip even numbers
        continue
    # Print odd numbers
    print(num)



# Example 2: Using continue to skip specific values

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Iterate through the list
for fruit in fruits:
    # Check if the length of the fruit name is less than or equal to 5
    if len(fruit) <= 5:
        # Skip fruits with names of 5 characters or less
        continue
    # Print only fruits with names longer than 5 characters
    print(fruit)




# Print fruits from a list, skipping bananas

fruits = ["apple", "banana", "cherry", "date", "fig"]

for fruit in fruits:
    if fruit == "banana":  # Check if the fruit is banana
        continue  # Skip bananas
    print(fruit)  # Print other fruits
