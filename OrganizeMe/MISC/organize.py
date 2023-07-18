# this helps us identify the type of files in our dir
import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def files_directory(value):
    for k, ves in SUBDIRECTORIES.items():
        for v in ves:
            if v == value :
                return k 
    return 'MISC'

print(files_directory('.jpeg'))

def arrange_directory():
    for items in os.scandir():

        if items.is_dir() == True:
            continue
        # we would need the file paths in order to manipulate them later so we import a new library
        pth_file = Path(items)
        typ_file = pth_file.suffix.lower()
        dir = files_directory(typ_file)
        pth_dir = Path(dir)
        if pth_dir.is_dir() != True :
            pth_dir.mkdir()
        pth_file.rename(pth_dir.joinpath(pth_file))

arrange_directory()