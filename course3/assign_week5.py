import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter url: ")
data = urllib.urlopen(url).read()  # read the xml to a string
tree = ET.fromstring(data)  # make a tree with that string
count_lst = tree.findall(".//count")  # find all count tags and return a list

total = 0
for count in count_lst:
    total = total + int(count.text)

print total
