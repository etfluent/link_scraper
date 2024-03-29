# Link Scraper
Command line tool that scrapes links from list of urls provided at runtime, and writes them into a csv. This csv has the option to be uploaded to an s3 bucket. Loading the file to s3 deletes the file locally as well.

### To load csv into s3:
Note: You will need [AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) configured for boto3. Also, you may have to use `python3` in place of `python` depending on your configuration.

```
python scraper.py load <BUCKET_NAME> https://www.google.com https://www.yotutube.com https://x.com
```

### To keep csv local:

```
python scraper.py https://www.google.com https://www.yotutube.com https://x.com
```
### Docker
Dockerfile is provided. You will still need to configure AWS credentials in the container for uploading the csv via boto3 to work properly.
### Requires the following packages:

```
pip install requests
```
```
pip install html5lib
```
```
pip install bs4
```
Running tests will require pytest:
```
pip install pytest
```
Uploading csv to s3 will require boto3:
```
pip install boto3
```
Note: boto3 will require further setup. See their [documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for setup
