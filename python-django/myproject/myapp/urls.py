from django.urls import path

from . import views

urlpatterns = [
    path("products", views.ProductsView.as_view(), name="products"),
    path("create", views.CreateProductsView.as_view(), name="create"),
]
