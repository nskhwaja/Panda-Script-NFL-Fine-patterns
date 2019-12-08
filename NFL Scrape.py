#import requests 
#from bs4 import BeautifulSoup
#url = 'https://www.spotrac.com/nfl/fines-suspensions/'
#page = requests.get('https://www.spotrac.com/nfl/fines-suspensions/')
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin

# Remove the trailing / you had, as that gives a 404 page
url = 'https://www.spotrac.com/nfl/fines-suspensions/'
u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")
for link in soup.select('a[href^="http://"]'):
    href = link.get('href')
    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx']):
        continue

    filename = href.rsplit('/', 1)[-1]
    print("Downloading %s to %s..." % (href, filename) )
    urlretrieve(href, filename)
    print("Done.")