from pprint import pprint
import json
from hh_api.vacancies import get_vacancies, get_vacancy
from validation.models import Vacancy


# vacancies = get_vacancies('Аналитик данных', 'Москва')
vacancy = get_vacancy('42838492')

parsed_vacancy = Vacancy.parse_raw(json.dumps(vacancy))

print(parsed_vacancy.key_skills)