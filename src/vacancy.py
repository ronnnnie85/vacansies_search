class Vacancy:
    __slots__ = ("__job_title", "__link_to_the_vacancy", "__salary", "__description", "__id")

    __job_title: str  # наименование вакансии
    __link_to_the_vacancy: str  # ссылка на вакансию
    __salary: int  # зарплата
    __description: str  # описание
    __id: int  # id

    def __init__(self, job_title, link_to_the_vacancy, salary, description, id):
        dct_params = {
            "job_title": job_title,
            "link_to_the_vacancy": link_to_the_vacancy,
            "salary": salary,
            "description": description,
            "id": id,
        }
        if not self.__validation(dct_params):
            raise ValueError("Invalid parameters")
        self.__job_title = dct_params["job_title"]
        self.__link_to_the_vacancy = dct_params["link_to_the_vacancy"]
        self.__salary = dct_params["salary"]
        self.__description = dct_params["description"]
        self.__id = int(dct_params["id"])

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
            job_title = vac.get("name", "")
            link_to_the_vacancy = vac.get("alternate_url", "")
            salary = (vac_salary if (vac_salary := vac.get("salary")) is not None else {}).get("from", 0)
            requirement = (vac_requirement if (vac_requirement := vac.get("snippet")) is not None else {}).get(
                "requirement", ""
            )
            responsibility = (
                vac_responsibility if (vac_responsibility := vac.get("snippet")) is not None else {}
            ).get("responsibility", "")
            description = (
                ("\n").join([requirement, responsibility])
                if requirement is not None and responsibility is not None
                else ""
            )
            id = vac.get("id", "")
            try:
                vacancy = cls(job_title, link_to_the_vacancy, salary, description, id)
            except ValueError():
                print("Ошибка значения")
            else:
                result.append(vacancy)
        return result

    @staticmethod
    def __validation(dct_params: dict):
        """Валидация данных"""
        if not dct_params["job_title"] or not dct_params["id"]:
            return False
        dct_params["link_to_the_vacancy"] = (
            dct_params["link_to_the_vacancy"] if dct_params["link_to_the_vacancy"] else ""
        )
        dct_params["salary"] = dct_params["salary"] if dct_params["salary"] else 0
        dct_params["description"] = dct_params["description"] if dct_params["description"] else ""
        return True

    @property
    def job_title(self):
        """Переопределение"""
        return self.__job_title

    @property
    def link_to_the_vacancy(self):
        """Переопределение"""
        return self.__link_to_the_vacancy

    @property
    def salary(self):
        """Переопределение"""
        return self.__salary

    @property
    def description(self):
        """Переопределение"""
        return self.__description

    @property
    def id(self):
        """Переопределение"""
        return self.__id

    def __le__(self, other):
        """сравнение больше или равно"""
        if isinstance(other, Vacancy):
            return self.__salary <= other.salary
        else:
            raise TypeError("не совподающие типы данных")

    def __ge__(self, other):
        """сравнение меньше или равно"""
        if isinstance(other, Vacancy):
            return self.__salary >= other.salary
        else:
            raise TypeError("не совподающие типы данных")

    def __repr__(self):
        """Вывод информации для разработчика"""
        return (
            f"{self.__class__.__name__}({self.__job_title}, {self.__link_to_the_vacancy}, {self.__salary}, "
            f"{self.__description}, {self.__id})"
        )

    def __str__(self):
        """Вывод информации для пользователя"""
        return (
            f"ID номер: {self.__id}"
            f"название вакансии: {self.__job_title}"
            f"ссылка на вакансию: {self.__link_to_the_vacancy}"
            f"размер зарплаты: {self.__salary}"
            f"описание вакансии: {self.__description}"
        )
