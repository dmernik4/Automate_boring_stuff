#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("Saved successfully: " + sys.argv[2])

# Delete keyword and its content
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]
    print("Deleted: " + sys.argv[2])

elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("Successfully loaded: " + sys.argv[1])
    else:
        print("This keyword does not exist.")

# Delete all keywords and the content
elif len(sys.argv) == 2 and sys.argv[1].lower() == "deleteAll":
    mcbShelf.clear()
    print("All keyword and their content was deleted.")

mcbShelf.close()
