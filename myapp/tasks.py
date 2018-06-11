import time
import requests
from pymongo import MongoClient
from myapp.celery import app

# set up mongo
client=MongoClient('mongo', 27017)
db = client['webscape']
collection = db['test-data']
post = db.test

@app.task(bind=True, default_retry_delay=10) 
def basic_scrape(self, url):
    try:
        request = requests.get(url)
        post.insert({'status': request.status_code, "time": time.time()})
    except Exception as e:
        raise self.retry(exc=e)
    return request.status_code
