from typing import Any

from src.config import (
    FROM_SALARY_KEY,
    ID_KEY,
    JOB_TITLE_KEY,
    LINK_KEY,
    REQUIREMENT_KEY,
    RESPONSIBILITY_KEY,
    SALARY_KEY,
    SNIPPET_KEY,
)


class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("__job_title", "__link_to_the_vacancy", "__salary", "__description", "__id")

    __job_title: str
    __link_to_the_vacancy: str
    __salary: int
    __description: str
    __id: int

    def __init__(self, job_title: str, link_to_the_vacancy: str, salary: int, description: str, id: str):
        """Инициализирует экземпляр вакансии."""
        dct_params = {
            "job_title": job_title,
            "link_to_the_vacancy": link_to_the_vacancy,
            "salary": salary,
            "description": description,
            "id": id,
        }
        if not self.__validation(dct_params):
            raise ValueError("Invalid parameters")
        self.__job_title = dct_params.get("job_title", "")
        self.__link_to_the_vacancy = dct_params.get("link_to_the_vacancy", "")
        self.__salary = dct_params.get("salary", 0)
        self.__description = dct_params.get("description", "")
        self.__id = int(dct_params.get("id", 0))

    def cast_to_dict(self) -> dict:
        """Преобразует вакансию в словарь."""
        return {
            "job_title": self.__job_title,
            "link_to_the_vacancy": self.__link_to_the_vacancy,
            "salary": self.__salary,
            "description": self.__description,
            "id": self.__id,
        }

    @classmethod
    def cast_to_object_list(cls, lst_vacancy: list) -> list:
        """Преобразует список словарей с данными вакансий в список объектов Vacancy."""
        result = []
        for vac in lst_vacancy:
            job_title = vac.get(JOB_TITLE_KEY, "")
            link_to_the_vacancy = vac.get(LINK_KEY, "")
            salary = (vac_salary if (vac_salary := vac.get(SALARY_KEY)) is not None else {}).get(FROM_SALARY_KEY, 0)
            requirement = (vac_requirement if (vac_requirement := vac.get(SNIPPET_KEY)) is not None else {}).get(
                REQUIREMENT_KEY, ""
            )
            responsibility = (
                vac_responsibility if (vac_responsibility := vac.get(SNIPPET_KEY)) is not None else {}
            ).get(RESPONSIBILITY_KEY, "")
            description = (
                ("\n").join([responsibility, requirement])
                if requirement is not None and responsibility is not None
                else ""
            )
            id = vac.get(ID_KEY, "")
            try:
                vacancy = cls(job_title, link_to_the_vacancy, salary, description, id)
            except ValueError():
                print("Ошибка значения")
            else:
                result.append(vacancy)
        return result

    @staticmethod
    def __validation(dct_params: dict) -> bool:
        """Проверяет валидность параметров вакансии."""
        if not dct_params.get("job_title") or not dct_params.get("id"):
            return False
        dct_params["link_to_the_vacancy"] = (
            dct_params.get("link_to_the_vacancy", "") if dct_params.get("link_to_the_vacancy", "") else ""
        )
        dct_params["salary"] = dct_params.get("salary") if dct_params.get("salary") else 0
        dct_params["salary"] = dct_params.get("salary") if dct_params.get("salary", 0) > 0 else 0
        dct_params["description"] = dct_params.get("description", "") if dct_params.get("description", "") else ""
        return True

    @property
    def job_title(self) -> str:
        """Возвращает название вакансии."""
        return self.__job_title

    @property
    def link_to_the_vacancy(self) -> str:
        """Возвращает ссылку на вакансию."""
        return self.__link_to_the_vacancy

    @property
    def salary(self) -> int:
        """Возвращает зарплату."""
        return self.__salary

    @property
    def description(self) -> str:
        """Возвращает описание вакансии."""
        return self.__description

    @property
    def id(self) -> int:
        """Возвращает идентификатор вакансии."""
        return self.__id

    def __le__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (меньше или равно)."""
        if isinstance(other, Vacancy):
            return self.__salary <= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary <= other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __ge__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (больше или равно)."""
        if isinstance(other, Vacancy):
            return self.__salary >= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary >= other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __eq__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (равно)."""
        if isinstance(other, Vacancy):
            return self.__salary == other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary == other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __ne__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (не равно)."""
        if isinstance(other, Vacancy):
            return self.__salary != other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary != other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __lt__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (меньше)."""
        if isinstance(other, Vacancy):
            return self.__salary < other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary < other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __gt__(self, other: Any) -> Any:
        """Сравнивает вакансии по зарплате (больше)."""
        if isinstance(other, Vacancy):
            return self.__salary > other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary > other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return (
            f"{self.__class__.__name__}({self.__job_title}, {self.__link_to_the_vacancy}, "
            f"{self.__salary}, "
            f"{self.__description}, {self.__id})"
        )

    def __str__(self) -> str:
        """Возвращает строковое представление вакансии для пользователя."""
        return (
            f"ID номер:             {self.__id}\n"
            f"Название вакансии:    {self.__job_title}\n"
            f"Ссылка на вакансию:   {self.__link_to_the_vacancy}\n"
            f"Размер зарплаты:      {self.__salary}\n"
            f"Описание вакансии:    {self.__description}"
        )
