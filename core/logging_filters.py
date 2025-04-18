from core.request_local import get_request
from django.urls import resolve
import logging

class AppRequestFilter(logging.Filter):
    def __init__(self, app_name):
        super().__init__()
        self.app_name = app_name

    def filter(self, record):
        try:
            request = get_request()
            if request is None:
                return False
            resolver_match = resolve(request.path)
            return resolver_match.app_name == self.app_name
        except Exception:
            return False