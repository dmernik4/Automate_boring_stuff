#! python3
# selectiveCopy.py - Program that copies only the certain file types
# from a desired location to a new folder

import os, shutil


def copySpecificFiles(fromFolder, toFolder, fileType):
    for folder, subfolder, files in os.walk(fromFolder):
        for file in files:
            if file.endswith(fileType):
                # Copy those files into a new location
                sourcePath = os.path.join(folder, file)
                shutil.copy(sourcePath, toFolder)
                # print(os.path.join(fromFolder + ": " + file))
                print("File copied: " + file)


copySpecificFiles("C:\\delicious", "C:\\delicious_2", ".txt")
