# Chapter 12 - WEB SCRAPING - Automate the boring stuff

## Project: mapIt.py with the webbrowser Module

"""
import webbrowser
webbrowser. open("https://inventwithpython.com/")
"""

## Downloading Files from the Web with the request Module

## -- Downloading a Web Page with the requests.get() Function --

import requests

"""
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])
"""

## -- Checking for Errors --

"""
res = requests.get("https://inventwithpython.com/page_that_does_not_exists")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
"""

## Saving Downloaded Files to the Hard Drive

"""
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
"""

## HTML

## -- Resources for Learning HTML --

## Parsing HTML with the bs4 Module

## Creating a BeautifulSoup Object from HTML

import bs4

"""
res = requests.get("https://nostarch.com")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(noStarchSoup)

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
print(type(exampleSoup))
"""

## Finding an Element with the select() Method

"""
exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")
type(elems)  # elems is a list of Tag objects.
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

print("")

pElems = exampleSoup.select("p")
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
"""

## Getting Data from an Element's Attributes


soup = bs4.BeautifulSoup(open("example.html"), "html.parser")
spanElem = soup.select("span")[0]
print(str(spanElem))
print(spanElem.get("id"))
print(spanElem.get("some_nonexisting_addr") == None)
print(spanElem.attrs)
