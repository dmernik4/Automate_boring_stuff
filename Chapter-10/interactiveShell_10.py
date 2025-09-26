# CHAPTER 10 - Automate the boring stuff

## The shutil Module
import shutil, os
from pathlib import Path

# -- Copying Files and Folders --

"""
p = Path.home()
folder = p / "some_folder"
folder.mkdir(exist_ok=True)  # Creates a folder if does not exists

shutil.copy(p / "spam.txt", folder / "spam.txt")
shutil.copy(p / "eggs.txt", folder / "eggs2.txt")

p = Path.home()
shutil.copytree(p / "some_folder", p / "some_folder_backup")
"""

# -- Moving and Renaming Files and Folders

"""
shutil.move(
    "C:\\Users\\david\\sonnet29.txt", "C:\\Users\\david\\some_folder\\new_sonnet_29.txt"
)

shutil.move("spam.txt", "c:\\does_not_exists\\eggs\\ham")
"""

# -- Permanently Deleting Files and Folders --

"""
for filename in Path.home().glob("*.txt"):
    # os.unlink(filename)
    print(filename)
"""

# -- Safe Deletes with the send2trash Module --
import send2trash

"""
baconFile = open("bacon.txt", "a")  # Create the file
baconFile.write("Bacon is not a vegetable.")
baconFile.close()
send2trash.send2trash("bacon.txt")
"""

## Walking a Directory Tree

"""
for folderName, subfolders, filenames in os.walk("C:\\delicious"):
    print("The current folder is " + folderName)

    for subfolder in subfolders:
        print("SUBFOLDER OF " + folderName + ": " + subfolder)

    for filename in filenames:
        print("FILE INSIDE " + folderName + ": " + filename)

    print("")
"""

## Compressing Files with the zipfile Module

# -- Reading ZIP Files --
import zipfile

"""
p = Path.home()
exampleZip = zipfile.ZipFile(p / "example.zip")
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo("spam.txt")
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(
    f"Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!"
)
exampleZip.close()
"""

# -- Extracting from ZIP Files --

"""
p = Path.home()
exampleZip = zipfile.ZipFile(p / "example.zip")
exampleZip.extractall("C:\\delicious_2")
exampleZip.close()

exampleZip.extract("spam.txt", "C:\\some\\new\\fodlers")
exampleZip.close()
"""

# -- Creating and Adding to ZIP Files --

"""
newZip = zipfile.ZipFile("new.zip", "w")
newZip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
"""
