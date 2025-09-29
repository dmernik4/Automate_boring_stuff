#! python3
# fillingInTheGaps.py - Program that finds files in a folder
# and locates any gaps in numbering and rename all the later files.

import os, re

filesFolder = r"C:\delicious"

# Regex that matches the files with numbering pattern.
patternRegex = re.compile(
    r"""^
    ([^\d]+)?              # Optional prefix before the number
    (\d+)                  # Number part
    (\.[a-zA-Z0-9]{2,4}$)  # File extension
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Loop through the files in working folder and get different file parts.
fileInfo = []
for file in os.listdir(filesFolder):
    match = patternRegex.match(file)
    if match:
        prefix, number, extension = match.groups()
        fileInfo.append((file, prefix or "", number, extension))

# Sort files using the numeric value of number part of file.
fileInfo.sort(key=lambda x: int(x[2]))

# Determine number of digits for leading zeros or use 4 digits.
# If you have more than 1000 files use higher number!
numDigits = len(fileInfo[0][2]) if fileInfo else 4

# Rename files to fill the gaps in numbering.
expectedNumber = 1
for originalName, prefix, currentNumber, extension in fileInfo:
    if int(currentNumber) != expectedNumber:
        newNumber = str(expectedNumber).zfill(numDigits)
        newName = f"{prefix}{newNumber}{extension}"
        src = os.path.join(filesFolder, originalName)
        dst = os.path.join(filesFolder, newName)
        os.rename(src, dst)
        print(f"Renamed: {originalName} -> {newName}")
    expectedNumber += 1
