from typing import Optional

import requests

from areas import get_city
from settings import BASE_URL

SUFFIX = 'vacancies'


def get_vacancies(text: str, city_name: str = None):


    params = {
        'text': text
    }

    if city_name:
        params.update({'area': get_city(city_name)['id']})

    url = '/'.join((BASE_URL, SUFFIX))
    response = requests.get(url, params=params).json()

    return response


def get_vacancy(vacancy_id: str):
    url = '/'.join((BASE_URL, SUFFIX, vacancy_id))
    response = requests.get(url).json()

    return response
