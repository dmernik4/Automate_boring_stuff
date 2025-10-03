# Chapter 11 - DEBUGGING - Automate the boring stuff

## Raising Exceptions

"""
raise Exception("This is the error message.")
"""

## Getting the Traceback as a string
import traceback

"""
try:
    raise Exception("This is the error message.")

except:
    errorFile = open("errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written to errorInfo.txt")
"""

## Assertions

"""
ages = [26, 57, 92, 54, 22, 15, 17, 80, 40, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
"""

"""
ages = [26, 57, 92, 54, 22, 15, 17, 80, 40, 73]
ages.reverse()
print(ages)
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
"""

# -- Using an Assertion in a Traffic Light Simulation --

"""
market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"

    assert "red" in stoplight.values(), "Neither light is red! " + str(stoplight)


switchLights(market_2nd)
"""

## Logging

# -- Using the logging Module --

# factorialLog.py

# -- Don't Debug with the print() Function --

# -- Logging Levels --
import logging

"""
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Some debugging details.")
logging.info("The logging module is working.")
logging.warning("An error message is about to be logged.")
logging.error("An error has occurred.")
logging.critical("The program is unable to recover.")
"""

# -- Disabling Logging --

"""
logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.critical("Critical error! Critical error!")
logging.disable(logging.CRITICAL)
logging.critical("Critical error! Critical error!")
logging.error("Error! Error!")
"""

# -- Logging to a File --

"""
logging.basicConfig(
    filename="myProgramLog.txt",
    level=logging.DEBUG,
    format=" %(asctime)s - %(levelname)s - %(message)s",
)
logging.critical("Critical error! Critical error!")
"""

# -- Debugging a Number Adding Program --

# buggyAddingProgram.py

# -- Breakpoints --

# coinFlip.py
