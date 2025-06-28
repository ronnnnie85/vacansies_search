import json
import os
from typing import Any, Optional

from src.saver import Saver
from src.vacancy import Vacancy


class JsonSaver(Saver):
    """Класс для сохранения вакансий в JSON-файл, наследующийся от абстрактного класса Saver."""

    file_name: str

    def __init__(self, file_name: str = "../data/vacancies.json"):
        """Инициализирует экземпляр класса с указанием имени файла."""
        self.file_name = file_name

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в JSON-файл."""
        json_data = self.open_file_read(self.file_name)

        if json_data:
            json_data = [vac for vac in json_data if vac.get("id") != vacancy.id]

        vac_dict = vacancy.cast_to_dict()
        json_data.append(vac_dict)
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

    def get_vacancy(self, vacancy_id: int) -> Optional[Vacancy]:
        """Возвращает вакансию по её ID."""
        json_data = self.open_file_read(self.file_name)

        if json_data:
            vacancy_data = next((vac for vac in json_data if vac.get("id") == vacancy_id), None)
            if vacancy_data:
                return Vacancy(**vacancy_data)

        return None

    def delete_vacancy(self, vacancy_id: int) -> bool:
        """Удаляет вакансию из JSON-файла по её ID."""
        json_data = self.open_file_read(self.file_name)

        if json_data:
            res_data = [vac for vac in json_data if vac.get("id") != vacancy_id]
            if len(res_data) < len(json_data):
                with open(self.file_name, "w", encoding="utf-8") as f:
                    json.dump(res_data, f, ensure_ascii=False, indent=4)
            return True
        return False

    @staticmethod
    def open_file_read(file_name: str) -> Any:
        """Открывает файл для чтения и возвращает его содержимое."""
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        else:
            return []
