from apps.common.db.connections import get_db_client


class BaseModel:
    def __init__(self):
        self.client = get_db_client()

    def get(self, key) -> "BaseModel":
        raise NotImplementedError

    def create(self, **kwargs):
        raise NotImplementedError
