from django.contrib import admin

# Register your models here.
from .models import people,place

admin.site.register(people)
admin.site.register(place)
