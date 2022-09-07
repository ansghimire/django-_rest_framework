from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('company',views.CompanyViewSet)



urlpatterns = [
    
    # path('reg-company/', views.CompanyApiView.as_view(), name="profile")
] 

urlpatterns += router.urls