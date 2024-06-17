from abc import ABC, abstractmethod
import requests
from src.work_with_vacancies import Vacancy


class GetVacancies(ABC):
    """Абстрактный класс для метода получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


class JSONABCSaver(ABC):
    """
    Запись полученных вакансий в файл json и чтение
    """

    @abstractmethod
    def file_writer(self):
        pass

    @abstractmethod
    def file_reader(self):
        pass


class HeadHunterAPI(GetVacancies):
    """Класс для подключения к сайту HH.ru"""
    def get_vacancies(self, name_job, pages):
        hh_list = []

        for i in range(pages):
            params = {
                'text': name_job,
                'per_page': '5',
                'page': i
            }

            response = requests.get('http://api.hh.ru/vacancies', params=params)
            response_json = response.json()

            for j in response_json['items']:
                hh_title = j['name']
                if not (j['area'] is None):
                    hh_town = j['area']['name']
                else:
                    hh_town = None
                if not ((j['salary'] is None) or (j['salary']['from'] is None)):
                    salary_from = j['salary']['from']
                    salary_to = j['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                hh_employment = j['employment']['name']
                hh_url = j['alternate_url']

                hh_vacancy = Vacancy(hh_title, hh_town, salary_from, salary_to, hh_employment, hh_url)
                hh_list.append(hh_vacancy)
        return hh_list

