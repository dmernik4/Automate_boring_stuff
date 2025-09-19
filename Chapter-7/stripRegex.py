# stripRegex.py
# Program that strips characters with regular expression.

import re

message = input("Write a string from which you want to strip characters: ")
print("What character you want to strip out?")
stripCharacter = input("(if left empty, it will remove whitespace)")

charStripRegex = re.compile(stripCharacter)
whitespaceRegex = re.compile(r"\s")

if stripCharacter == "" or stripCharacter == " ":
    print(whitespaceRegex.sub("", message))
    # Remove white space at the beginning the end!
else:
    print(charStripRegex.sub("", message))
