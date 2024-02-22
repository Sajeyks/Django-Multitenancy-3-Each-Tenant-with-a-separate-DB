from django.contrib import admin
from .models import customer, rocket, payload, launch, Tenant # add Tenant
from .utils import tenant_from_the_request
# Register your models here.


class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdomain_prefix','db_name')

    def db_name(self, obj):
        return "database_"+str(obj.id) 

    db_name.short_description = 'DB Name'
    
    def has_module_permission(self, request):
        current_tenant = tenant_from_the_request(request)
        return current_tenant == 'default'

admin.site.register(Tenant, TenantAdmin)
admin.site.register(customer)
admin.site.register(rocket)
admin.site.register(payload)
admin.site.register(launch)