import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"
req = requests.get(url)
htmlConten = req.content
soup = BeautifulSoup(htmlConten, "html.parser")


# soup.find(tag)[class]
# soup.findAll(tag,class = "desire class")
res = soup.find_all("a", id = "")
link_set = set()
for linkk in res:
    if linkk != "#":
        link_set.add(linkk.get('href'))

for link in link_set:
    print(link)
    