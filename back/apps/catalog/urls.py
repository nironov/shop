from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path("catalog/", views.catalog_page, name="catalog"),
    path("catalog1/", views.CatalogPageView.as_view(), name="catalog1"),
    path("product/<int:product_id>/", views.product_page, name="product_page"),
]