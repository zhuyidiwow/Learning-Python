import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input("Enter location: ")
url = serviceurl + \
    urllib.urlencode({'sensor': 'false', 'address': address})

data = urllib.urlopen(url).read()

try:
    js = json.loads(str(data))
except:
    js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data

print json.dumps(js, indent=4)
print js["results"][0]["place_id"]
