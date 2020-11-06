from .services import send_product_page_visit


class ActivityTrackingMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        # print("Tracking middleware")
        send_product_page_visit(request)
        response = self._get_response(request)
        return response
