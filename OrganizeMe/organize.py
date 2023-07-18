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

print(files_directory('.jpeg'))