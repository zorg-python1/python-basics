# Example of integer to float conversion
num_int = 10
num_float = float(num_int)
print(num_float)  # Output: 10.0

# Example of float to integer conversion
num_float = 10.5
num_int = int(num_float)
print(num_int)  # Output: 10

# Example of string to integer/float conversion
str_num = '20'
num_int = int(str_num)
num_float = float(str_num)
print(num_int, num_float)  # Output: 20 20.0

# Example of integer/float to string conversion
num_int = 30
num_float = 30.5
str_num_int = str(num_int)
str_num_float = str(num_float)
print(str_num_int, str_num_float)  # Output: '30' '30.5'

# Example of list to tuple conversion
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Example of tuple to list conversion
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4]

# Example of boolean to integer conversion
bool_true = True
bool_false = False
int_true = int(bool_true)
int_false = int(bool_false)
print(int_true, int_false)  # Output: 1 0

dict_value = {'a': 1, 'b': 2, 'c': 3}
list_value = list(dict_value.items())
print(list_value)  # Output: [('a', 1), ('b', 2), ('c', 3)]

list_value = [('a', 1), ('b', 2), ('c', 3)]
dict_value = dict(list_value)
print(dict_value)  # Output: {'a': 1, 'b': 2, 'c': 3}

bool_value = True
int_value = int(bool_value)
print(int_value)  # Output: 1

int_value = 1
bool_value = bool(int_value)
print(bool_value)  # Output: True

str_value = 'True'
bool_value = bool(str_value)
print(bool_value)  # Output: True