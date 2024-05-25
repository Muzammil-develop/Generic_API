from django.urls import path
from home import views

urlpatterns = [
    path ('list' , views.Car_list.as_view () , name='Car_list'),
    path ('<int:pk>' , views.Car_detail.as_view () , name='Car_detail'),
]
