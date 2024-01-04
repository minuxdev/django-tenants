# Tenant and domain models
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)


class Domain(DomainMixin):
    pass
