import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    url = urllib.request.urlopen(address, context=ctx)

    data = url.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    count = 0
    sum = 0
    for item in counts:
        count = count + 1
        sum = sum + float(item.text)

    print("Count:", count)
    print("Sum:", sum)