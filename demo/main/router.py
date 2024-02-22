from .middleware import get_current_db_name


class TenantRouter:
    def db_for_read(self, model, **hints):
        db = get_current_db_name()
        print("---------------------------------------------------DB for read:", db)
        return db

    def db_for_write(self, model, **hints):
        db = get_current_db_name()
        print("---------------------------------------------------DB for write:", db)
        return db
    
    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None