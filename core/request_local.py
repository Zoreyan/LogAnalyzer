import threading

_request_storage = threading.local()

def set_request(request):
    _request_storage.request = request

def get_request():
    return getattr(_request_storage, 'request', None)