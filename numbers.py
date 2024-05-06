# Integers are whole numbers, positive or negative.
int_value = 123
print(int_value)  # Output: 123# Floating-point numbers have a decimal point.

float_value = 123.456
print(float_value)  # Output: 123.456# Complex numbers have a real part and an imaginary part separated by a 'j' or 'J'.

complex_value = 123 + 456j
print(complex_value)  # Output: (123+456j)# Integer division returns the floor of the result.

# Example of complex numbers
complex1 = 1 + 2j
complex2 = -3j
print(complex1, complex2)  # Output: (1+2j) (-3j)

int_value1 = 123
int_value2 = 45
result = int_value1 // int_value2
print(result)  # Output: 2# Floored division returns the floor of the result.

float_value1 = 123.456
float_value2 = 45
result = float_value1 // float_value2
print(result)  # Output: 2.76# The modulus operator returns the remainder of the division.

int_value1 = 123
int_value2 = 45
result = int_value1 % int_value2
print(result)  # Output: 9# The exponentiation operator raises the first operand to the power of the second operand.

base = 2
exponent = 3
result = base ** exponent
print(result)  # Output: 8# The absolute value function returns the non-negative value of a number.

num = -123
result = abs(num)
print(result)  # Output: 123# The round() function rounds a number to the nearest integer.

num = 123.456
result = round(num)
print(result)  # Output: 123

# Example of number formatting
num = 3.14159

formatted_num1 = f"{num:.2f}"  # Two decimal places
formatted_num2 = "{:.2f}".format(num)  # Using format method

print(formatted_num1, formatted_num2)  # Output: 3.14 3.14

# Example of type conversion
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
num_complex = complex(num_str)

print(num_int, num_float, num_complex)  # Output: 123 123.0 (123+0j)

# Example of arithmetic operations
a = 10
b = 3

addition = a + b       # 10 + 3 = 13
subtraction = a - b    # 10 - 3 = 7
multiplication = a * b # 10 * 3 = 30
division = a / b       # 10 / 3 = 3.3333...
exponentiation = a ** b # 10^3 = 1000

print(addition, subtraction, multiplication, division, exponentiation)


# Python provides several built-in functions to work with numbers, such as abs(), pow(), round(), max(), and min().
# Absolute value
print(abs(-10.5))

# Power function
print(pow(2, 3))

# Rounding
print(round(3.14159, 2))

# Maximum value
print(max(10, 20,)) 