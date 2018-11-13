#Extracting Data from XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url = input("Enter url: ")

uh = urllib.request.urlopen(url)
data = uh.read()
total = 0
tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')

for count in counts:
    total += int(count.text)
print(total)
