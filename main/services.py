from redis import Redis
from django.conf import settings


_redis_client = Redis(host='localhost', port=6379, db=0)


def push_path_to_redis_list(request) -> None:
    """
    Pushes url path of the given request to redis list
    """
    path = request.path
    # user = request.user.id if request.user.is_authenticated else request.user

    _redis_client.lpush(settings.REDIS_PAGE_TRACKING_LIST_NAME, path)
