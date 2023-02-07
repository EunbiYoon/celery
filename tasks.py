from celery import Celery
from time import sleep

app=Celery('tasks',broker='amqps://tktymfau:wmS6dhhBR8GHQgtaZgFIRapTrUnyHYg7@shark.rmq.cloudamqp.com/tktymfau')

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
