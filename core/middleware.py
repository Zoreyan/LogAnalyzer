from django.utils.deprecation import MiddlewareMixin
from core.request_local import set_request

class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        set_request(request)