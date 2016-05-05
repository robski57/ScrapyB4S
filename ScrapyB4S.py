import requests
from bs4 import BeautifulSoup
#url is assinged to ("url")
url = (url)
# if url has more then one page this is the exampled used.
url_page_2 = url + '&page=' + str(2) + '&s=relevance'
# r is set to request.get )url)
r = requests.get(url)
#BeautifulSoup
soup = BeautifulSoup(r.content)
#Find all links with a
links = soup.find_all("a")

for link in links:
    print("<a href='%s'>%s</a>" %(link.get("href"), link.text))


g_data = soup.find_all("div",{"class": "info"})

for item in g_data:
    print(item.content[0].find_all("a", {"class": "business-name"})[0].text)
    try:
        print(item.content[1].find_all("span", {"itemprop": "streetlocality"})[0].text)
    except:
        pass
    try:
        print(item.content[1].find_all("span", {"itemprop": "addresslocality"})[0].text)
    except:
        pass
    try:
        print(item.content[1].find_all("span", {"itemprop": "addressRegion"})[0].text)
    except:
        pass
    try:
        print(item.content[1].find_all("span", {"itemprop": "postalCode"})[0].text)
    except:
        pass
    try:
        print(item.content[1].find_all("li", {"class": "primary"})[0].text)
    except:
        pass
