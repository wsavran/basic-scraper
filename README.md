# web scraper 

scalable web scraper written in python using celery, and mongodb

## running
``` docker-compose build ```
``` docker-compose up ```

once everything is running
``` run.sh ``` to active the task
``` mongocli.sh ``` to access mongocli 

### Change Log:
* initial, added docker, mongo, and celery. basic functionality

### TODO:
* incorporate libcomcat to store comcat catalog data and metadata
* build api using flask
* add authentication layer to protect api
* minor frontend using templating to show data
* consider transformation map to access historic data


