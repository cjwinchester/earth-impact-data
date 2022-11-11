riocuarto_data = {
    'csv': {
        'crater_name': 'Rio Cuarto',
        'state': '',
        'country': 'Argentina',
        'latitude': -32.87,
        'longitude': -64.23,
        'diameter_km': 4.5,
        'age_millions_years_ago': '<0.1',
        'exposed': True,
        'drilled': False,
        'target_rock': 'Mixed',
        'bolid_type': 'Chondrite (H)',
        'url': 'http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/Riocuarto.html'  # noqa
    },
    'feature': {
        'type': 'Feature',
        'properties': {
            'crater_name': 'Rio Cuarto',
            'state': '',
            'country': 'Argentina',
            'diameter_km': 4.5,
            'age_millions_years_ago': '<0.1',
            'exposed': True,
            'drilled': False,
            'target_rock': 'Mixed',
            'bolid_type': 'Chondrite (H)',
            'url': 'http://www.passc.net/EarthImpactDatabase/New%20website_05-2018/Riocuarto.html'  # noqa
        },
        'geometry': {
            'type': 'Point',
            'coordinates': [-64.23, -32.87]
        }
    }
}

target_rock_labels = {
    'C': 'Crystalline',
    'C-Ms': 'Metasedimentary',
    'M': 'Mixed',
    'S': 'Sedimentary'
}

countries_with_states = {
    'Alabama, U.S.A.': ('Alabama', 'United States'),
    'Alaska, U.S.A.': ('Alaska', 'United States'),
    'Alberta, Canada': ('Alberta', 'Canada'),
    'Arizona, U.S.A.': ('Arizona', 'United States'),
    'Illinois, U.S.A.': ('Illinois', 'United States'),
    'Indiana, U.S.A.': ('Indiana', 'United States'),
    'Iowa, U.S.A.': ('Iowa', 'United States'),
    'Kansas, U.S.A.': ('Kansas', 'United States'),
    'Kentucky, U.S.A.': ('Kentucky', 'United States'),
    'Manitoba, Canada': ('Manitoba', 'Canada'),
    'Michigan, USA': ('Michigan', 'United States'),
    'Missouri, U.S.A.': ('Missouri', 'United States'),
    'Montana, U.S.A.': ('Montana', 'United States'),
    'New Mexico , U.S.A.': ('New Mexico', 'United States'),
    'Newfoundland-Labrador, CA': ('Newfoundland and Labrador', 'Canada'),
    'North Dakota, U.S.A.': ('North Dakota', 'United States'),
    'Northern Territory': ('Northern Territory', 'Australia'),
    'Northern Territory, AU': ('Northern Territory', 'Australia'),
    'Northern Territory,AU': ('Northern Territory', 'Australia'),
    'Northwest Territories, Canada': ('Northwest Territories', 'Canada'),
    'Nova Scotia, Canada': ('Nova Scotia', 'Canada'),
    'Nunavut, Canada': ('Nunavut', 'Canada'),
    'Ohio, U.S.A.': ('Ohio', 'United States'),
    'Oklahoma, U.S.A.': ('Oklahoma', 'United States'),
    'Ontario, Canada': ('Ontario', 'Canada'),
    'Quebec, Canada': ('Quebec', 'Canada'),
    'Queensland': ('Queensland', 'Australia'),
    'Saskatchewan, Canada': ('Saskatchewan', 'Canada'),
    'South Australia': ('South Australia', 'Australia'),
    'Tennessee, U.S.A.': ('Tennessee', 'United States'),
    'Texas, U.S.A.': ('Texas', 'United States'),
    'Utah, U.S.A.': ('Utah', 'United States'),
    'Victoria Island, Arctic Canada': ('Victoria Island', 'Canada'),
    'Virginia, U.S.A.': ('Virginia', 'United States'),
    'Western Australia': ('Western Australia', 'Australia'),
    'Wisconsin, U.S.A.': ('Wisconsin', 'United States'),
    'Wyoming, USA': ('Wyoming', 'United States'),
    'Yucatan, Mexico': ('Yucatán', 'Mexico')
}

unicode_replacements = [
    ('Ã¤', 'ä'),
    ('Ã¸', 'ø'),
    ('Ã¥', 'å'),
    ('Ã£', 'ã'),
    ('Ã´', 'ô'),
    ('Ã¶', 'ö')
]

replace_age = [
    ('Â', ''),
    ('*', ''),
    ('+/-', '±'),
    ('~ ', '~'),
    ('< ', '<')
]

boolean_map = {
    'N': False,
    'Y': True
}
