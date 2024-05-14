# try:
#     # Code that may raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     # Handling the ZeroDivisionError exception
#     print("Error: Division by zero")


# Example 1: Catching a specific exception type

# try:
#   x = int(input("Enter a number: "))
#   print(10 / x)
# except ZeroDivisionError:
#   print("Cannot divide by zero.")

# Example 2: Catching multiple exception types

# try:
#   x = int(input("Enter a number: "))
#   print(10 / x)
# except (ValueError, TypeError):
#   print("Invalid input. Please enter a number.")

# Example 3: Using else and finally blocks

try:
  x = int(input("Enter a number: "))
  print(10 / x)
except ZeroDivisionError:
  print("Cannot divide by zero.")
else:
  print("Success!")
finally:
  print("Done.")