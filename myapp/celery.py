from celery import Celery

app = Celery('myapp',broker='amqp://admin:mypass@rabbit:5672',backend='rpc://',include=['myapp.tasks'])
