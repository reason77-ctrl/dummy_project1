import os
import shutil


def file_organizer():
    path = input("Enter Directory Path: ")
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+ '/' +extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)


# path = input("Enter Directory Path: ")
# files = os.listdir(path)


# for file in files:
#     filename, extension = os.path.splitext(file)
#     extension = extension[1:]

#     if os.path.exists(path+ '/' +extension):
#         shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
#     else:
#         os.makedirs(path+'/'+extension)
#         shutil.move(path+'/'+file, path+'/'+extension+'/'+file)