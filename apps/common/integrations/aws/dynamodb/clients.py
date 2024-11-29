import os

import boto3
import botocore

from apps.common.db.clients import DBClient


class DynamoClient(DBClient):
    def __init__(self):
        self.client = boto3.client(
            "dynamodb",
            # endpoint_url="http://localhost:8090",  # DynamoDB Local endpoint
            # aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            # aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            # region_name=os.environ.get("AWS_REGION"),
        )

    def add(self, table_name: str, item: {}):
        try:
            response = self.client.put_item(TableName=table_name, Item=item)
            return response
        except botocore.exceptions.ClientError as err:
            raise err

    def get(self, table_name: str, id_field: str, id_value: str):
        try:
            key = {id_field: {"S": id_value}}
            response = self.client.get_item(TableName=table_name, Key=key)
            return response["Item"]
        except botocore.exceptions.ClientError as err:
            raise err
        except KeyError:
            return {}

    def update(self, title, year, rating, plot):
        raise NotImplementedError

    def query(self, year):
        raise NotImplementedError

    def scan(self, year_range):
        raise NotImplementedError

    def delete(self, table_name: str, id_field: str, id_value: str):
        try:
            self.client.delete_item(TableName=table_name, Key={id_field: id_value})
        except botocore.exceptions.ClientError as err:
            raise err


def get_dynamo_client():
    return DynamoClient()
