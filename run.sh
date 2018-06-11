#! /bin/bash

docker exec -i -t celery-with-docker-rabbit-mq_worker_1 python -m myapp.run
