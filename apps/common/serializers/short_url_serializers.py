from apps.common.integrations.aws.dynamodb.clients import DynamoClient
from apps.common.serializers.serializers import Serializer


class ShortUrlSerializer(Serializer):
    def serialize_to_db(self, obj) -> dict:
        if type(obj.client) is DynamoClient:
            return {
                "hash": {"S": obj.hash},
                "url": {"S": obj.url},
                "expires_at": {"S": str(obj.expires_at)},
            }
        return None

    def serialize_to_class(self, obj, **kwargs) -> "ShortUrl":  # noqa: F821
        if type(obj.client) is DynamoClient:
            obj.hash = kwargs.get("hash", {}).get("S")
            obj.url = kwargs.get("url", {}).get("S")
            obj.expires_at = kwargs.get("expires_at", {}).get("S")
        return obj
