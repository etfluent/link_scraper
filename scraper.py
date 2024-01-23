import sys
import requests
import csv
from bs4 import BeautifulSoup
from bucket_loader import upload_csv


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
    with open('url_csv.csv', 'w') as f:
        w = csv.DictWriter(f, url_dict.keys())
        w.writeheader()
        w.writerow(url_dict)


def build_url_dict(url_list: list) -> dict:
    url_dict = {}
    for base_link in url_list:
        scraped_links = scrape_links(base_link)
        if contains_links(scraped_links):
            url_dict[base_link] = scraped_links
    return url_dict


def main(s3_load: str, urls: list) -> None:
    final_url_dict = build_url_dict(urls)
    create_csv(final_url_dict)
    print('Scraping Completed!')
    if s3_load.lower() == 'load':
        upload_csv()
        print('Upload Completed!')
    else:
        print('Upload Skipped.')


if __name__ == "__main__":
    main(s3_load=sys.argv[1], urls=sys.argv[2:])
