import os
from pathlib import Path
from datetime import datetime

basepath = "./"

for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath,entry)):    # to list subdir in directory
        pass #print(entry)
    if os.path.isfile(os.path.join(basepath,entry)):   # to list only files in the directory
        pass #print(entry.name)



with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():     # to list only files in the directory
            pass #print(entry.name)
        if entry.is_dir():     # to list subdir in directory
            pass #print(entry.name)


basepath2 = Path("./")
files_in_basepath2 = basepath2.iterdir()

for item in files_in_basepath2:
    if item.is_file():    # to list only files in the directory
        pass #print(item.name)
    if item.is_dir():     # to list subdir in the directory
       pass #print(item.name)

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

def get_files():
    dir_entries = Path('./')
    for entry in dir_entries.iterdir():
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_atime)}')

p = Path("reason/")
#p.mkdir()

os.makedirs('2024/5/21')