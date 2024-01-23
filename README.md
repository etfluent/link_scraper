# Link Scraper
Command line tool that scrapes links from list of urls provided at runtime, and writes them into a csv. This csv has the option to be uploaded to an s3 bucket. Loading the file to s3 deletes the file locally as well.

### To load csv into s3:
Note: You may have to use `python3` in place of `python` depending on you configuration.

```
python scraper.py load <BUCKET_NAME> https://www.google.com https://www.yotutube.com https://x.com
```

### To keep csv local:

```
python scraper.py https://www.google.com https://www.yotutube.com https://x.com
```

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

```
pip install boto3
```
Note: boto3 will require further setup. See their documentation for setup