import boto3
from constants import FILE_PATH, FILE_NAME


def upload_csv(bucket: str) -> None:
    s3 = boto3.client('s3')
    try:
        with open(FILE_PATH, "rb") as f:
            s3.upload_fileobj(f, bucket, FILE_NAME)
        print('Upload Completed! Csv deleted.')
    except BaseException as e:
        print(str(e))
        print('Upload Failed. Csv retained locally.')
