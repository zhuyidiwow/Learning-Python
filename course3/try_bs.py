from bs4 import BeautifulSoup
import urllib

url = raw_input("Enter url - ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")

for tag in tags:
    print tag.get("href", None)
