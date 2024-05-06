# Example of global namespace
global_var = 10

def print_global_var():
    print(global_var)

print_global_var()  # Output: 10

# Example of local namespace (function scope)
def local_function():
    local_var = 20
    print(local_var)

local_function()  # Output: 20
# Accessing local_var outside the function will result in NameError

# Example of enclosing namespace (nested functions)
def outer_function():
    outer_var = 30
    def inner_function():
        print(outer_var)
    inner_function()

outer_function()  # Output: 30

# Example of built-in namespace functions like print(), len(), and types like list, dict, etc.

print(len([1, 2, 3]))  # Output: 3


# Example of using global and nonlocal keywords
global_var = 10

def modify_global_var():
    global global_var
    global_var = 20

def outer_function():
    outer_var = 30
    def inner_function():
        nonlocal outer_var
        outer_var = 40
    inner_function()
    print(outer_var)  # Output: 40

modify_global_var()
print(global_var)  # Output: 20
outer_function()



