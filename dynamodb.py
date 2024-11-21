import boto3
from moto import mock_dynamodb2

@mock_dynamodb2
def test_create_dynamodb_table():
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    dynamodb.create_table(
        TableName="test-table",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    tables = dynamodb.list_tables()["TableNames"]
    assert "test-table" in tables
