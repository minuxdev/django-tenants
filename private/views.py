from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse, render
from django_tenants.utils import connection, get_tenant_model, schema_context

from .models import Lecture


def home(request):
    lectures = Lecture.objects.all()
    context = {"lectures": lectures}
    return render(request, "private/list.html", context)


def get_tenant(request, pk):
    tenant = Client.objects.get(pk=pk)
    return render(request, "private/tenant.html", {"tenant": tenant})


def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = get_user_model().objects.create_superuser(
            username=username, password=password
        )
        return HttpResponse(f"{user} created successfully.")
    return render(request, "private/login.html")
