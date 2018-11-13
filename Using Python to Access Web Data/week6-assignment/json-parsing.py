#Extracting Data from JSON
import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url: ")

uh = urllib.request.urlopen(url)
data = uh.read()
total = 0

info = json.loads(data)
comment_list = info['comments']

for item in comment_list:
    total += item['count']
print(total)
