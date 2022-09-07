from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest.urls')),
    path('api/', include('deepSerializerDemo.urls')),
    path('api/', include('company.urls')),
]
