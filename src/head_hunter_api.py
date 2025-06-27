from typing import Optional

import requests

from src.config import DATA_KEY, HEADERS, PAGE_KEY, PARAMS, SEARCH_TEXT_KEY, URL
from src.parser import Parser


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter, наследующийся от абстрактного класса Parser."""

    __url: str
    __headers: dict
    __params: dict
    __vacancies: list

    def __init__(self):
        """Инициализирует экземпляр класса с настройками для запросов к API."""
        self.__url = URL
        self.__headers = HEADERS
        self.__params = PARAMS
        self.__vacancies = []

    def load_data(self, keyword: str) -> list:
        """Загружает данные о вакансиях по ключевому слову."""
        self.__params[SEARCH_TEXT_KEY] = keyword
        while self.__params.get(PAGE_KEY) != 20:
            response = self._Parser__get_request()
            if not response:
                return []
            vacancies = response.json()[DATA_KEY]
            self.__vacancies.extend(vacancies)
            self.__params[PAGE_KEY] += 1
        self.__params[PAGE_KEY] = 0
        return self.__vacancies

    def _Parser__get_request(self) -> Optional[requests.Response]:
        """Отправляет GET-запрос к API и возвращает ответ."""
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        except requests.exceptions.RequestException:
            return None
        else:
            if response.status_code != 200:
                return None
            return response
