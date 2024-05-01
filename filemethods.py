# Open a file for writing
file = open("myfile.txt", "w")

# Write some text to the file
file.write("Hello world!")

# Close the file
file.close()

# Open the file for reading
file = open("myfile.txt", "r")

# Read the contents of the file
contents = file.read()

# Print the contents of the file
print(contents)  # Output: Hello world!

# Close the file
file.close()

