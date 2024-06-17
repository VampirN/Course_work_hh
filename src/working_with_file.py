import json


class Vacancies:
    """Обработка списка вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    def get_data(self, criterion):
        def __init__():
            self.criterion = criterion




    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a