from .services import push_path_to_redis_list


class ActivityTrackingMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        # print("Tracking middleware")
        push_path_to_redis_list(request)
        response = self._get_response(request)
        return response
