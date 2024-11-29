from dataclasses_json import dataclass_json

from apps.common.db.connections import get_db_client


@dataclass_json
class BaseModel:
    def __init__(self):
        self.client = get_db_client()

    def get(self, key) -> "BaseModel":
        raise NotImplementedError

    def create(self, **kwargs):
        raise NotImplementedError
