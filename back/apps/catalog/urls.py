from django.urls import path

from . import views

urlpatterns = [
    path("catalog/", views.catalog_page, name="catalog"),
    path("product/<int:product_id>/", views.product_page, name="product_page"),
]