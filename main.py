from pprint import pprint

from vacancies import get_vacancies

vacancies = get_vacancies('Аналитик', 'Самара')
# filtered_vacancy = get_vacancy('43130295')


pprint(vacancies)
