# Example of creating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'hello', 3.14, True)
empty_tuple = ()

# Example of accessing elements in a tuple
print(tuple1[0])  # Output: 1
print(tuple2[2])  # Output: 'cherry'

# Example of tuple slicing
print(tuple1[1:4])  # Output: (2, 3, 4)
print(tuple2[:2])   # Output: ('apple', 'banana')
print(tuple3[::2])  # Output: (1, 3.14)

# Example of tuple unpacking
tuple4 = ('John', 'Doe', 30)
first_name, last_name, age = tuple4
print(first_name)  # Output: 'John'
print(last_name)   # Output: 'Doe'
print(age)         # Output: 30

# Example of attempting to modify a tuple (will raise an error)
tuple2[0] = 'orange'  # Raises TypeError: 'tuple' object does not support item assignment
