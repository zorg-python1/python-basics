global_var = 10

def function():
    print("Global variable inside function:", global_var)

function()
print("Global variable outside function:", global_var)


def function():
    local_var = 20
    print("Local variable inside function:", local_var)

function()
# Trying to access local_var outside the function will raise an error


def outer_function():
    outer_var = 30

    def inner_function():
        nonlocal outer_var
        outer_var = 40
        print("Nonlocal variable inside inner function:", outer_var)

    inner_function()
    print("Nonlocal variable outside inner function:", outer_var)

outer_function()
