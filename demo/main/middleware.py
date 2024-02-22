import threading
from .utils import tenant_db_from_the_request

Thread_Local = threading.local()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_db = tenant_db_from_the_request(request)
        set_db_for_router(tenant_db)
        print("---------------------------------------------------Selected DB:", tenant_db)
        response = self.get_response(request)
        return response

def get_current_db_name():
    return getattr(Thread_Local, "Database", None)

def set_db_for_router(tenant_db):
    setattr(Thread_Local, "Database", tenant_db)