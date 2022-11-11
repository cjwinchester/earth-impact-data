import time

import requests
from bs4 import BeautifulSoup


start_page = 'http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/Namesort.html'  # noqa

r = requests.get(start_page)
r.raise_for_status()

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')[1:]

links = [x.find('a')['href'] for x in rows]

for link in links:
    path = f'pages/{link}'
    url = f'http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/{link}'  # noqa
    r = requests.get(url)
    with open(path, 'w') as outfile:
        outfile.write(r.text)
    print(f'Downloaded {path}')
    time.sleep(0.2)
