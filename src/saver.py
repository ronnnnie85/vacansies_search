from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod # pragma: no cover
    def add_vacancy(self):
        pass

    @abstractmethod # pragma: no cover
    def get_vacancy(self):
        pass

    @abstractmethod # pragma: no cover
    def delete_vacancy(self):
        pass
