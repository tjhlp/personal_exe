import os

def print_dir(path):

    temp_dirs = os.listdir(path)
    for i in temp_dirs:
        print(i)
        if os.path.isdir(i):
            return print_dir(i)
