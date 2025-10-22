'''Create a script that deletes all .tmp files from the current directory using os
and os.remove() .
'''

import os 
current_dir= os.getcwd()

for file_name in os.listdir(current_dir):
    if file_name.endswith(".x"):
        file_path = os.path.join(current_dir, file_name)
        os.remove(file_path)
        print(f" deleted the file {file_name}")
print("All .tmp files have been deleted (if any existed).")
