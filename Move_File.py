import os
import shutil

from_dir = "C:/Users/infos/OneDrive/Documents/Documents"
to_dir = "C:/Users/infos/Downloads"

list_of_files = os.listdir(from_dir)

print("List of files in the source directory:")
for file_name in list_of_files:
    print(file_name)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    print(f"File: {name}, Extension: {extension}")

    source_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, file_name)

    shutil.move(source_path, destination_path)

print("Files moved successfully!")