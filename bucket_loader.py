import os
import boto3

FILE_NAME = "url_csv.csv"


def upload_csv() -> None:
    s3 = boto3.client('s3')

    with open(FILE_NAME, "rb") as f:
        s3.upload_fileobj(f, "link.scraper", FILE_NAME)

    os.remove(FILE_NAME)
