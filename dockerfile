FROM python:3.6

ADD requirements.txt /app/requirements.txt
ADD ./myapp/ /app/
WORKDIR /app/

RUN pip install -r requirements.txt

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser

ENTRYPOINT celery -A myapp worker --loglevel=info
