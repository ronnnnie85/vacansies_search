import re

from src.head_hunter_api import HeadHunterAPI
from src.vacancies_processing import VacProcessing
from src.vacancy import Vacancy


class UserInteraction:
    """Класс для взаимодействия с пользователем через консоль."""

    def user_interaction(self) -> None:
        """Основной метод для взаимодействия с пользователем."""
        print("Здравствуйте")

        while True:
            search_query = self.check_input("Введите ключевое слово для поиска вакансий")

            hh_parser = HeadHunterAPI()
            vacancy_data = hh_parser.load_data(search_query)

            vacancies_main = Vacancy.cast_to_object_list(vacancy_data)
            vacancies = []
            vacancies.extend(vacancies_main)
            while True:

                print("\nВыберите метод поиска:")
                print("1) Найти топ вакансий")
                print("2) Найти вакансии по слову из описания")
                print("3) Найти вакансии по диапазону зарплат")
                print("4) Отсортировать вакансии по зарплате")

                print("5) Выход")

                user_input = input()

                if user_input.strip() == "1":
                    top_n = self.check_input("Введите количество вакансий в топе")

                    try:
                        n = int(top_n)
                    except ValueError:
                        print("Ошибка: введите корректное число")
                    else:
                        result_top = VacProcessing.get_top_vacancies(vacancies, n)
                        print(VacProcessing.print_vacancies(result_top))
                        self.result_for_next(vacancies, result_top)
                elif user_input.strip() == "2":
                    keyword = self.check_input("Введите ключевое слово для поиска в описании")

                    result_description = VacProcessing.filter_vacancies(vacancies, keyword)
                    print(VacProcessing.print_vacancies(result_description))
                    self.result_for_next(vacancies, result_description)
                elif user_input.strip() == "3":
                    range_salary = self.check_input("Введите диапазон зарплат через - ")
                    pattern = re.compile(r"\b(0|[1-9][0-9]*)-([1-9][0-9]*)\b")

                    match = pattern.fullmatch(range_salary.strip())
                    if not match:
                        print("Ошибка: введите диапазон корректно")
                    else:
                        result_range = VacProcessing.get_vacancies_by_salary(vacancies, range_salary.strip())
                        print(VacProcessing.print_vacancies(result_range))
                        self.result_for_next(vacancies, result_range)
                elif user_input.strip() == "4":
                    ascending_str = self.check_input("Отсортировать по возрастанию?[Y/n]")
                    reverse = ascending_str.lower() != "y"
                    sorted_vacs = VacProcessing.sort_vacancies(vacancies, reverse)
                    print(VacProcessing.print_vacancies(sorted_vacs))
                    self.result_for_next(vacancies, sorted_vacs)
                elif user_input == "5":
                    break
                else:
                    print("Неверный ввод. Пожалуйста, введите от 1 до 5")

            resume_input = self.check_input("Ввести новый запрос?[Y/n]")
            if resume_input.lower() != "y":
                break

    @staticmethod
    def result_for_next(vacancies: list, result: list) -> None:
        """Предлагает пользователю использовать результат для дальнейшей обработки."""
        print("Использовать результат для дальнейшей обработки? [Y/n]")
        user_input = input()

        if user_input.strip().lower() == "y":
            vacancies.clear()
            vacancies.extend(result)

    @staticmethod
    def check_input(text: str) -> str:
        """Проверяет ввод пользователя на пустоту."""
        while True:
            print(text)
            user_input = input()
            if user_input.strip():
                return user_input
            print("Ничего не введено")
