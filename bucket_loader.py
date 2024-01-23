import os
import boto3

FILE_NAME = "url_csv.csv"


def upload_csv(bucket: str) -> None:
    s3 = boto3.client('s3')
    try:
        with open(FILE_NAME, "rb") as f:
            s3.upload_fileobj(f, bucket, FILE_NAME)

        print('Upload Completed! Csv deleted.')
        os.remove(FILE_NAME)
    except BaseException as e:
        print(str(e))
        print('Upload Failed. Csv retained locally.')
