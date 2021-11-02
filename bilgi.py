import urllib.request
from bs4 import BeautifulSoup
webSite = urllib.request.urlopen("https://www.mevzuat.gov.tr/")
getBytes = webSite.read()
webPage = getBytes.decode("utf8")
webSite.close()
soup = BeautifulSoup(webPage, 'html.parser')
print(soup.title.contents)