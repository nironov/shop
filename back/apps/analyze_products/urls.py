from django.urls import path
from . import views


urlpatterns = [
    path('api/get_data', views.get_data)
]