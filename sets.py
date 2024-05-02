# Example of creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {'apple', 'banana', 'cherry'}
empty_set = set()

# Example of adding and removing elements from a set
set1.add(6)        # Adds 6 to set1
set2.remove('apple')  # Removes 'apple' from set2
set2.discard('pear')  # No error even if 'pear' is not in set2

# Example of set operations
set3 = {3, 4, 5, 6}
union_set = set1.union(set3)          # Union of set1 and set3
intersection_set = set1.intersection(set3)  # Intersection of set1 and set3
difference_set = set1.difference(set3)      # Set difference: elements in set1 but not in set3
symmetric_difference_set = set1.symmetric_difference(set3)  # Symmetric difference

# Example of set membership and iteration
if 4 in set1:
    print("4 is in set1")
for element in set2:
    print(element)



# Empty set
empty_set = set()

# Set with multiple elements
unique_names = {"Brad", "Eric", "John", "Alice"}

unique_names.add("Bob")
unique_names.remove("Alice")
unique_names.discard("Charlie")  # Will not raise an error

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2

# Intersection
intersection_set = set1 & set2

# Difference
difference_set = set1 - set2

# Symmetric difference
symmetric_difference_set = set1 ^ set2