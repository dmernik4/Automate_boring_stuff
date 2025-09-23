#! python3
# regexSearch.py - finds user-supplied input
#                  in all text files in a folder,
#                  and prints them out

import re, os

# Take user input regular expression
prompt = input("Enter a regular expression: ")
userRegex = re.compile(prompt)

# Open all .TXT files in a CWD folder
txtFiles = []
allFiles = os.listdir(os.getcwd())

txtFileRegex = re.compile(r".txt")

for file in allFiles:
    if txtFileRegex.search(file) is not None:
        txtFiles.append(file)

if not txtFiles:
    print("No text files found.")

# Go through all text and find users regex
for file in txtFiles:
    currentFile = open("{0}/{1}".format(os.getcwd(), file))
    content = currentFile.read()
    string = "".join(content)
    found = userRegex.findall(string)
    foundString = " ".join(found)
    print(foundString + " - in file " + file)
