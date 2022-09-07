from django.urls import path 
from . import views

urlpatterns = [
    path('address/', views.AddressView.as_view(), name="address"),
    path('profile/', views.ProfileView.as_view(), name="profile")
]
