'''3. OS and Shutil Modules
Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder
Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)'''

import os
import shutil

# --- Using os module ---

# 1. Print the current working directory
print("Current Working Directory:", os.getcwd())

# 2. List all files and folders in the current directory
print("Contents of current directory:", os.listdir())

# 3. Create a new folder named 'my_folder' (if it doesn't already exist)
folder_name = "my_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

# --- Using shutil module ---

# For demonstration, first create a sample file
with open("sample.txt", "w") as f:
    f.write("This is a test file for shutil operations.")

# 4. Copy the file to 'my_folder'
shutil.copy("sample.txt", folder_name)
print("File copied to 'my_folder'.")

# 5. Move the copied file to a new folder
new_folder = "moved_folder"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

shutil.move(os.path.join(folder_name, "sample.txt"), new_folder)
print("File moved to 'moved_folder'.")

# 6. Delete the original file (careful: irreversible)
os.remove("sample.txt")
print("Original 'sample.txt' deleted.")
