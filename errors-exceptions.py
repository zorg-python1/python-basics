print "Hello, World!"



print(my_variable)




x = 5
y = "Hello"
print(x + y)



x = 5
y = 0
print(x / y)




numbers = [1, 2, 3, 4, 5]
print(numbers[6])




my_dict = {"name": "John", "age": 30}
print(my_dict["city"])




if True:
    print("This will not be printed")
print("This will be printed")



try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    # Open a file for reading
    file = open("non_existent_file.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File not found.")



x = -1
if x < 0:
    raise ValueError("x should be a positive integer")



print("Hello world)  # Missing closing quotation mark



# NameError example
print(variable)

# TypeError example
result = 10 + "5"


# ValueError example
number = int("hello")

FileNotFoundError example
with open("non_existent_file.txt", "r") as file:
    content = file.read()

# ZeroDivisionError example
result = 10 / 0

