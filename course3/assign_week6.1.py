import urllib
import json

url = raw_input("Enter url: ")
data = urllib.urlopen(url).read()  # read the xml to a string
json_data = json.loads(data)  # make a dictionary with that string
comment_lst = json_data["comments"]

total = 0
for comment in comment_lst:
    total = total + int(comment["count"])

print total
