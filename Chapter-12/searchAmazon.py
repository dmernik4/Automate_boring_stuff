#! python3
# searchAmazon.py - Opens first 10 products on Amazon.de

import requests, sys, webbrowser, bs4

print("Searching...")

res = requests.get("https://www.amazon.de/s?k=" + " ".join(sys.argv[1:]))

res.raise_for_status()

# Retrieve top search results links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# TODO: Open a browser tab for each result.
