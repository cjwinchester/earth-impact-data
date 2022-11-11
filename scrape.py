import glob
import json
import csv
import re

from bs4 import BeautifulSoup

from fixes import (
    countries_with_states,
    unicode_replacements,
    riocuarto_data,
    target_rock_labels,
    replace_age,
    boolean_map
)


def parse_dms_to_decimal(dms):
    ''' given a dms value in this data, return decimal equivalent '''

    parts = [x for x in re.split('[°\'" ]+', dms) if x]
    direction = parts[0]
    degrees = parts[1]
    minutes = parts[2]
    seconds = 0.0

    if len(parts) == 4:
        seconds = parts[3]

    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    
    if direction in ('S', 'W'):
        dd *= -1

    return round(dd, 4)


pages = glob.glob('pages/*.html')
filename_out = 'earth-impact-craters'

geojson = {
    'type': 'FeatureCollection',
    'features': []
}

csv_data = []
csv_headers = [
    'crater_name',
    'state',
    'country',
    'target_rock',
    'diameter_km',
    'age_millions_years_ago',
    'exposed',
    'drilled',
    'bolid_type',
    'latitude',
    'longitude',
    'url',
    'notes'
]

# loop over the saved pages
for page in pages:

    # open the page and read in the HTML
    with open(page, 'r') as infile:
        html = infile.read()

    # the page for Rio Cuarto 404s, but data is at
    # http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/SouthAmerica.html  # noqa
    if 'Riocuarto' in page:
        csv_data.append(riocuarto_data['csv'])
        geojson['features'].append(riocuarto_data['feature'])
        continue

    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main')
    
    # grab the crater name
    crater_name = main.find('h1').text.strip()

    # do a little unicode cleanup
    for pair in unicode_replacements:
        crater_name = crater_name.replace(*pair)

    # locate the table with the data in it
    tables = main.find_all('table')
    data_table, references = tables

    # this table has but two rows, my friend
    headers, data = data_table.find_all('tr')

    # love it when a plan comes together
    _, location, latitude, longitude, diameter, age, exposed, drilled, target_rock, bolid_type = [x.text.strip() for x in data.find_all('td')]  # noqa

    # look up the target rock value
    target_rock = target_rock_labels.get(target_rock, '')

    # parse the lat/lng values
    lat = parse_dms_to_decimal(latitude.replace('Â', ''))
    lng = parse_dms_to_decimal(longitude.replace('Â', ''))

    # suss out state/country data
    state = ''
    country = location

    if countries_with_states.get(country):
        state, country = countries_with_states.get(country)
    
    # fix some wonk in the diameter values
    for char in ['(', ')', '*', '~', 'km']:
        diameter = diameter.replace(char, '')

    # ... and the age values
    for pair in replace_age:
        age = age.replace(*pair)

    # get booleans for the `exposed` and `drilled` values
    exposed = boolean_map.get(exposed, '')
    drilled = boolean_map.get(drilled, '')

    # we want blanks not dashes for empty bolid types
    if bolid_type == '-':
        bolid_type = ''

    # build the URL
    url = f'http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/{page.split("/")[-1]}'  # noqa

    # build the props dict
    props = {
        'crater_name': crater_name,
        'state': state,
        'country': country,
        'target_rock': target_rock,
        'diameter_km': diameter,
        'age_millions_years_ago': age,
        'exposed': exposed,
        'drilled': drilled,
        'bolid_type': bolid_type,
        'url': url
    }

    # add a note to the Kärdla record
    if 'Kardla' in url:
        props['notes'] = 'The diameter of the Kärdla impact crater is under review.'  # noqa

    # add a note to the Santa Fe record
    if '6-13' in diameter and 'SantaFe' in url:
        props['diameter_km'] = 6.0
        props['notes'] = 'The diameter of the Santa Fe crater is estimated at 6-13 kilometers.'    # noqa

    # coerce diameter values to floats
    props['diameter_km'] = float(props['diameter_km'])

    # build the geojson feature record
    d = {
        'type': 'Feature',
        'properties': props,
        'geometry': {
            'type': 'Point',
            'coordinates': [lng, lat]
        }
    }

    # add the record to the geojson feature collection
    geojson['features'].append(d)

    # drop a copy of this data (w/ coords) in the csv list
    data_for_csv = props.copy()
    data_for_csv['latitude'] = lat
    data_for_csv['longitude'] = lng
    csv_data.append(data_for_csv)


# write data to file
with open(f'{filename_out}.geojson', 'w') as outfile_gj, open(f'{filename_out}.csv', 'w') as outfile_csv:  # noqa

    # write geojson data
    outfile_gj.write(json.dumps(geojson))

    # write csv data
    writer = csv.DictWriter(outfile_csv, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(csv_data)
