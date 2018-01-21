import urllib.request, urllib.parse, urllib.error
import json

SERVICE_URL = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
url = SERVICE_URL + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
else:
    print('Place ID:', js['results'][0]['place_id'])
