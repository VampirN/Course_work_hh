class VacanciesHH:
    '''Класс для работы с вакансиями'''
    def __init__(self, name, url, salary, currency, requirements):
        self.name = name
        self.url = url
        self.salary = salary
        self.currency = currency
        self.requirements = requirements


        '''Валидация данных'''
        if not isinstance(self.salary, (str, int, float)):
            self.salary = 0

    def __repr__(self):
        return (f"Название вакансии: {self.name}\n "
                f"Ссылка на вакансию: {self.url}\n "
                f"Зарплата: {self.salary} {self.currency}\n "
                f"Требования: {self.requirements}")

    def __lt__(self, other):
        '''Сравнение вакансий по зп'''
        return self.salary < other.salary

    def __eq__(self, other):
        '''Проарка сходства вакансий'''
        return (self.name == other.name and self.salary == other.salary
                and self.currency == other.currency and self.requirements == other.requirements)
