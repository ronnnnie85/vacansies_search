from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def __get_request(self):
        pass
