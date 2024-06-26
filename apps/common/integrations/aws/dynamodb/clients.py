import boto3
import botocore


class DynamoClient:
    def __init__(self):
        self.client = boto3.client("dynamodb")

    def add(self, table_name: str, item: {}):
        try:
            self.client.put_item(TableName=table_name, Item=item)
        except botocore.exceptions.ClientError as err:
            raise err

    def get(self, table_name: str, id_field: str, id_value: str):
        try:
            response = self.client.get_item(
                TableName=table_name, Key={id_field: id_value}
            )
        except botocore.exceptions.ClientError as err:
            raise err
        else:
            return response["Item"]

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
