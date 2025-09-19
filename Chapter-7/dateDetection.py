# dateDetection.py
# Program that detects dates in a certain text

import re, pyperclip
from datetime import datetime


def extractDateComponents(dateStr):
    # Extract day, month and year from date adn remove extra white space
    dateStr = re.sub(r"[\s\-/\.]+", " ", dateStr.strip())
    parts = dateStr

    if len(parts) == 3:
        try:
            nums = [int(part) for part in parts]
            day, month, year = nums
            return day, month, year
        except ValueError:
            return None, None, None
    return None, None, None


def isValidDate(day, month, year):
    # Check if a date is a valid date
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


def formatDate(day, month, year):
    # Format date as DD.MM.YYYY
    return f"{day:02d}.{month:02d}.{year:04d}"


dateRegex = re.compile(
    r"""(
    \d{1,2}
    (\s|-|/|.)?
    \d{1,2}
    (\s|-|/|.)?
    \d{4}
    )""",
    re.VERBOSE,
)

text = str(pyperclip.paste())

dates = []
invalidDates = []

for groups in dateRegex.findall(text):
    # date = "".join([groups[0]])
    dateStr = groups[0]

    day, month, year = extractDateComponents(dateStr)

    if day and month and year:
        if isValidDate(day, month, year):
            # Valid date - format as DD.MM.YYYY
            formatedDate = formatDate(day, month, year)
            dates.append(formatedDate)
        else:
            # Invalid date - keep original + note
            invalidDates.append(f"{dateStr} - not a valid date")

allDates = dates + invalidDates

# Copy dates into clipboard.
if len(allDates) > 0:
    pyperclip.copy("\n".join(allDates))
    print("Copied to clipboard:")
    print("\n".join(allDates))

else:
    print("No dates found.")

print(dates, invalidDates)
