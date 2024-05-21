import os
import shutil


def delete_file():
    directory = input("Enter Directory path: ")
    file_name = input("Enter File Name: ")
    file_path = os.path.join(directory, file_name)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print("File Deleted.")
        else:
            print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied: Unable to delete '{file_path}'.")

    except Exception as e:
        print(f"An error occurred while deleting the file '{file_path}': {e}")




def delete_folder():
    directory = input("Enter Directory path: ")
    folder_name = input("Enter Folder Name: ")
    folder_path = os.path.join(directory, folder_name)

    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"{folder_name} folder deleted.")
        else:
            print(f"Folder '{folder_path}' not found.")

    except OSError as e:
        print(f'Error: {folder_path} : {e.strerror}')

