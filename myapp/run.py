from .tasks import basic_scrape
import time

if __name__ == '__main__':
    urls = ['http://www.wikipedia.org', 'http://www.reddit.com', 'http://www.google.com']
    for url in urls:
        result = basic_scrape.delay(url)
        time.sleep(2)
        print('Result: {}'.format(result.result))
