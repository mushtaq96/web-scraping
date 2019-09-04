import requests,sys,webbrowser
from bs4 import BeautifulSoup

print("Googling...")
res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
print(res.raise_for_status())

soup = BeautifulSoup(res.text,"html5lib")

linkElems = soup.select('div#main > div > div > div > a')

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

print("hello")
