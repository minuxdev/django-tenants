from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=30)
    join_date = models.DateField(auto_now_add=True)

    auto_create_schema = True

    def get_absolute_url(self):
        return f"/r/{self.schema_name}/"


class Domain(DomainMixin):
    pass
