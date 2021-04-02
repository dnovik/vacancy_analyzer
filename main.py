from vacancies import get_vacancies, get_vacancy
from areas import get_city
from pprint import pprint

vacancies = get_vacancies('Аналитик', 'Самара')
# filtered_vacancy = get_vacancy('43130295')


pprint(vacancies)