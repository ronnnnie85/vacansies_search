from src.config import JOB_TITLE_KEY, LINK_KEY, SALARY_KEY, FROM_SALARY_KEY, SNIPPET_KEY, REQUIREMENT_KEY, \
    RESPONSIBILITY_KEY, ID_KEY


class Vacancy:
    __slots__ = ("__job_title", "__link_to_the_vacancy", "__salary", "__description", "__id")

    __job_title: str
    __link_to_the_vacancy: str
    __salary: int
    __description: str
    __id: int

    def __init__(self, job_title: str, link_to_the_vacancy: str, salary: int, description: str, id: int):
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

    def cast_to_dict(self):
        """Делаем объект словарем"""
        return {
            "job_title": self.__job_title,
            "link_to_the_vacancy": self.__link_to_the_vacancy,
            "salary": self.__salary,
            "description": self.__description,
            "id": self.__id,
        }

    @classmethod
    def cast_to_object_list(cls, lst_vacancy):
        """Делаем список объектом"""
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
                ("\n").join([requirement, responsibility])
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
    def __validation(dct_params: dict):
        if not dct_params.get("job_title") or not dct_params.get("id"):
            return False
        dct_params["link_to_the_vacancy"] = (
            dct_params.get("link_to_the_vacancy") if dct_params.get("link_to_the_vacancy") else ""
        )
        dct_params["salary"] = dct_params.get("salary") if dct_params.get("salary") > 0 else 0
        dct_params["description"] = dct_params.get("description") if dct_params.get("description") else ""
        return True


    @property
    def job_title(self):
        return self.__job_title

    @property
    def link_to_the_vacancy(self):
        return self.__link_to_the_vacancy

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    @property
    def id(self):
        return self.__id

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.__salary <= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary <= other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __ge__(self, other):
        """сравнение меньше или равно"""
        if isinstance(other, Vacancy):
            return self.__salary >= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.__salary >= other
        else:
            raise TypeError("Несовпадающие типы данных")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.__job_title}, {self.__link_to_the_vacancy}, {self.__salary}, "
            f"{self.__description}, {self.__id})"
        )

    def __str__(self):
        return (
            f"ID номер:             {self.__id}\n"
            f"Название вакансии:    {self.__job_title}\n"
            f"Ссылка на вакансию:   {self.__link_to_the_vacancy}\n"
            f"Размер зарплаты:      {self.__salary}\n"
            f"Описание вакансии:    {self.__description}"
        )
