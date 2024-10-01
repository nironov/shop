from django.urls import path

from . import views

urlpatterns = [
    path("catalog/", views.CatalogPageView.as_view(), name="catalog")
]