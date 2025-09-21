from pathlib import Path
import os

"""
# print(Path("spam", "bacon", "eggs"))
# print(str(Path("spam", "bacon", "eggs")))

# print(Path("spam") / "bacon" / "eggs")
# print(Path("spam") / Path("bacon/eggs"))
# print(Path("spam") / Path("bacon", "eggs"))

"""
# homeFolder = r"C:\Users\David"
"""
# subFolder = "spam"
# print(homeFolder + "\\" + subFolder)
# print("\\".join([homeFolder, subFolder]))

homeFolder = Path("C:/Users/David")
subFolder = Path("spam")
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))


print(Path.cwd())
os.chdir("C:\\Windows\\System32")
print(Path.cwd())

os.chdir("C:/ThisFolderDoesNotExist")

print(Path.home())

os.makedirs("C:\\delicious\\walnut\\waffles")
"""

# Path(r"C:\Users\david\spam").mkdir()

"""
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path("spam/bacon/eggs").is_absolute())


print(Path("my/relative/path"))
print(Path.cwd() / Path("my/relative/path"))

print(Path("my/relative/path"))
print(Path.home() / Path("my/relative/path"))

print(os.path.abspath("."))
print(os.path.abspath(".\\Scripts"))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))
print(os.path.relpath("C:\\Windows", "C:\\"))
print(os.path.relpath("C:\\Windows", "C;\\spam\\eggs"))

p = Path("C:/Users/david/spam.txt")
print(p.anchor)
print(p.parent)  # This is Path object, not a string.
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)


print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
print(Path.cwd().parents[4])


calcFilePath = "C:\\Windows\\System32\\calc.exe"
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))

print(calcFilePath.split(os.sep))

print(os.path.getsize("C:\\Windows\\System32\\calc.exe"))
print(os.listdir("C:\\Windows\\System32"))

totalSize = 0
for filename in os.listdir("C:\\Windows\\System32"):
    totalSize = totalSize + os.path.getsize(
        os.path.join("C:\\Windows\\System32", filename)
    )
print(totalSize)
"""

# --- Modifying a List of Files Using Glob Patterns ---

"""
p = Path("C:/Users/david/OneDrive/Namizje")
print(p.glob("*"))
print(list(p.glob("*")))

print(list(p.glob("*.pdf")))

for pdfFilePathObj in p.glob("*.pdf"):
    print(pdfFilePathObj)  # Prints the file Path object as a string.
    # Do something with the pdf file
"""

# --- Checking Path Validity ---

"""
winDir = Path("C:/Windows")
notExistsDir = Path("C:/This/Folder/Does/Not/Exists")
calcFile = Path("C:/Windows/System32/calc.exe")
print(winDir.exists())
print(winDir.is_dir())
print(notExistsDir.exists())
print(calcFile.is_file())
print(calcFile.is_dir())

dDrive = Path("D:/")
print(dDrive.exists())
"""

# --- The File Reading/Writing Process ---

"""
p = Path("spam.txt")
p.write_text("Hello, World!")
p.read_text()
"""

# --- Opening Files with the open() Function ---

"""
# helloFile = open(Path.home() / "hello.txt")
helloFile = open("C:\\Users\\david\\hello.txt")
"""

# --- Reading the Contents of File ---

"""
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open(Path.home() / "sonnet29.txt")
print(sonnetFile.readlines())
"""

# --- Writing to Files ---

"""
baconFile = open("bacon.txt", "w")
baconFile.write("Hello, world!\n")
baconFile.close()
baconFile = open("bacon.txt", "a")
baconFile.write("Bacon is not a vegetable.")
baconFile.close()
baconFile = open("bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)
"""

# --- Saving Variables with the shelve Module ---
import shelve

"""
shelfFile = shelve.open("mydata")
cats = ["Zoophie", "Pooka", "Simon"]
shelfFile["cats"] = cats
shelfFile.close()

shelfFile = shelve.open("mydata")
print(type(shelfFile))
print(shelfFile["cats"])
shelfFile.close()
"""

# --- Saving Variables with the pprint.pformat() Function
import pprint

"""
cats = [{"name": "Zoophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
print(pprint.pformat(cats))
fileObj = open("mycats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")
fileObj.close()

import mycats

mycats.cats
mycats.cats[0]
mycats.cats[0]["name"]
"""
