import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")
position = int(raw_input("Enter position: "))
count = int(raw_input("Enter count: "))


html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

for i in range(0, count - 1):
    url = tags[position - 1].get("href", None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

print tags[position - 1].get("href", None)
