global_var = 10

def function():
    global global_var  # Declaring global_var as global inside the function
    global_var = 20
    print("Inside function:", global_var)

print("Before function call:", global_var)
function()
print("After function call:", global_var)
