subdirectory = {
    'DOCUMENTS' : ['.pdf', '.rtf', '.txt'] ,
    'AUDIO' : ['.m4a', '.m4b', '.mp3'],
    'VIDEOS' : ['.mov', '.avi', '.mp4'],
    'IMAGES' : ['.jpg', '.jpeg', '.png']
}

# def sorter(value):
#     for k, v in value.items():
#         print(k)
#         print(v)

# sorter(subdirectory)

def sorter(value):
    for category, suffixes in subdirectory.items():
        for suffix in suffixes:
            if suffix == value:
                return category
            
print(sorter('.mov'))