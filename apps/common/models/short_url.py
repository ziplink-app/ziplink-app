import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from apps.common.logging import get_logger
from apps.common.models.base_model import BaseModel
from apps.common.serializers.short_url_serializers import ShortUrlSerializer

logger = get_logger(__name__)

@dataclass
class ShortUrl(BaseModel):
    hash: str
    url: str
    expires_at: int

    def __init__(self):
        super().__init__()

    def get(self, key) -> "ShortUrl":
        response = self.client.get(
            table_name="short_url", id_field="hash", id_value=key
        )
        self = ShortUrlSerializer().serialize_to_class(self, **response)
        return self

    def create(self, **kwargs) -> "ShortUrl":
        logger.info(self.client.__class__)
        self.url = kwargs.get("url")
        self.hash = kwargs.get("hash")
        self.expires_at = kwargs.get("expires_at")
        item = ShortUrlSerializer().serialize_to_db(self)
        self.client.add(table_name="short_url", item=item)
        return self
