from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize_to_db(self, client, **kwargs) -> dict:
        # todo find a way of getting the db context
        raise NotImplementedError

    @abstractmethod
    def serialize_to_class(self, client, **kwargs) -> dict:
        # todo find a way of getting the db context
        raise NotImplementedError
