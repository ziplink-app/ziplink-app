from dataclasses import dataclass
import datetime

from apps.common.integrations.aws.dynamodb.clients import get_dynamo_client


class BaseModel:
    def __init__(self):
        # Todo use generic client here
        self.client  = get_dynamo_client()

    def get(self, id) -> "BaseModel":
        raise NotImplementedError


@dataclass
class ShortUrl(BaseModel):
    hash: str
    ttl: datetime
    url: str

    def get(self, hash) -> "ShortUrl":
        response = self.client.get("short_url", "hash", hash)
        return response

