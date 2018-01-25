import json, urllib, requests

url = input('Enter location: ')
print('Retrieving {}'.format(url))

# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
r = requests.get(url)
data = r.json()

chars, count, total = 0, 0, 0
for comment in data['comments']:
    chars += len(comment['name'])
    count += 1
    total += comment['count']

print('Retrieved {} characters'.format(chars))
print('Count: {}'.format(count))
print('Sum: {}'.format(total))

