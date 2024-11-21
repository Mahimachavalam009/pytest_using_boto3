import boto3
from moto import mock_s3

@mock_s3
def test_upload_file_to_s3():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="test-bucket")
    s3.put_object(Bucket="test-bucket", Key="example.txt", Body="Hello, World!")
    
    response = s3.list_objects(Bucket="test-bucket")
    assert response["Contents"][0]["Key"] == "example.txt"
