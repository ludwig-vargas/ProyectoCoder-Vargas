from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("product/add/", views.ProductCreateView.as_view(), name="product-add"),
    
]
