import requests
from settings import BASE_URL
from typing import Dict

SUFFIX = 'areas'


def get_city(name: str) -> Dict:

    url = '/'.join((BASE_URL, SUFFIX))
    countries = requests.get(url).json()

    for country in countries:
        for areas in country['areas']:
            if areas.get('name') != name:
                for area in areas['areas']:
                    if area.get('name') == name:
                        return area
            else:
                return areas
