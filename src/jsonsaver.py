import json

from src.getting_vacancies import JSONABCSaver
from src.work_with_vacancies import Vacancy
from src.working_with_file import Vacancies


class JSONSaver(Vacancies, JSONABCSaver):
    """
    Запись и чтение json
    """

    def file_writer(self):
        """
        Запись файла
        """
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def file_reader(self):
        """
        Чтение файла
        """
        with open('vacancies.json', 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))