import os
import sys
import requests
import csv
import bucket_loader
from bs4 import BeautifulSoup
from constants import OUT_DIR, FILE_PATH


def scrape_links(url: str) -> list:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        if 'http' in link.get('href'):
            links.append(link.get('href'))
    return links


def contains_links(url_list: list) -> bool:
    return len(url_list) > 0


def create_csv(url_dict: dict) -> None:
    out_dir_exists = os.path.exists(OUT_DIR)
    if not out_dir_exists:
        os.makedirs(OUT_DIR)

    with open(FILE_PATH, 'w') as f:
        w = csv.DictWriter(f, url_dict.keys())
        w.writeheader()
        w.writerow(url_dict)


def clean_output() -> None:
    for f in os.listdir(OUT_DIR):
        os.remove(os.path.join(OUT_DIR, f))
    os.rmdir(OUT_DIR)


def build_url_dict(url_list: list) -> dict:
    url_dict = {}
    for base_link in url_list:
        scraped_links = scrape_links(base_link)
        if contains_links(scraped_links):
            url_dict[base_link] = scraped_links
    return url_dict


def scrape(urls: list) -> None:
    final_url_dict = build_url_dict(urls)
    create_csv(final_url_dict)
    print('Scraping Completed!')


def main(cli_args: list) -> None:
    s3_load = cli_args[0]
    if s3_load.lower() == 'load':
        bucket = cli_args[1]
        urls = cli_args[2:]
        scrape(urls)
        bucket_loader.upload_csv(bucket)
    else:
        urls = cli_args
        scrape(urls)
        print('Upload Skipped. Csv retained locally.')


if __name__ == "__main__":
    main(sys.argv[1:])
