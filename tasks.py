# tasks.py
from celery import Celery

# Set up Celery app with Redis as the broker
app = Celery('simple_task', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y