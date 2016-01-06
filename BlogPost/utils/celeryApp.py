#encoding = utf8
from celery import Celery
from kombu import Queue, Exchange

class Config:
    CELERY_TASK_RESULT_EXPIRES=3600
    CELERY_TASK_SERIALIZER='json'
    CELERY_ACCEPT_CONTENT=['json']
    CELERY_RESULT_SERIALIZER='json'

    CELERY_DEFAULT_EXCHANGE = 'agent'
    CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
    CELERY_DEFAULT_QUEUE = 'z1'

    CELERT_QUEUES =  (
       Queue('z1',exchange='agent',routing_key='z1'),
       Queue('z2',exchange='agent',routing_key='z2'),
       Queue('z3',exchange='agent',routing_key='z3'),
     )

app = Celery('zhangrg',broker='redis://172.30.15.184:6379/0',backend='redis://172.30.15.184:6379/0',)
app.config_from_object(Config)
