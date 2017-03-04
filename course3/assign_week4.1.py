import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter url - ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")

total = 0
for tag in tags:
    total = total + int(tag.contents[0])

print total
