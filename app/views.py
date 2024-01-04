from django.shortcuts import render

from .models import Lecture


def home(request):
    lectures = Lecture.objects.all()
    context = {"lectures": lectures}
    return render(request, "list.html", context)
