import json
import os
from django.conf import settings
from django.db import DatabaseError, connection
from .models import Tenant
from django.core.cache import cache
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def create_database(self):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {self.db_name}")
    except DatabaseError as e:
        print("---------------------------------------------------------", e)
    
def update_settings(self):
    # Update the DATABASES setting in memory for the new tenant
    print("-------------------------------------------------Updating db settings------------------------------")
    settings.DATABASES[self.db_name] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': self.db_name,
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 0,
        'CONN_HEALTH_CHECKS': True,
        'TIME_ZONE' : 'UTC',
        "OPTIONS": {},
        "AUTOCOMMIT": True,
    }

    # Write the updated configuration to the JSON file
    try:
        TENANT_SETTINGS_FILE = os.path.join(settings.BASE_DIR, 'tenant_databases.json')
        with open(TENANT_SETTINGS_FILE, 'w') as file:
            json.dump(settings.DATABASES, file, indent=2)
    
    except Exception as e:
        print(f"-----------------------------------------An error occurred: {e}-------------------------------")


def tenant_from_the_request(request):
    hostname = request.get_host().split(":")[0].lower()

    # Check if the hostname is a subdomain
    if '.' in hostname:
        subdomain = hostname.split('.')[0]

        tenant = Tenant.objects.using(os.environ['DEFAULT_DB_ALIAS']).filter(subdomain_prefix=subdomain).first()
        if tenant:
            return tenant
        else: 
            return None
    
    else:
        # Check if the hostname is localhost
        if hostname == "localhost":
            tenant = "default"
            return tenant
        else:
            return None


def tenant_db_from_the_request(request):
    tenant = tenant_from_the_request(request)
    
    if tenant == "default":
        return os.environ['DB_NAME']
    
    elif tenant is None:
        return None

    else:
        try:
            tenants_map = get_tenants_map()
            tenant_db = tenants_map.get(tenant.name, None)
            return tenant_db
        
        except Tenant.DoesNotExist:
            return None

def get_tenants_map():
    tenants_map = cache.get('tenants_map')
    if tenants_map is None:
        tenants = Tenant.objects.using(os.environ['DEFAULT_DB_ALIAS']).all()

        tenants_map = {tenant.name: tenant.db_name for tenant in tenants}
        cache.set('tenants_map', tenants_map, timeout=None)
    return tenants_map