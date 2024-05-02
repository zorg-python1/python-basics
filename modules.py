# Example of using built-in modules
import math

print(math.sqrt(16))  # Using the math module to calculate the square root

# Example of using a third-party module (Pandas)
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)



# File: main_program.py
import mymodule

mymodule.greet("Alice")  # Calling the greet function from the custom module

# Example of using a standard library module (datetime)
from datetime import datetime

now = datetime.now()
print(now)

# Example of using an external package (requests)
import requests

response = requests.get("https://www.google.com")
print(response.status_code)

# Example of using namespace and module alias
import math as m

print(m.sqrt(25))  # Using the alias 'm' for the math module
