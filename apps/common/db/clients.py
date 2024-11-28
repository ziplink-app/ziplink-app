from abc import ABC, abstractmethod


class DBClient(ABC):
    @abstractmethod
    def add(self, table_name: str, item: {}):
        raise NotImplementedError

    @abstractmethod
    def get(self, table_name: str, id_field: str, id_value: str):
        raise NotImplementedError

    @abstractmethod
    def update(self, title, year, rating, plot):
        raise NotImplementedError

    @abstractmethod
    def query(self, year):
        raise NotImplementedError

    @abstractmethod
    def scan(self, year_range):
        raise NotImplementedError

    @abstractmethod
    def delete(self, table_name: str, id_field: str, id_value: str):
        raise NotImplementedError
