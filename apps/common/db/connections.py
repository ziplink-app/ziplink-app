import os

from apps.common.integrations.aws.dynamodb.clients import get_dynamo_client
from apps.common.logging import get_logger

logger = get_logger(__name__)

def get_db_client():
    db = os.environ.get("DB")

    logger.info(db)
    match db:
        case "DYNAMO_DB":
            return get_dynamo_client()
