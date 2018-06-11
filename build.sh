#! /bin/bash

docker-compose build
docker-compose scale worker=1
docker-compose up

