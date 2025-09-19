import re

"""
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My phone number is 415-555-4242.")
print("Phone number found: " + mo.group())
"""

"""
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is 415-555-4242.")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

mo.groups()
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
"""

"""
phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is (415) 555-4242.")
print(mo.group(1))
print(mo.group(2))
"""

"""
heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())
mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost the wheel.")
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("The Adventures of Batman")
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo1.group())
print(mo2.group())

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo1 = phoneRegex.search("My number is 415-555-4242")
mo2 = phoneRegex.search("My number is 555-4242")
print(mo1.group())
print(mo2.group())

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The adventures of Batman")
mo2 = batRegex.search("The adventures of Batwoman")
mo3 = batRegex.search("The adventures of Batwowowowowoman")
print(mo1.group())
print(mo2.group())
print(mo3.group())

batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The adventures of Batman")
mo2 = batRegex.search("The adventures of Batwoman")
mo3 = batRegex.search("The adventures of Batwowowowowoman")
print(mo1 == None)
print(mo2.group())
print(mo3.group())


haRegex = re.compile(r"(Ha){3}")
mo1 = haRegex.search("HaHaHa")
mo2 = haRegex.search("Ha")
print(mo1.group())
print(mo2 == None)

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())

nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo1 = nongreedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups
mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group())
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

xmasRegex = re.compile(r"\d+\s\w+")
print(
    xmasRegex.findall(
        "12 rummers, 11 pipers, 10 lords, 9, ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
    )
)


vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("Robocop eats baby food. BABY FOOD."))

consonantRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantRegex.findall("Robocop eats baby food. BABY FOOD."))


beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello, world!"))
print(beginsWithHello.search("He said hello.") == None)

endWithNumber = re.compile(r"\d$")
print(endWithNumber.search("Your number is 42"))
print(endWithNumber.search("Your number is forty two.") == None)


wholeStringIsNum = re.compile(r"^\d+$")
print(wholeStringIsNum.search("1234567890"))
print(wholeStringIsNum.search("12345xyz67890") == None)
print(wholeStringIsNum.search("12    34567890") == None)


atRegex = re.compile(r".at")
print(atRegex.findall("The cat in the hat sat on the flat mat."))

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group(1))
print(mo.group(2))


nongreedyRegex = re.compile(r"<.*?>")
mo = nongreedyRegex.search("<To serve man> for dinner.>")
print(mo.group())


greedyRegex = re.compile(r"<.*>")
mo = greedyRegex.search("<To serve man> for dinner.>")
print(mo.group())

noNewlineRegex = re.compile(".*")
print(
    noNewlineRegex.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law."
    ).group()
)

newlineRegex = re.compile(".*", re.DOTALL)
print(
    newlineRegex.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law."
    ).group()
)

robocop = re.compile(r"robocop", re.I)
print(robocop.search("RoboCop os part man, part machine, all cop.").group())
print(robocop.search("ROBOCOP protects the inocent.").group())
print(
    robocop.search(
        "Al, why does your programming book talk about robocop so much?"
    ).group()
)


namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))

agentNameRegex = re.compile(r"Agent (\w)\w*")
print(
    agentNameRegex.sub(
        r"\1****",
        "Agent Alice told Agent Carol that Agent Eve know Agent Bob was a double agent.",
    )
)

numRegex = re.compile(r"\d+")
print(numRegex.sub("X", "12 drummers, 11 pipers, five rings, 3 hense"))
"""

"""
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My phone number is 415-555-4242.")
print("Phone number found: " + mo.group())
"""

# ___________________________________________________________________

"""
numRegex = re.compile(r"\b\d{1,3}(?:,\d{3})*\b")
print(numRegex.findall("12,424 32 505"))
"""

"""
watanabeRegex = re.compile(r"[A-Z]\w+ Watanabe")
print(
    watanabeRegex.findall(
        "Haruto Watanabe, Robocop Watanabe, just Watanabe, or watanabe, Mr. Watanabe, Jinu Watanabe"
    )
)
"""

"""
text = "Alice eats apples."
sentenceRegex = re.compile(r"([A-Z]\w+) (eats|pets|throws) (apples|cats|baseballs).")
print(sentenceRegex.search(text).group())
"""


import re, pyperclip
from datetime import datetime


def extract_date_components(date_str):
    """Extract day, month, year from date string"""
    # Remove extra whitespace and normalize separators
    date_str = re.sub(r"[\s\-/\.]+", " ", date_str.strip())
    # Remove addition white spaces
    date_str = re.sub(r"\s+", " ", date_str)
    parts = date_str.split()

    if len(parts) == 3:
        try:
            nums = [int(part) for part in parts]
            # Assume DD MM YYYY format based on your regex pattern
            day, month, year = nums
            return day, month, year
        except ValueError:
            return None, None, None

    return None, None, None


def is_valid_date(day, month, year):
    """Check if the given day, month, year form a valid date"""
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


def format_date(day, month, year):
    """Format date as DD.MM.YYYY"""
    return f"{day:02d}.{month:02d}.{year:04d}"


# Your original regex
dateRegex = re.compile(
    r"""(
    \d{1,2}
    (\s|-|/|\.)?
    \d{1,2}
    (\s|-|/|\.)?
    \d{4}
    )""",
    re.VERBOSE,
)

text = str(pyperclip.paste())
dates = []
invalid_dates = []

for groups in dateRegex.findall(text):
    date_str = groups[0]  # Original matched date string

    # Extract components
    day, month, year = extract_date_components(date_str)

    if day and month and year:
        if is_valid_date(day, month, year):
            # Valid date - format as DD.MM.YYYY
            formatted_date = format_date(day, month, year)
            dates.append(formatted_date)
        else:
            # Invalid date - keep original and mark as invalid
            invalid_dates.append(f"{date_str} - not a valid date")
    else:
        # Couldn't parse - keep original and mark as invalid
        invalid_dates.append(f"{date_str} - not a valid date")

# Combine valid and invalid dates
all_results = dates + invalid_dates

# Copy results to clipboard
if len(all_results) > 0:
    pyperclip.copy("\n".join(all_results))
    print("Copied to clipboard:")
    print("\n".join(all_results))

    # Show summary
    if dates:
        print(f"\nValid dates found: {len(dates)}")
    if invalid_dates:
        print(f"Invalid dates found: {len(invalid_dates)}")
else:
    print("No dates found.")
