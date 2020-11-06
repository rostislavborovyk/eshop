from time import sleep

from kafka import KafkaProducer
from django.conf import settings

# from eshop import settings as my_settings

# settings.configure(default_settings=my_settings)

kafka_producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_SERVERS,
    retries=5
)


def send_product_page_visit(request):
    """
    Sends a message via KafkaProducer with id of product
    """
    kafka_producer.send(
        settings.KAFKA_PAGE_TRACKING_TOPIC_NAME,
        str(request.path).encode("utf-8"),
    )


if __name__ == '__main__':

    # debug
    while True:
        kafka_producer.send(
            "debug",
            b'message',
            b'Hello'
        )
        sleep(0.5)

# go into docker container
# sudo docker exec -it kafka /bin/sh

# list kafka topic
# /opt/kafka_2.13-2.6.0/bin # ./kafka-topics.sh --list --zookeeper zookeeper:2181

# create kafka topic
# /opt/kafka_2.13-2.6.0/bin # ./kafka-topics.sh --create --zookeeper zookeeper:2181
# --replication-factor 1 --partitions 1 --topic visited_urls
