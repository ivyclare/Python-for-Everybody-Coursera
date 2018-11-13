# Following Links in Python
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = input("Enter url: ")
count = input("Enter count: ")
position = input("Enter position: ")
n = 0
count = int(count)
position = int(position)
# Retrieve all of the anchor tags
while n <= count:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    # Look at the parts of a tag
    print("Retrieving: ",url)
    url = tags[position-1].get('href', None)
    n += 1
