from django.urls import path

from . import views

urlpatterns = [
    path("catalog/", views.catalog_page, name="catalog"),
]