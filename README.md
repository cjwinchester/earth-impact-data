# Earth Impact Craters
Data files ([geojson](earth-impact-craters.geojson), [csv](earth-impact-craters.csv)) derived from tables on the [PASCC Earth Impact Database website](http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/Index.html), and the Python scripts that created them.

- [`download.py`](download.py): Downloads the page for each event.
- [`scrape.py`](scrape.py): Hoovers out the data from each page and does some light cleaning and transformation (DMS coordinates to decimal, etc.)