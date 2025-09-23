#! python3
# madLibs.py - Program that opens a text file, reads it,
#              go through words and replace ADJECTIVE,
#              NOUN, ADVERB and VERB with users input,
#              and save text into a new file,

import re, sys


# Set witch words to replace in a file.
wordsRegex = re.compile(r"(ADJECTIVE|NOUN|ADVERB|VERB)")

# Specify the file name which to open.
textFile = input("Enter a name of file you want to open: ")

# Open and go through all the words and replace them with user input.
with open(textFile, "r") as inputFile, open("replacedFile.txt", "w") as outputFile:

    content = inputFile.read()
    matches = wordsRegex.findall(content)

    for match in matches:
        sub = input("Enter a " + match + ": ")
        content = content.replace(match, sub, 1)

    # Save a file with the new name.
    outputFile.write(content)
    print(content)
    inputFile.close()
    outputFile.close()
