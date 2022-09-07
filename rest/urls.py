from django.urls import path
from . import views

urlpatterns = [
     path('data/', views.func),
     path('person/', views.PersonView.as_view()),
     path('person-detail/', views.PersonDetailView.as_view()),
]
