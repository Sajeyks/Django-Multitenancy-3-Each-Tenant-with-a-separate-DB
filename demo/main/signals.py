import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.core.management import call_command
from django.db import transaction
from .models import Tenant
from .utils import create_database, update_settings


@receiver(post_save, sender=Tenant)
def update_tenants_map_cache(sender, instance, **kwargs):
    def on_commit_callback():
        create_database(instance)
        update_settings(instance)
        
        # Run migrations for the specific database
        call_command('migrate', database=instance.db_name)
        tenants = Tenant.objects.using(os.environ['DEFAULT_DB_ALIAS']).all()

        tenants_map = {tenant.name: tenant.db_name for tenant in tenants}
        cache.set('tenants_map', tenants_map, timeout=None)

    # Schedule the on_commit_callback to be run after the transaction is successfully committed
    try:
        transaction.on_commit(on_commit_callback)

    except Exception as e:
        print(f"-----------------------------------------An error occurred: {e}-------------------------------")
        
        
@receiver(post_delete, sender=Tenant)
def delete_from_tenants_map_cache(sender, instance, **kwargs):
    tenants_map = cache.get('tenants_map')
    if tenants_map is not None:
        name = instance.name
        if name in tenants_map:
            del tenants_map[name]
            cache.set('tenants_map', tenants_map, timeout=None)