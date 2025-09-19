# strongPasswordDetection.py
# Detecting if a password created is weak or strong!

import re

print(
    "Password strength checker.\n"
    "\t- password must be at least 8 characters long\n"
    "\t- contains both uppercase and lowercase characters\n"
    "\t- it has at least one digit\n"
    "\t- a special character is extra bonus\n"
)
password = input("Enter a password: ")


def passwordLength(password):
    if len(password) < 8:
        print("Password too short!")
        exit()
    else:
        return True


def upperLowercase(password):
    upperCharacterRegex = re.findall(r"[A-Z]", password)
    lowerCharacterRegex = re.findall(r"[a-z]", password)
    if len(upperCharacterRegex) > 0 and len(lowerCharacterRegex) > 0:
        return True
    return False


def hasNumber(password):
    numIncludedRegex = re.findall(r"[0-9]", password)
    if len(numIncludedRegex) > 0:
        return True


def specialCharacters(password):
    specialCharacterRegex = re.findall(r"[^a-zA-Z0-9\s]", password)
    if len(specialCharacterRegex) > 0:
        return True
    return False


if passwordLength(password):

    has_spec_char = specialCharacters(password)
    has_num = hasNumber(password)
    has_up_low = upperLowercase(password)

    if has_spec_char and has_num and has_up_low:
        print("You have a strong password!")
    else:
        print("Your password is weak!")
