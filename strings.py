# the below code fragment can be found in: colab
# Create a string
my_string = "Hello, world!"

# Access the first character of the string
first_character = my_string[0]
print(first_character)  # Output: H

# Access the last character of the string
last_character = my_string[-1]
print(last_character)  # Output: !

# Slice the string to get a substring
substring = my_string[1:5]
print(substring)  # Output: ello

# Concatenate two strings
new_string = my_string + " This is a new string."
print(new_string)  # Output: Hello, world! This is a new string.


#######################################################################

# the below code fragment can be found in:chatgpt
# Examples of creating strings
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''Triple quoted strings can span
multiple lines'''

# Example of accessing characters in a string
print(str1[0])  # Output: 'H'
print(str2[-1])  # Output: 'g'

# Example of string concatenation
full_str = str1 + ' ' + str2
print(full_str)  # Output: 'Hello, World! Python Programming'

# Example of string methods
print(str1.upper())  # Convert to uppercase
print(str2.lower())  # Convert to lowercase
print(str1.find('World'))  # Find the index of a substring
print(str2.split())  # Split the string into a list of words

# Example of string formatting
name = 'Alice'
age = 30
formatted_str = 'My name is {} and I am {} years old'.format(name, age)
print(formatted_str)  # Output: 'My name is Alice and I am 30 years old'

# Example of string slicing
print(str2[0:6])  # Output: 'Python'
print(str1[::-1])  # Reverse the string

# Example of using escape characters
escaped_str = 'This is a single quote: \' and a new line\nHere.'
print(escaped_str)

# Example of checking string properties
print(len(str1))  # Length of the string
print(str2.isalpha())  # Check if all characters are alphabetic

#######################################################################
# tabnine AI support
# Using % operator
age = 30
print("My age is %d years old" % age)  # Output: My age is 30 years old

# Using format() method
name = "John Doe"
print("My name is {}".format(name))  # Output: My name is John Doe# Uppercase
print("hello".upper())  # Output: HELLO

# Lowercase
print("HELLO".lower())  # Output: hello

# Count occurrences of a substring
print("hello world".count("l"))  # Output: 3

# Find the index of a substring
print("hello world".find("l"))  # Output: 1

# Replace a substring
print("hello world".replace("world", "universe"))  # Output: hello universe
# Single-quoted string
print('single-quoted string')

# Double-quoted string
print("double-quoted string")

# Triple-quoted string (single)
print('''triple-quoted string''')

# Triple-quoted string (double)
print ("""triple-quoted string""")

# Raw string
print(r'raw string with \n')  # Output: raw string with \n

name = "John Doe"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is John Doe and I am 30 years old.




#####################################################################
# Original string
original_string = "Hello, World!"

# Uppercase all characters
uppercase_string = original_string.upper()
print("Uppercase: ", uppercase_string)  # Output: HELLO, WORLD!

# Lowercase all characters
lowercase_string = original_string.lower()
print("Lowercase: ", lowercase_string)  # Output: hello, world!

# Count the number of occurrences of a substring
count_substring = original_string.count("o")
print("Count of 'o': ", count_substring)  # Output: 2

# Find the index of a substring
index_substring = original_string.find("Wor")
print("Index of 'Wor': ", index_substring)  # Output: 5

# Replace a substring
replaced_string = original_string.replace("World", "Earth")
print("Replaced: ", replaced_string)  # Output: Hello, Earth!

# Split the string into a list of substrings
split_string = original_string.split(", ")
print("Split: ", split_string)  # Output: ['Hello', ' World!']

# Join a list of substrings into a single string
joined_string = ", ".join(split_string)
print("Joined: ", joined_string)  # Output: Hello, World!