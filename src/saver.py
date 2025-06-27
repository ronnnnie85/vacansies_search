from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для сохранения данных о вакансиях."""

    @abstractmethod  # pragma: no cover
    def add_vacancy(self):
        """Абстрактный метод для добавления вакансии."""
        pass

    @abstractmethod  # pragma: no cover
    def get_vacancy(self):
        """Абстрактный метод для получения вакансии."""
        pass

    @abstractmethod  # pragma: no cover
    def delete_vacancy(self):
        """Абстрактный метод для удаления вакансии."""
        pass
