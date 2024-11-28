import datetime
from dataclasses import dataclass

from apps.common.models.base_model import BaseModel
from apps.common.serializers.short_url_serializers import ShortUrlSerializer


@dataclass
class ShortUrl(BaseModel):
    hash: str
    url: str
    ttl: datetime

    def __init__(self):
        super().__init__()

    def get(self, key) -> "ShortUrl":
        response = self.client.get(
            table_name="short_url", id_field="hash", id_value=key
        )
        self = ShortUrlSerializer().serialize_to_class(self, **response)
        return self

    def create(self, **kwargs) -> "ShortUrl":
        self.url = kwargs.get("url")
        self.hash = kwargs.get("hash")
        self.ttl = kwargs.get("ttl")
        item = ShortUrlSerializer().serialize_to_db(self)
        self.client.add(table_name="short_url", item=item)
        return self
