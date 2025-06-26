# Import statements
import os

# Vars
folder_path = "C:\\Users\\Exosteel\\Downloads\\new_folder\\"

# List of all the items in the folder
items = os.listdir(folder_path)

for name in items:
    file_path = os.path.join(folder_path, name)
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
        
