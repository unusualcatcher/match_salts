

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('/get-medicines/', views.get_medicines, name='get_medicines'),
]
