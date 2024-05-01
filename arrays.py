from array import array

# Create an array of integers
int_array = array('i', [1, 2, 3, 4, 5])

# Create an array of doubles
double_array = array('d', [1.5, 2.5, 3.5, 4.5, 5.5])

# Access the first element of the array
print(int_array[0])  # Output: 1

# Access the last element of the array
print(double_array[-1])  # Output: 5.5

# Iterate over the integer array
for i in int_array:
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Iterate over the double array using an index
for i in range(len(double_array)):
    print(double_array[i])

# Output:
# 1.5
# 2.5
# 3.5
# 4.5
# 5.5

# Add an element to the end of the array
int_array.append(6)

# Output the updated array
print(int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Remove the last element from the array
int_array.pop()

# Output the updated array
print(int_array)  # Output: array('i', [1, 2, 3, 4, 5])

# Search for the element 3 in the array
index = int_array.index(3)

# Output the index of the element
print(index)  # Output: 2