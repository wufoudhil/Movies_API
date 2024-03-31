# Movies-API

This is a Movies-API app that helps to add new movies to a cinema program, via API. first install the project dependencies, in your terminal run:

```shell
poetry install
```
This will install all the packages needed to run the project. Next, it is supposed to have already a Redis server installed and running, to start the project run:

```shell
python manage.py runserver
```

Then in another terminal run:

```shell
celery -A movies.celery worker -l info
```

This will help track the task execution periodically.

In another terminal run:

```shell
celery -A movies beat -l info
```
This will display the task execution log (results).

Now go to: [http://127.0.0.1:8000/api/MovieList/](http://127.0.0.1:8000/api/MovieList/), to list movies, based on their rank (higher ones come first).
> Refresh the page after more than 5 minutes to see that the ranking of each movie, from creation (status="coming_up") to launch (status="running"), has been increased by 10 every 5 minutes

# Answers 

## 1. How to design and implement content-based and collaborative filtering recommendation algorithms?:

At first, we should gather and Preprocess the data of items (e.g., movies, products) and their features. Represent each item and user with relevant features. Then use a User-Item Matrix where rows represent users and columns represent items, with ratings or preferences as the matrix entries, after that, calculate the similarity between users or items based on their interactions, and then we can predict the rating or preference of a user for an item based on the ratings/preferences of similar users or items.

## 2. What databases would you use for efficient storage and querying of user preferences and movie metadata?

For efficient storage and querying of user preferences and movie metadata in a recommendation system, typically I chose a database that supports fast reads and writes, can handle large volumes of data, and provides flexible querying capabilities, like SQL Databases(**PostgreSQL**), NoSQL Databases(**MongoDB**, **Redis**).

## 3. How would you optimize database performance for a social networking platform using Postgres, Neo4j, and Qdrant for structured, graph-based, and similarity search data?

For **PostgreSQL**:
* Indexing
* Query Optimization
* Partitioning
* Connection Pooling

For **Neo4j**:
* Indexing
* Caching
* Cypher Query Optimization
* Data Modeling

For **Qdrant**:
* Indexing
* Query Optimization
* Vector Encoding
* Scalability

## 3. Describe using Celery for asynchronous task processing in a Django application, ensuring reliability and fault tolerance, especially for tasks that may fail or need to be retried.

Celery is a powerful distributed task queue that can be integrated with Django to handle asynchronous task,
Steps:

* Install Celery
```shell
pip install celery
``` 
* Configure Celery: Create a Celery configuration file (e.g., celery.py) in a Django project directory. Here's a basic example:
```python
# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```
* Define Tasks: Create the tasks want to execute asynchronously using Celery. Tasks are defined as regular Python functions with the @app.task decorator.
```python
# tasks.py
from celery import shared_task

@shared_task
def my_task(arg1, arg2):
    # Your task logic here
    return result
```

* Handle Task Failure and Retry: Celery provides built-in support for retrying tasks that fail. Configure the number of retries and the delay between retries.
```python
# tasks.py
from celery import shared_task
from celery.exceptions import Retry

@shared_task(bind=True, max_retries=3, default_retry_delay=60)  # Retry up to 3 times with a delay of 60 seconds
def my_task(self, arg1, arg2):
    try:
        # Your task logic here
        return result
    except Exception as exc:
        # Log the exception or handle it as needed
        raise self.retry(exc=exc)
```

* Handle Task Timeouts: We can also handle task timeouts to prevent tasks from running indefinitely.
```python
# tasks.py
from celery.exceptions import SoftTimeLimitExceeded

@shared_task(bind=True, soft_time_limit=300)  # Set a soft time limit of 5 minutes
def my_task(self, arg1, arg2):
    try:
        # Your task logic here
        return result
    except SoftTimeLimitExceeded:
        # Task timed out, handle it accordingly
```
