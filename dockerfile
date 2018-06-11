FROM python:3

ADD requirements.txt /app/requirements.txt
ADD ./myapp/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt

ENTRYPOINT celery -A myapp worker --loglevel=info
