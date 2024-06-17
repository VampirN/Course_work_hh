from src.getting_vacancies import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.sorted_vacancies import get_vacancies, save_vacancies_to_file


def user_choice_hh():
    keyword = input('Напишите название профессии: \n')
    hh_api = HeadHunterAPI()
    print('Введите количество страниц вакансий для вывода в топ N: \n')
    pages = int(input())
    print("Введите ключевые слова для фильтрации вакансий: ")
    keyword = input()
    sorted_vacancies = get_vacancies(keyword)
    if sorted_vacancies:
        save_vacancies_to_file(sorted_vacancies, 'sorted_vacancies.json')
    from_hh = hh_api.get_vacancies(keyword, pages)
    print('Список вакансий с сайта "HeadHuter": \n')
    for i in from_hh:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Спасибо за использование программы!')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()
        return jsonfile_hh


if __name__ == "__main__":
    user_choice_hh()
