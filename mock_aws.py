import boto3
from moto import mock_s3

@mock_s3
def test_create_s3_bucket():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="test-bucket")
    buckets = s3.list_buckets()["Buckets"]
    assert len(buckets) == 1
    assert buckets[0]["Name"] == "test-bucket"
