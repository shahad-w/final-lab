from django.urls import path 
from app1 import views 


urlpatterns = [
    path('', views.home , name='home'),
    path('list/', views.list, name='list')
    ]

