from dataclasses_json import dataclass_json

from apps.common.db.connections import get_db_client
from apps.common.logging import get_logger

logger = get_logger(__name__)

@dataclass_json
class BaseModel:
    def __init__(self):
        self.client = get_db_client()
        logger.info(self.client.__class__)

    def get(self, key) -> "BaseModel":
        raise NotImplementedError

    def create(self, **kwargs):
        raise NotImplementedError
