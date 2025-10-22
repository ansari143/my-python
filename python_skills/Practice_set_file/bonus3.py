'''Write a Python command-line tool that takes a folder name and prints the
total size of all files inside it (use os.path.getsize() )'''

import os
import sys

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python folder_size.py <folder_name>")
        sys.exit(1)

    folder_name = sys.argv[1]

    if not os.path.isdir(folder_name):
        print(f"Error: '{folder_name}' is not a valid directory.")
        sys.exit(1)

    size_bytes = get_folder_size(folder_name)
    size_mb = size_bytes / (1024 * 1024)
    print(f"Total size of '{folder_name}': {size_mb:.2f} MB")


