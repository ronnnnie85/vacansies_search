from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod  # pragma: no cover
    def load_data(self):
        pass

    @abstractmethod  # pragma: no cover
    def __get_request(self):
        pass
