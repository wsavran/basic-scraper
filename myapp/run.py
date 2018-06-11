from .tasks import basic_scrape
import time

if __name__ == '__main__':
    urls = ['http://www.wikipedia.org', 'http://www.reddit.org', 'http://www.google.com']
    for url in urls:
        result = basic_scrape.delay(url)
        print("Status: {}".format(result.result))

