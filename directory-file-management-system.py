
# from ChatGP 

import os

os.path.isdir('my_directory')
os.rename('file1.txt', 'new_file.txt')


import os

if os.path.exists('my_directory'):
    print("Directory exists")
else:
    print("Directory does not exist")

import os

files = os.listdir('my_directory')
print(files)

#rename a file or directory using the os module's rename() function
import os

os.rename('old_file.txt', 'new_file.txt')

#delete a file or directory using the os module's remove() function for files and rmdir() function for directories
import os

os.remove('file_to_delete.txt')
os.rmdir('directory_to_delete')

# copy a file from one location to another using the shutil module's copy2() function

import shutil

shutil.copy2('source_file.txt', 'destination_directory')

#move a file from one location to another using the shutil module's move() function
import shutil

shutil.move('source_file.txt', 'destination_directory')

#check if a path refers to a file or a directory using the os.path module's isfile() and isdir() functions.
import os

path = 'new_file.txt'

if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
else:
    print("It is neither a file nor a directory")




# from ColabAI

# Import necessary modules
import os
import shutil

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List all files and directories in the current working directory
files_and_directories = os.listdir(cwd)
print("Files and directories:", files_and_directories)

#Create a new directory
new_directory = "new_directory"
os.makedirs(new_directory)

# Rename a file
os.rename("old_file.txt", "new_file.txt")

# Copy a file
shutil.copyfile("myfile.txt", "new_file.txt")

# Move a file
shutil.move("example.txt", "my_directory/file1.txt")

# # Delete a file
os.remove("myfile.txt")

# # Delete a directory
shutil.rmtree("my_directory")
