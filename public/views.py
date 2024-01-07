from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import redirect, render

from .models import Client, Domain


def home(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, "list.html", context)


@transaction.atomic()
def create_tenant(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = get_user_model().objects.create_superuser(
            username=username, password=password
        )
        client = Client.objects.create(schema_name=username, name=username)
        Domain.objects.create(domain=client.schema_name, tenant=client)
        return redirect("public:home")
    return render(request, "register.html")
