import os
import scraper
from constants import FILE_PATH


def test_contains_links():
    url_list = ['test.com']
    assert scraper.contains_links(url_list)


def test_create_csv():
    url_dict = {'https://www.google.com': ['https://www.google.com/imghp?hl=en&tab=wi', 'https://maps.google.com/maps?hl=en&tab=wl', 'https://play.google.com/?hl=en&tab=w8', 'https://www.youtube.com/?tab=w1', 'https://news.google.com/?tab=wn', 'https://mail.google.com/mail/?tab=wm', 'https://drive.google.com/?tab=wo', 'https://www.google.com/intl/en/about/products?tab=wh', 'http://www.google.com/history/optout?hl=en', 'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ'], 'https://x.com': ['https://help.twitter.com/using-twitter/twitter-supported-browsers', 'https://twitter.com/tos', 'https://twitter.com/privacy', 'https://support.twitter.com/articles/20170514', 'https://legal.twitter.com/imprint.html', 'https://business.twitter.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo']}
    scraper.create_csv(url_dict)
    assert os.path.exists(FILE_PATH)
    scraper.clean_output()

# TODO: Needs mocking as values may change
# def test_scrape_links():
#     url = 'https://x.com'
#     expected = ['https://help.twitter.com/using-twitter/twitter-supported-browsers', 'https://twitter.com/tos', 'https://twitter.com/privacy', 'https://support.twitter.com/articles/20170514', 'https://legal.twitter.com/imprint.html', 'https://business.twitter.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo']
#     assert scrape_links(url) == expected
