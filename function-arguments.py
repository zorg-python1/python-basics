def greet(name, message):
    return f"Hello, {name}! {message}"

print(greet("Alice", "How are you?"))


def greet(name, message):
    return f"Hello, {name}! {message}"

print(greet(message="How are you?", name="Bob"))


def greet(name, message="How are you?"):
    return f"Hello, {name}! {message}"

print(greet("Alice"))
print(greet("Bob", "What's up?"))


def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")


