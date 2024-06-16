class VacanciesHH:
    '''Класс для работы с вакансиями'''
    def __init__(self, name, url, salary, currency, requirements):
        self.name = name
        self.url = url
        self.salary = salary
        self.currency = currency
        self.requirements = requirements

    def __repr__(self):
        return (f"Название вакансии: {self.name}\n "
                f"Ссылка на вакансию: {self.url}\n "
                f"Зарплата: {self.salary} {self.currency}\n "
                f"Требования: {self.requirements}")
