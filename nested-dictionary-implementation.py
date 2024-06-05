nested_dict = {
    'person1': {
        'name': 'John',
        'age': 30,
        'address': {
            'city': 'New York',
            'state': 'NY'
        }
    },
    'person2': {
        'name': 'Jane',
        'age': 25,
        'address': {
            'city': 'Los Angeles',
            'state': 'CA'
        }
    }
}

# Accessing elements
print(nested_dict['person1']['name'])  # Output: John
print(nested_dict['person2']['address']['city'])  # Output: Los Angeles
################################################################

# Adding a new person
nested_dict['person3'] = {
    'name': 'Alice',
    'age': 28,
    'address': {
        'city': 'Chicago',
        'state': 'IL'
    }
}

# Modifying an existing entry
nested_dict['person1']['age'] = 31

print(nested_dict['person3'])
# Output: {'name': 'Alice', 'age': 28, 'address': {'city': 'Chicago', 'state': 'IL'}}
print(nested_dict['person1']['age'])  # Output: 31

################################################################

# Deleting a key-value pair
del nested_dict['person2']['address']['state']

# Deleting a whole person entry
del nested_dict['person3']

print(nested_dict)
# Output: {'person1': {'name': 'John', 'age': 31, 'address': {'city': 'New York'}}, 'person2': {'name': 'Jane', 'age': 25, 'address': {'city': 'Los Angeles'}}}

########################################################################

for person, details in nested_dict.items():
    print(f"Person: {person}")
    for key, value in details.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")

################################################################

students = {
    'Alice': {
        'math': 85,
        'science': 92,
        'english': 88
    },
    'Bob': {
        'math': 78,
        'science': 81,
        'english': 85
    },
    'Charlie': {
        'math': 95,
        'science': 89,
        'english': 92
    }
}

# Accessing Bob's science grade
print(students['Bob']['science'])  # Output: 81

# Adding a new subject grade for Alice
students['Alice']['history'] = 90

# Modifying Charlie's math grade
students['Charlie']['math'] = 97

# Deleting Bob's English grade
del students['Bob']['english']

print(students)
# Output: {'Alice': {'math': 85, 'science': 92, 'english': 88, 'history': 90}, 'Bob': {'math': 78, 'science': 81}, 'Charlie': {'math': 97, 'science': 89, 'english': 92}}
