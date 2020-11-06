"""
Deprecated, activity tracking via middleware with redis
"""

from django.conf import settings
from eshop import settings as my_settings
from kafka import KafkaConsumer
from time import sleep
from redis import Redis

settings.configure(default_settings=my_settings)


_redis_client = Redis(host='localhost', port=6379, db=0)


def push_path_to_redis_list(paths_list) -> None:
    """
    Pushes url path of the given request to redis list
    """

    # user = request.user.id if request.user.is_authenticated else request.user

    _redis_client.lpush(settings.REDIS_PAGE_TRACKING_LIST_NAME, *paths_list)


KAFKA_LOOP_DELAY = 0.5  # in seconds
KAFKA_LOOPS_TO_WRITE = 5  # write cache to file every KAFKA_LOOPS_TO_WRITE loops

consumer = KafkaConsumer(
    settings.KAFKA_PAGE_TRACKING_TOPIC_NAME,
    bootstrap_servers=settings.KAFKA_SERVERS,
    consumer_timeout_ms=1000
)

if __name__ == '__main__':
    products_visits_cache = []
    count = 0
    while True:
        for message in consumer:
            value = message.value.decode('utf-8')
            products_visits_cache.append(value)
        count += 1
        if count >= KAFKA_LOOPS_TO_WRITE:
            # writing a cache to file
            # with open("products_visits.txt", "a") as f:
            #     f.writelines(products_visits_cache)
            # products_visits_cache = []

            # writing a cache to redis
            if len(products_visits_cache) > 0:
                print("====== Writing cache to redis =======")
                push_path_to_redis_list(products_visits_cache)
                products_visits_cache = []

            count = 0
        sleep(KAFKA_LOOP_DELAY)
