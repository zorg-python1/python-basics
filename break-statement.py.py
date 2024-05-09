# Example 1: Using break in a while loop
num = 0

while True:
    print(num)
    num += 1

    if num == 5:
        break

print("Loop ended")





# Example 2: Using break in a for loop
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
    
    if fruit == "cherry":
        break
