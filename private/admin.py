from django.contrib import admin

from .models import Grade, Lecture

admin.site.register((Grade, Lecture))
