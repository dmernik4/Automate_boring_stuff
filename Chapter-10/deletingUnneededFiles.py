#! python3
# deletingUnneededFiles.py - Program that deletes unneeded files
# that are greater than 100MB.

import os


def findLargeFiles(folder):
    # Check if any large files have been found
    foundLargeFiles = False

    for foldername, subfolders, files in os.walk(folder):
        for file in files:
            currentFile = os.path.join(foldername, file)

            # Check if files can't be deleted due to restrictions
            try:
                fileSize = os.path.getsize(currentFile)
                if fileSize > 100000000:  # Files larger than 100MB
                    # os.unlink(currentFile)   # Uncomment to delete files
                    print(f"Deleted file: {currentFile} - {fileSize}bytes.")
                    foundLargeFiles = True
            except Exception as e:
                print(f"Error deleting file: {currentFile} - {e}")

    if not foundLargeFiles:
        print("No files grater than 100MB were found.")


findLargeFiles("C:\\delicious_2")
