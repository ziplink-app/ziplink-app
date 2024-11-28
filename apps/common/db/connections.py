import os

from apps.common.integrations.aws.dynamodb.clients import get_dynamo_client


def get_db_client():
    db = os.getenv("DB")
    match db:
        case "DYNAMO_DB":
            return get_dynamo_client()
