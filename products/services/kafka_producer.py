"""
Deprecated, activity tracking via middleware with redis
"""

from time import sleep

from kafka import KafkaProducer
from django.conf import settings

# from eshop import settings as my_settings

# settings.configure(default_settings=my_settings)

kafka_producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_SERVERS,
    retries=5
)


def send_product_page_visit(products_id):
    """
    Sends a message via KafkaProducer with id of product
    """
    kafka_producer.send(
        "requests",
        str(products_id).encode("utf-8"),
    )


if __name__ == '__main__':

    # debug
    while True:
        kafka_producer.send(
            "requests",
            b'message',
            b'Hello'
        )
        sleep(0.5)
