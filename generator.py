#Simple Generator 
def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3



# Using Generators with Loops 
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)




#Generator Expressions
# Generator expression
squared_numbers = (x * x for x in range(5))

# Using the generator expression
for num in squared_numbers:
    print(num)



#Fibonacci Sequence Generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator
for num in fibonacci(10):
    print(num)




# Reading Large Files

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line

# Using the generator to read a large file
for line in read_large_file('large_file.txt'):
    print(line.strip())
