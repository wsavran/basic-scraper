import time
import requests
import traceback
import pprint
from pymongo import MongoClient
from myapp.celery import app

# set up mongo
client = MongoClient('mongodb://database:27017')
db = client.test_scraper
info = db.info


@app.task()
def basic_scrape(url):
    response = requests.get(url)
    try:
        ins_id = info.insert_one({'time': time.time(),
                                  'response': response.status_code,
                                  'content': response.content}).inserted_id
        pprint.pprint(info.find_one({"_id": ins_id}))
        tb = 'Success'
    except:
        tb = traceback.format_exc()
    finally:
        print(tb)

    return response.status_code, str(ins_id)
