import datetime
from dataclasses import dataclass

from apps.common.integrations.aws.dynamodb.clients import get_dynamo_client


class BaseModel:
    def __init__(self):
        # Todo use generic client here
        self.client = get_dynamo_client()

    def get(self, key) -> "BaseModel":
        raise NotImplementedError


@dataclass
class ShortUrl(BaseModel):
    hash: str
    url: str
    ttl: datetime

    def __init__(self):
        super().__init__()

    def get(self, key) -> "ShortUrl":
        response = self.client.get("short_url", "hash", key)
        return response
