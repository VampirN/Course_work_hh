from abc import ABC, abstractmethod
import requests


class FromAPI(ABC):
    '''Абстрактный класс для с API сервиса с вакансиями'''
    @abstractmethod
    def getting_vacancies(self, *args, **kwargs):
        pass


 class GettingVacancies(FromAPI):
     '''Класс для работы с вакансиями'''
     def __init__(self, base_url='https://api.hh.ru/vacancies'):
         self.base_url = base_url

     def getting_vacancies(self, search_vacancies):
         '''Загружает вакансии с url по запросу пользователя'''
         params = {"text": search_vacancies, "area": 102}
         response = requests.get(self.base_url, params=params)
         return response.json()

