from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Grade, Lecture

admin.site.register((Grade, Lecture))
