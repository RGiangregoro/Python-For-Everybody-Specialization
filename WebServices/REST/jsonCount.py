import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter url: ')
if len(address) < 1: address = "http://py4e-data.dr-chuck.net/comments_42.json"

print('Retrieving', address)
url = urllib.request.urlopen(address)
data = url.read()

info = json.loads(data)
print('Count: ', len(info['comments']))

sum = 0 
for item in info['comments']:
    sum = sum + float(item['count'])

print('Sum: ', sum)
