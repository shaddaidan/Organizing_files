# in order for us to be able to read the files and their extensions in the folder we would be working 
# we would need to install a new library 

import os

# we would need the paths of the file so we need this library in order to retrieve there path when
# we need it.

from pathlib import Path

# now for our reference library 
subdirectory = {
    'DOCUMENTS' : ['.pdf', '.rtf', '.txt'] ,
    'AUDIO' : ['.m4a', '.m4b', '.mp3'],
    'VIDEOS' : ['.mov', '.avi', '.mp4'],
    'IMAGES' : ['.jpg', '.jpeg', '.png']
}

# time to make our function 

def organiser():
    pass 

    # os.scandir this is the command that would help us get the info on the files in the repository.