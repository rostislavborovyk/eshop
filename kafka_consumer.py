from django.conf import settings
from eshop import settings as my_settings
from kafka import KafkaConsumer
from time import sleep

settings.configure(default_settings=my_settings)

KAFKA_LOOP_DELAY = 0.5  # in seconds
KAFKA_LOOPS_TO_WRITE = 5  # write cache to file every KAFKA_LOOPS_TO_WRITE loops

consumer = KafkaConsumer(
    'requests',
    bootstrap_servers=settings.KAFKA_SERVERS,
    consumer_timeout_ms=1000
)

if __name__ == '__main__':
    products_visits_cache = []
    count = 0
    while True:
        print("=== Kafka reading loop ===")
        for message in consumer:
            value = message.value.decode('utf-8')
            products_visits_cache.append(f"Visited product with id {value}\n")
        count += 1
        if count >= KAFKA_LOOPS_TO_WRITE:
            with open("products_visits.txt", "a") as f:
                f.writelines(products_visits_cache)
            count = 0
            products_visits_cache = []
        sleep(KAFKA_LOOP_DELAY)
