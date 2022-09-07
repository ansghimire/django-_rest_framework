from django.contrib import admin

from .models import Company, Document, Shareholders

admin.site.register(Company)
admin.site.register(Document)
admin.site.register(Shareholders)
