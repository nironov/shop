from django.urls import path

from . import views

urlpatterns = [
    path("product/<int:product_id>", views.ProductPageView.as_view(), name="product_page"),
]