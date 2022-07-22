import os

folder_path = ""
for path, subdirs, files in os.walk(folder_path):
    for name in files:
        file_path = os.path.join(path, name)