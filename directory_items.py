import os

# Scanning the current working directory
with os.scandir() as entries:
    for entry in entries:
        print(entry.name)
