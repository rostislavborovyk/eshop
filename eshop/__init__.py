import pymongo
from django.conf import settings
from .celery import celery_app

__all__ = ["celery_app"]

db_name = "db"
collection_name = "products_cart"

mongo_cluster = pymongo.MongoClient(settings.MONGO_CONNECTION_STRING)
mongo_db = mongo_cluster[db_name]
