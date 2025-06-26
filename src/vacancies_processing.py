class VacProcessing:

    @classmethod
    def get_top_vacancies(cls, vacancies_list: list, n: int) -> list:
        sorted_vacancies = cls.sort_vacancies(vacancies_list, reverse=True)
        return sorted_vacancies[:n]

    @classmethod
    def sort_vacancies(cls, vacancies_list: list, reverse: bool = False) -> list:
        return sorted(vacancies_list, reverse=reverse)

    @classmethod
    def print_vacancies(cls, vacancies_list: list) -> str:
        result = [f"{str(x)}\n{'-' * 50}" for x in vacancies_list]
        return "\n".join(result)

    @classmethod
    def filter_vacancies(cls, vacancies_list: list, keyword: str) -> list:
        return [x for x in vacancies_list if keyword.lower() in x.description.lower()]

    @classmethod
    def get_vacancies_by_salary(cls, vacancies_list: list, salary_range: str) -> list:
        salary_range_lst = sorted([int(x.strip()) for x in salary_range.split("-")])
        return [x for x in vacancies_list if salary_range_lst[0] <= x <= salary_range_lst[1]]
