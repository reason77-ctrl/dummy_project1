import os
import shutil
import glob
import fnmatch

path = input("Enter Directory Path: ")
list_of_fileFolder = os.listdir(path)

for file_folder in list_of_fileFolder:
    files = fnmatch.fnmatch(file_folder, '*.*')
    if files:
        file_name = input("Enter File Name: ")
        os.remove(file_name)
            # os.remove(file_name)
    # print(file_folder)
    # name = input("Enter file name or directory: ")
    # extension = os.path.splitext(file_folder)
    # if os.path.isfile(name):
    #     os.remove(name)
    # elif os.path.isdir(name):
    #     os.rmdir(name)

    # else:
    #     print(f'Error: {name} not exist')

