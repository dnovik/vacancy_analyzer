import requests
from settings import BASE_URL
from typing import Optional
from areas import get_city

SUFFIX = 'vacancies'


def get_vacancies(text: str, city_name: Optional[str]):

    if city_name:
        area = get_city(city_name)

    params = {
        'text': text,
        'area': area['id']
    }

    url = '/'.join((BASE_URL, SUFFIX))
    response = requests.get(url, params=params).json()

    return response


def get_vacancy(vacancy_id: str):
    
    url = '/'.join((BASE_URL, SUFFIX, vacancy_id))
    response = requests.get(url).json()

    return response
