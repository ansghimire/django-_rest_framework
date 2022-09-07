from django.contrib import admin

# Register your models here.
from .models import PersonDetail, Person

admin.site.register(Person)
admin.site.register(PersonDetail)