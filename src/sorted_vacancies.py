import requests
import json


def get_vacancies(keyword):
    url = f'http://api.hh.ru/vacancies?text={keyword}'
    response = requests.get(url)

    if response.status_code == 200:
        vacancies = response.json()
        sorted_vacancies = sorted(vacancies['items'], key=lambda x: x['name'])
        return sorted_vacancies
    else:
        print('Error fetching vacancies')
    return None


def save_vacancies_to_file(vacancies, filename):
    with open(filename, 'w') as file:
        json.dump(vacancies, file, indent=4)



