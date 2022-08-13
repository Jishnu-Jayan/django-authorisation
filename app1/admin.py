import django
from django.contrib import admin

# Register your models here.
from app1.models import Application
admin.site.register(Application)