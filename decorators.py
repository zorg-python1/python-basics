# Example 1: Logging Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

# Using the decorated function
result = add(5, 3)




# Example 2: Timing Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)
    return "Finished"

# Using the decorated function
result = long_running_function()






# Example 3: Authorization Decorator
def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('permission') == permission:
                return func(user, *args, **kwargs)
            else:
                print(f"User {user['name']} does not have {permission} permission")
                return None
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user, username):
    print(f"User {username} deleted by {user['name']}")

# Using the decorated function
user = {'name': 'Alice', 'permission': 'admin'}
delete_user(user, 'Bob')  # User Bob deleted by Alice

user = {'name': 'Bob', 'permission': 'user'}
delete_user(user, 'Alice')  # User Bob does not have admin permission





# Chaining Decorators

@timer
@logger
def multiply(x, y):
    return x * y

# Using the decorated function
result = multiply(3, 4)
