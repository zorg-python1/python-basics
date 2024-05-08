# Define a list
my_list = [1, 2, 3, 4, 5]

# Get an iterator object from the list
my_iterator = iter(my_list)

# Iterate through the iterator using a loop
try:
    while True:
        # Get the next element from the iterator
        element = next(my_iterator)
        print(element)
except StopIteration:
    # StopIteration exception is raised when there are no more elements
    pass


# Python's for loop automatically handles iterator objects, making it convenient to iterate over collections without explicitly using iterator methods.
for element in my_list:
    print(element)
