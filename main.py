# main.py
from tasks import add

# Calling the Celery task asynchronously (does not block)
result = add.delay(4, 6)
print(f"Task sent to the worker: {result.id}")